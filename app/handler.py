from app.machine_learning.watson import watsonhandler
from app.machine_learning.data_extractor import extractor
from app.dbservices import crud
from app.test_relate import generate_test


wh = watsonhandler()
e = extractor()

class convo_handler():

    def server_convo_handler(self, data, email):
        assistant = wh.get_assistant()
        db = crud()
        result_dict = {}
        db_doc = db.search_feature(email, 'candidate_features')
        context = {
                   "skills":{
                       "main skill": {
                           "user_defined": {
                               "flag": 1,
                               "first_round_flag": db_doc['first_round_flag'],
                               'test_link_share':db_doc['test_link_share']
                           }
                       }
                   }
        }

        response, contextvariable = wh.watson_request(data['session_id'], assistant,
                                                    data['message'], context)
        print(contextvariable)
        if 'dob' not in contextvariable.keys():
            data1 = unpack_response(response, data)
            return(data1)

        elif ('dob' in contextvariable.keys()) and ('cand_result' not in contextvariable.keys()):
            dob = contextvariable['dob']
            result = {'dob': dob}
            db.search_and_insert(email, 'candidate_features', result, 'single')
            data1 = unpack_response(response, data)
            return data1

        elif ('dob' in contextvariable.keys()) and ('10th' in contextvariable['cand_result']):
            result = e.split_and_compile(contextvariable['cand_result']['10th'])
            for index, val in enumerate(result):
                if index == 2:
                    result[index] = float(result[index])
            result_dict = {'Education': {'UG': result}}
            result_dict = {'Education': {'10th standard': result}}
            db.search_and_insert(email, 'candidate_features', result_dict,'double')
            data1 = unpack_response(response, data)
            return data1

        elif ('dob' in contextvariable.keys()) and ('12th' in contextvariable['cand_result']):
            result = e.split_and_compile(contextvariable['cand_result']['12th'])
            for index, val in enumerate(result):
                if index == 2:
                    result[index] = float(result[index])
            result_dict = {'Education': {'UG': result}}
            result_dict = {'Education': {'12th standard': result}}
            db.search_and_insert(email, 'candidate_features', result_dict,'double')
            data1 = unpack_response(response, data)
            return data1

        elif ('dob' in contextvariable.keys()) and ('UG' in contextvariable['cand_result']):
            result = e.split_and_compile(contextvariable['cand_result']['UG'])
            for index, val in enumerate(result):
                if index == 2:
                    result[index] = float(result[index])
            result_dict = {'Education': {'UG': result}}
            db.search_and_insert(email, 'candidate_features', result_dict,'double')
            data1 = unpack_response(response, data)
            return data1

        elif ('dob' in contextvariable.keys()) and ('Skill' in contextvariable['cand_result']):

            ##ensure lowercase for skills
            result = e.split_and_compile(contextvariable['cand_result']['Skill'])
            result = [i.lower() for i in result]
            result_dict = {'Skill': result}
            db.search_and_insert(email, 'candidate_features', result_dict, flag= 'single')
            data1 = unpack_response(response, data)
            return data1

        elif ('dob' in contextvariable.keys()) and ('Hobbies' in contextvariable['cand_result']):
            result = e.split_and_compile(contextvariable['cand_result']['Hobbies'])
            result_dict = {'Hobbies': result}
            db.search_and_insert(email, 'candidate_features', result_dict, flag= 'single')
            data1 = unpack_response(response,data)
            return data1

        elif ('dob' in contextvariable.keys()) and ('Project' in contextvariable['cand_result']):
            if not contextvariable['cand_result']['Project']:
                data1 = unpack_response(response, data)
                return data1
            else:
                result = e.split_and_compile(contextvariable['cand_result']['Project'])
                result_dict = {'Project': {
                    result[0]: [result[1], result[2]]
                }}
                db.search_and_insert(email, 'candidate_features', result_dict, flag = 'double')
                data1 = unpack_response(response, data)
                return data1

        elif ('dob' in contextvariable.keys()) and ('Internship' in contextvariable['cand_result']):
            if not contextvariable['cand_result']['Internship']:
                data1 = unpack_response(response, data)
                return data1
            else:
                result = e.split_and_compile(contextvariable['cand_result']['Internship'])
                result_dict = {'Internship': {
                    result[0]: [result[1], result[2]]
                }}
                db.search_and_insert(email, 'candidate_features', result_dict, flag = 'double')
                data1 = unpack_response(response, data)
                return data1

        elif ('dob' in contextvariable.keys()) and ('Achievement' in contextvariable['cand_result']):
            rek = {}
            if not contextvariable['cand_result']['Achievement']:
                my_document = db.search_feature(email, 'candidate_features')
                if my_document['Education'][2]['UG'][2] >= 7.0:
                    rek['first_round_flag'] = 'Pass'
                    rek['test_link_share'] = "http://127.0.0.1:5000/test"
                    db.search_and_insert(email, 'candidate_features', rek, flag ='single')
                else:
                    my_document['first_round_flag'] = 'Fail'
                    db.search_and_insert(email, 'candidate_features', rek, flag ='single')
                data1 = unpack_response(response, data)
                return data1
            else:
                result_dict = {'Achievement': contextvariable['cand_result']['Achievement']}
                data1 = unpack_response(response, data)
                return data1
        else:
            data1 = unpack_response(response, data)
            return data1


    def hr_session_handler()

def unpack_response(response, data):
    for key, value in response.items():
        if key == 'response':
            rep = value
    data1 = {'user': data, 'bot_msg': rep}
    return data1
