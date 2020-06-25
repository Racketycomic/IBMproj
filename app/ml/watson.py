from ibm_watson import AssistantV2 as ibma
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

apikey="w1PWgbjbxMdvIbA6x4J-MbcP46AbPtqyPoi2N_79L-8X"
authenticator = IAMAuthenticator(f'{apikey}')

assistant = ibma(
    version = '2020-06-16',
    authenticator = authenticator
)

assistant.set_service_url("https://api.eu-gb.assistant.watson.cloud.ibm.com/instances/a4b4a8ab-ebad-4b90-9a6c-fb8a73bc683b")

response = assistant.create_session(
    assistant_id = '8257428f-9e0c-48f2-b213-b1f2af28c13e'
).get_result()

print(json.dumps(response,indent=2))
