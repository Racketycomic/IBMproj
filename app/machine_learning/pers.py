from ibm_watson import PersonalityInsightsV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json
from flask import current_app


def get_personality_insights(text, samp):
    authenticator = IAMAuthenticator(current_app.config['INSIGHTS_API'])
    personality_insights = PersonalityInsightsV3(
        version = current_app.config['INSIGHTS_VER'],
        authenticator=authenticator
    )

    personality_insights.set_service_url(current_app.config['INSIGHTS_URL'])
    profile = personality_insights.profile(
        samp,
        'application/json',
        content_type='text/plain',
    ).get_result()
    print(profile)
    res = []
    for i in profile['personality']:
        pseudo_dict={}
        pseudo_dict['trait_name'] = i['name']
        print(i['name'])
        pseudo_dict['percentile'] = i['percentile']
        res.append(pseudo_dict)

    return res
    
