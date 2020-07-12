from app.machine_learning.watson import watsonhandler
from app.machine_learning.data_extractor import extractor
from app.dbservices import crud

wh = watsonhandler()
e = extractor()

class convo_handler():

    def server_convo_handler(self, data, counter, email):
        assistant = wh.get_assistant()
        db = crud()
        result_dict = {}
        context = {
                   "skills":{
                       "main skill": {
                           "user_defined": {
                               "flag": 1,
                           }
                       }
                   }
        }
        context.skills
        [response, context_var] = wh.watson_request(data['session_id'], assistant,
                                                    data['message'], context)

        if 'dob' not in context_var.keys():
            for key, value in response.items():
                if key == 'response':
                    rep = value
            data1 = {'user': data, 'bot_msg': rep}
            return(data1)

        elif 'dialog_flag' not in context_var.keys():
            dob = context_var['dob']
            result = {'dob': dob}
            db.search_and_insert(email, 'candidate_features', result)
            for key, value in response.items():
                if key == 'response':
                    rep = value
            data1 = {'user': data, 'bot_msg': rep}
            return data1

        elif context_var['dialog_flag'] is '10th':
            result = e.split_and_compile(data['message'])
            result_dict = {'Education': [{'10th standard': result}]}
            db.search_and_insert(email, 'candidate_features', result_dict)
            for key, value in response.items():
                if key == 'response':
                    rep = value
            data1 = {'user': data, 'bot_msg': rep}
            return data1

        elif context_var['dialog_flag'] is '12th':
            result = e.split_and_compile(data['message'])
            result_dict = {'Education': [{'12th standard': result}]}
            db.search_and_insert(email, 'candidate_features', result_dict)
            for key, value in response.items():
                if key == 'response':
                    rep = value
            data1 = {'user': data, 'bot_msg': rep}
            return data1

        elif context_var['dialog_flag'] is 'UG':
            result = e.split_and_compile(data['message'])
            result_dict = {'Education': [{'UG': result}]}
            db.search_and_insert(email, 'candidate_features', result_dict)
            for key, value in response.items():
                if key == 'response':
                    rep = value
            data1 = {'user': data, 'bot_msg': rep}
            return data1

        elif context_var['dialog_flag'] is 'skill':
            result = e.split_and_compile(data['message'])
            result_dict = {'skill': result}
            db.search_and_insert(email, 'candidate_features', result_dict)
            for key, value in response.items():
                if key == 'response':
                    rep = value
            data1 = {'user': data, 'bot_msg': rep}
            return data1


def unpack_response(response,data):
    for key, value in response.items():
        if key == 'response':
            rep = value
    data1 = {'user': data, 'bot_msg': rep}
    return data1
