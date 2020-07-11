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
        'text': '22/04/2000',
        'options' : {
            'return_context': True
        }
    },
    context = {
               "skills":{
                   "main skill": {
                       "user_defined": {
                           "flag": 1,
                       }
                   }
               }
    }
).get_result()

print(json.dumps(msg, indent=2))
resultdict ={}

##respomse extraction

for key1, value1 in msg.items():
    if key1 == 'output':
        for key2, value2 in value1.items():
            if key2 == 'generic':
                for i in value2:
                    for key4,value4 in i.items():
                        if key4 == 'text':
                            if 'response' in resultdict.keys():
                                resultdict['response'].append(value4)
                            else:
                                resultdict['response'] = [value4]

print(resultdict)
result ={}
###context variable extraction

for key1, value1 in msg.items():
    if key1 == 'context':
        for key2, value2 in value1.items():
            if key2 == 'skills':
                for key3, value3 in value2.items():
                    for key4, value4 in value3.items():
                        for key5, value5 in value4.items():
                            result[key5] = value5




print(result)


print(json.dumps(resultdict,indent =2))
