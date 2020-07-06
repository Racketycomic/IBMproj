from ibm_watson import AssistantV2 as ibma
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json
from flask import current_app


class watsonhandler():

    def get_assistant(self):
        authenticator = IAMAuthenticator(current_app.config['WT_APIKEY'])
        assistant = ibma(
            version=current_app.config['WT_VERSION'],
            authenticator=authenticator
        )
        assistant.set_service_url(current_app.config['WT_URL'])
        return assistant

    def get_session_id(self, assistant):
        response = assistant.create_session(
            assistant_id=current_app.config['WT_ASSISTANT_ID']
        ).get_result()
        print(json.dumps(response, indent=2))
        session_id = response['session_id']
<<<<<<< HEAD
        return (session_id, assistant)
=======
        return [session_id, assistant]
>>>>>>> 5b3f0c52e109350b5d390a0573f8df228333dfbd

    def watson_request(self, session_id, assistant, text):
        msg = assistant.message(
            assistant_id=current_app.config['WT_ASSISTANT_ID'],
            session_id=session_id,
            input={
                'message_type': 'text',
                'text': text
            }
        ).get_result()
<<<<<<< HEAD
        return (msg['output'])
=======
        resultdict ={}
        for key1,value1 in msg.items():
            if key1 == 'output':
                for key2, value2 in value1.items():
                    if key2 == 'entities':
                        for i in value2:
                            for key3, value3 in i.items():
                                if key3 == 'entity':
                                    skey = value3
                                if key3 == 'value':
                                    svalue = value3
                            resultdict[skey] = svalue
                    if key2 == 'generic':
                        for i in value2:
                            for key4,value4 in i.items():
                                if key4 == 'text':
                                    if 'response' in resultdict.keys():
                                        resultdict['response'].append(value4)
                                    else:
                                        resultdict['response'] = [value4]

        return (resultdict)
>>>>>>> 5b3f0c52e109350b5d390a0573f8df228333dfbd
