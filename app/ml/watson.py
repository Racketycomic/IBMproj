from ibm_watson import AssistantV2 as ibma
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json


class watsonconnection():
    
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
        'text': 'my name is Vinay S'
    }
).get_result()

print(json.dumps(msg, indent=2))
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

print(json.dumps(resultdict,indent =2))
