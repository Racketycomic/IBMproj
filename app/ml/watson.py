from ibm_watson import AssistantV2 as ibma
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

apikey = "v7BXhz6ssuu6N47OyVmm8aOhWlegSPPw5PF4fjEmiM2h"
authenticator = IAMAuthenticator(f'{apikey}')

assistant = ibma(
    version = '2020-04-01',
    authenticator = authenticator
)

assistant.set_service_url("https://api.eu-gb.assistant.watson.cloud.ibm.com/instances/94cb6503-cdf9-42c1-85a4-aa985d281087")

response = assistant.create_session(
    assistant_id = "0e8394dd-c7bb-44a4-ac8c-82943e502433"
).get_result()

print(json.dumps(response, indent=2))
print(response)
msg = assistant.message(
    assistant_id='0e8394dd-c7bb-44a4-ac8c-82943e502433',
    session_id=response['session_id'],
    input={
        'message_type': 'text',
        'text': 'hello'
    }
).get_result()

print(json.dumps(msg, indent=2))
