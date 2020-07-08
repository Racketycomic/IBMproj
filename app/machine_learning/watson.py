from ibm_watson import AssistantV2 as ibma
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json
from flask import current_app
from app.machine_learning.data_extractor import extractor

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


        return (session_id)


    def watson_request(self, session_id, assistant, text):
        msg = assistant.message(
            assistant_id=current_app.config['WT_ASSISTANT_ID'],
            session_id=session_id,
            input={
                'message_type': 'text',
                'text': text
            }
        ).get_result()

        return (msg['output'])
