from flask import redirect, render_template, session, request,logging
from app.dbservices import crud
from app import app
from app.machine_learning.watson import watsonhandler
from werkzeug.security import generate_password_hash, check_password_hash
from flask_socketio import SocketIO, join_room


db = crud()
wh =watsonhandler()
socketio = SocketIO(app)
@app.route('/')
@app.route('/index',methods=['POST','GET'])
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
            return render_template('login.html', error = error)
        else:
            if check_password_hash(doc['password'],password):
                session['user_id'] = email
                doc = db.search_feature(email, 'login_credentials')
                username = doc['username']
                return redirect('interaction/'+str(username))
            else:
                error = "Incorrect login credentials"
                return render_template('login.html',error = error)
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
                return redirect('/login')
    return render_template('register.html')


@app.route('/interaction/<string:username>')
def interaction(username):
    [session_id, assistant] = wh.get_session_id()
    return render_template('interaction.html', username=username, session_id = session_id)


@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('/index')


@socketio.on('join_room')
def handle_session_joining_event(data):
    print("The user " + data['username'] + "is connected to room " + data['session_id'])
    join_room(data['session_id'])


@socketio.on('send_message')
def handle_send_message(data):
    print("Sent_User: "+data['username']+"\nMessage:"+data['message']+"\nSession_id:"+ data['session_id'])
    socketio.emit('recieve_message', data, room=data['session_id'])
