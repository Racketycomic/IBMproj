from ibm_watson import PersonalityInsightsV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

authenticator = IAMAuthenticator('yLcjP_vAobDEORUcO86S1BttbZVclO3IQzFlIEnIaPKL')
personality_insights = PersonalityInsightsV3(
    version='22-05-2020',
    authenticator=authenticator
)

samp=''
profile = personality_insights.profile(
    samp,
    'application/json',
    content_type='text/plain',
).get_result()

print(profile)
res =[]
for i in profile['personality']:
    pseudo_dict={}
    pseudo_dict['trait_name'] = i['name']
    print(i['name'])
    pseudo_dict['percentile'] = i['percentile']
    res.append(pseudo_dict)
