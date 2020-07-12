from app.machine_learning.watson import watsonhandler
from app.machine_learning.data_extractor import extractor
from app.dbservices import crud

wh = watsonhandler()
e = extractor()

class convo_handler():

    def server_convo_handler(self, data, email):
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

        [response, context_var] = wh.watson_request(data['session_id'], assistant,
                                                    data['message'], context)

        if 'dob' not in context_var.keys():
            data1 = unpack_response(response, data)
            return(data1)

        elif ('dob' in context.var.keys()) and ('cand_result' not in context_var.keys()):
            dob = context_var['dob']
            result = {'_id': email, 'username': data['username'], 'dob': dob}
            db.search_and_insert(email, 'candidate_features', result, 'create')
            data1 = unpack_response(response, data)
            return data1

        elif ('dob' in context_var.keys()) and ('10th' in context_var['cand_result']):
            result = e.split_and_compile(context_var['cand_result']['10th'])
            result_dict = {'Education': [{'10th standard': result}]}
            db.search_and_insert(email, 'candidate_features', result_dict,'double')
            data1 = unpack_response(response, data)
            return data1

        elif ('dob' in context_var.keys()) and ('12th' in context_var['cand_result']):
            result = e.split_and_compile(context_var['cand_result']['12th'])
            result_dict = {'Education': [{'12th standard': result}]}
            db.search_and_insert(email, 'candidate_features', result_dict,'double')
            data1 = unpack_response(response, data)
            return data1

        elif ('dob' in context_var.keys()) and ('UG' in context_var['cand_result']):
            result = e.split_and_compile(context_var['cand_result']['UG'])
            result_dict = {'Education': [{'UG': result}]}
            db.search_and_insert(email, 'candidate_features', result_dict,'double')
            data1 = unpack_response(data, response)
            return data1

        elif ('dob' in context_var.keys()) and ('Skill' in context_var['cand_result']):

            ##ensure lowercase for skills
            result = e.split_and_compile(context_var['cand_result']['Skill'])
            for i in result:
                i.lower()
            result_dict = {'Skill': result}
            db.search_and_insert(email, 'candidate_features', result_dict, flag= 'single')
            data1 = unpack_response(response, data)
            return data1

        elif ('dob' in context_var.keys()) and ('Hobbies' in context_var['cand_result']):
            result = e.split_and_compile(context_var['cand_result']['Hobbies'])
            result_dict = {'Hobbies': result}
            db.search_and_insert(email, 'candidate_features', result_dict, flag= 'single')
            data1 = unpack_response(response,data)
            return data1

        elif ('dob' in context_var.keys()) and ('Project' in context_var['cand_result']):
            if not context_var['cand_result']['Project']:
                data1 = unpack_response(response, data)
                return data1
            else:
                result = e.split_and_compile(context_var['cand_result']['Project'])
                result_dict = {'Project':{
                    result[0]: [result[1], result[2]]
                }}
                db.search_and_insert(email, 'candidate_features', result_dict, flag = 'double')
                data1 = unpack_response(response, data)
                return data1

        elif ('dob' in context_var.keys()) and ('Internship' in context_var['cand_result']):
            if not context_var['cand_result']['Internship']:
                data1 = unpack_response(response, data)
                return data1
            else:
                result = e.split_and_compile(context_var['cand_result']['Internship'])
                result_dict = {'Internship':{
                    result[0]: [result[1], result[2]]
                }}
                db.search_and_insert(email, 'candidate_features', result_dict, flag = 'double')
                data1 = unpack_response(response, data)
                return data1

        elif ('dob' in context_var.keys()) and ('Achievement' in context_var['cand_result']):
            if not context_var['cand_result']['Achievement']:
                data1 = unpack_response(response, data)
                return data1
            else:
                result_dict = {'Achievement': [context_var['cand_result']['Achievement']]}
                db.search_and_insert(email, 'candidate_features', result_dict, flag = 'ach')
                data1 = unpack_response(response, data)
                return data1
        else:
            data1 = unpack_response(response, data)
            return data1



def unpack_response(response, data):
    for key, value in response.items():
        if key == 'response':
            rep = value
    data1 = {'user': data, 'bot_msg': rep}
    return data1
