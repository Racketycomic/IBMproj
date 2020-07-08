from app.machine_learning.watson import watsonhandler
from app.machine_learning.data_extractor import extractor


wh = watsonhandler()


class convo_handler():

    def server_convo_handler(self, data):
        assistant = wh.get_assistant()
        resp = wh.watson_request(data['session_id'], assistant, data['message'])
        for key, value in resp.items():
            if key == 'response':
                rep = value
        data1 = {'user': data, 'bot_msg': rep}
        return(data1)
