from flask import redirect, render_template, session, request, make_response
from app.dbservices import crud
from app import app
from app.machine_learning.watson import watsonhandler
from werkzeug.security import generate_password_hash, check_password_hash
from flask_socketio import SocketIO, join_room
from app.handler import convo_handler
from app.machine_learning.data_extractor import extractor
from app.test_relate import generate_test as gt
from app.candidate_scoring import scoring as sc
from app.machine_learning import pers as pp
import json
import pdfkit

db = crud()
cand = {}
hand = convo_handler()
wh = watsonhandler()
socketio = SocketIO(app)


@app.route('/')
@app.route('/index', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        session.pop('user_id', None)
        doc = db.search_feature(email, 'login_credentials')
        print(doc)
        if len(doc) == 0:
            error = 'Email not found please sign in'
            return render_template('login.html', error=error)
        else:
            if check_password_hash(doc['password'], password):
                session['user_id'] = email
                doc = db.search_feature(email, 'login_credentials')
                username = doc['username']
                return redirect('interaction/'+str(username))
            else:
                error = "Incorrect login credentials"
                return render_template('login.html', error=error)
    return render_template('login.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        repass = request.form['repass']
        doc = db.search_feature(email, "login_credentials")
        if len(doc) != 0:
            error = "The email already exists"
            render_template('register.html', error=error)
        else:
            if password == repass:
                hash = generate_password_hash(password)
                cdict = {'_id': email, 'username': username, 'password': hash,
                         'email': email}
                db.insert_feature(cdict, 'login_credentials')
                result = {'_id': session['user_id'], 'username': username, 'first_round_flag':'','test_link_share':''}
                db.insert_feature(result, 'candidate_features')
                return redirect('/login')
    return render_template('register.html')



@app.route('/interaction/<string:username>',methods =['POST','GET'])
def interaction(username):
    assistant = wh.get_assistant()
    id = wh.get_session_id(assistant)
    print(id+"SEE HERE SESSION ID")
    botintro = "Hi!! I'm REBOS, I'll be taking you through the recruitment process and help you clarify your queries."
    return render_template('interaction.html', username=username, session_id=id,
                           botintro=botintro)


@app.route('/evaluation', methods = ['POST','GET'])
def eval():
    score = 0
    questions = session.get('question_dict',None)
    for i in range(len(questions)):
        try:
            q1 = request.form[f'q{i+1}']
        except:
            continue
        if q1 == questions[i]['answer']:
            score += 1
    final_score = sc.totalscoring(session['user_id'])
    if final_score > 1500:
        result = {'_id': session['user_id']}
        flag = 'Pass'
        db.insert_feature(result, 'hr_question')
    else:
        result = {'_id': session['user_id']}
        flag = 'Fail'
        db.insert_feature(result, 'hr_question')

    print("SEEE THE SCORE HERE",str(score),str(final_score))
    print(flag)
    assistant = wh.get_assistant()
    id = wh.get_session_id(assistant)
    rek = db.search_feature(session['user_id'], 'login_credentials')
    username = rek['username']
    context = {
               "skills": {
                   "main skill": {
                       "user_defined": {
                           "flag": 1,
                           "second_round_flag": flag,
                           "username": username
                       }
                   }
               }
            }

    response, contextvariable = wh.watson_request(id, assistant,
                                                    'hr', context)
    response = response['response']
    return render_template('interaction2.html', response = response , session_id =id, username = username)


@app.route('/test', methods=['POST', 'GET'])
def testing():
    k = 1
    questions = gt.gettest(session['user_id'])
    print(questions)
    for i in questions:
        for key, value in i.items():
            if key == 'question_number':
                i[key] = k
                k += 1
    session['question_dict'] = questions

    return render_template('tests.html', questions = questions)


@app.route('/result', methods=['POST', 'GET'])
def report_generate():
    init_doc = db.search_feature(session['user_id'], 'hr_question')
    features = db.search_feature(session['user_id'], 'candidate_features')
    res_str = ''
    for i in range(len(init_doc)):
        try:
            res_str += '.' + init_doc[f'ans{i}']
        except:
            pass
    res_str = res_str[1:]
    print(res_str)
    insights_dict = pp.get_personality_insights(res_str)
    result_str = sc.personality_insight(insights_dict, session['user_id'])
    features = {
                "_id": "yondo@gmail.com",
                "_rev": "40-d26758433c9ad24b6fd734ce68c2c6c9",
                "username": "yondo",
                "first_round_flag": "Pass",
                "test_link_share": "http://127.0.0.1:5000/test",
                "dob": "2020-03-04",
                "Education": [
                {
                "10th standard": [
                "2000",
                "KSEEB",
                90,
                "Vidyanikethan Public school"
                ]
                },
                {
                "12th standard": [
                "2002",
                "KSEEB",
                90,
                "Narayana PU college"
                ]
                },
                {
                          "UG": [
                            "2006",
                            "VTU",
                            9.5,
                            "BNMIT"
                          ]
                        }
                      ],
                      "Skill": [
                        "java",
                        "python",
                        "javascript"
                      ],
                      "Hobbies": [
                        "Football",
                        "Cricket",
                        "Basketball",
                        "Anime"
                      ],
                      "Project": [
                        {
                          "Project 1": [
                            "JAVA",
                            "Description 1"
                          ]
                        },
                        {
                          "Project 2": [
                            "Python,AI,Machine Learning",
                            "Description 2"
                          ]
                        },
                        {
                          "Project 3": [
                            "JS,Machine Learning,Java,Python",
                            "Description 3"
                          ]
                        }
                      ],
                      "Internship": [
                        {
                          "Amazon": [
                            "3 months",
                            "Description 1"
                          ]
                        },
                        {
                          "Google": [
                            "3 months",
                            "Description 2"
                          ]
                        },
                        {
                          "FaceBook": [
                            "3 months",
                            "Description 3"
                          ]
                        }
                      ],
                      "Achievement": [
                        "Achievement1",
                        "Achievement2"
                      ]
                    }
    final_result = {}
    final_result['name'] = features['username']
    final_result['email'] = features['_id']
    final_result['dob'] = features['dob']
<<<<<<< HEAD
    print(final_result)
    final_result['10th standard'] = {'Year': features['Education'][0]['10th standard'][0]}
    final_result['10th standard'] = {'Board': features['Education'][0]['10th standard'][1]}
    final_result['10th standard'] = {'Marks': features['Education'][0]['10th standard'][2]}
    final_result['10th standard'] = {'School name': features['Education'][0]['10th standard'][3]}
    final_result['12th standard'] = {'Year' : features['Education'][1]['12th standard'][0]}
    final_result['12th standard'] = {'Board': features['Education'][1]['12th standard'][1]}
    final_result['12th standard'] = {'Marks': features['Education'][1]['12th standard'][2]}
    final_result['12th standard'] = {'College name' :features['Education'][1]['12th standard'][3]}
    final_result['UG'] = {'Year': features['Education'][2]['UG'][0]}
    final_result['UG'] = {'University': features['Education'][2]['UG'][1]}
    final_result['UG'] = {'CGPA': features['Education'][2]['UG'][2]}
    final_result['UG'] = {'College name': features['Education'][2]['UG'][3]}
    final_result['Skills'] = features['result']
=======
    final_result['10th standard']['Year'] = features['Education'][0]['10th standard'][0]
    final_result['10th standard']['Board'] = features['Education'][0]['10th standard'][1]
    final_result['10th standard']['Marks'] = features['Education'][0]['10th standard'][2]
    final_result['10th standard']['School name'] = features['Education'][0]['10th standard'][3]
    final_result['12th standard']['Year'] = features['Education'][1]['12th standard'][0]
    final_result['12th standard']['Board'] = features['Education'][1]['12th standard'][1]
    final_result['12th standard']['Marks'] = features['Education'][1]['12th standard'][2]
    final_result['12th standard']['College name'] = features['Education'][1]['12th standard'][3]
    final_result['UG']['Year'] = features['Education'][2]['UG'][0]
    final_result['UG']['University'] = features['Education'][2]['UG'][1]
    final_result['UG']['CGPA'] = features['Education'][2]['UG'][2]
    final_result['UG']['College name'] = features['Education'][2]['UG'][3]
    final_result['Skills'] = features['Skill']
>>>>>>> 27e4e31b8d7687d64911815d39c27678e9ae20d4
    final_result['Hobbies'] = features['Hobbies']
    final_result['Achievement'] = features['Achievement']
    pcounter = 1
    for key,value in features.items():
        if key == 'Project':
            for i in value:
                for key1, value1 in i.items():
                    final_result['Project'] ={f'Project_Title{pcounter}': key1}
                    pcounter += 1
                    for index,v in enumerate(value1):
                        if index == 0:
                            final_result['Project'] = {f'Project_tech{pcounter}':v}
                        else:
                            final_result['Project'] = {f'Project_desc{pcounter}': v}
    pcounter = 1
    for key,value in features.items():
        if key == 'Internship':
            for i in value:
                for key1, value1 in i.items():
                    final_result['Internship'] = {f'Internship_Title{pcounter}': key1}
                    pcounter += 1
                    for index,v in enumerate(value1):
                        if index == 0:
                            final_result['Internship'] = {f'Duration{pcounter}': v}
                        else:
                            final_result['Intership'] = {f'Internship_desc{pcounter}': v}


    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    rendered = render_template('result.html', final_result = final_result)
    pdf = pdfkit.from_string(rendered, False, configuration=config)
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = f"attachement; filename = {features['_id']}.pdf"
    return(response)


@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('/index')


@socketio.on('join_room')
def handle_session_joining_event(data):
    print(data['session_id'])
    print("The user " + data['username'] + " is connected to room " +
          data['session_id'])
    join_room(data['session_id'])


@socketio.on('send_message')
def handle_send_message(data):
    print("Sent_User: " + data['username'] + "\nMessage:" + data['message'] +
          "\nSession_id:" + data['session_id'])
    socketio.emit('1st_message',data, room = data['session_id'])
    data1 = hand.server_convo_handler(data, session['user_id'])
    global counter
    counter += 1
    socketio.emit('recieve_message', data1, room=data['session_id'])

@socketio.on('send_message2')
def handle_send_message(data):
    print("Sent_User: " + data['username'] + "\nMessage:" + data['message'] +
          "\nSession_id:" + data['session_id'])
    socketio.emit('1st_message',data, room = data['session_id'])
    data1 = hand.second_conversation(data, session['user_id'])
    print("Inside msg2")
    socketio.emit('recieve_message', data1, room=data['session_id'])
