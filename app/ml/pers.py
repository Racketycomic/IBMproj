from ibm_watson import PersonalityInsightsV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

authenticator = IAMAuthenticator('yLcjP_vAobDEORUcO86S1BttbZVclO3IQzFlIEnIaPKL')
personality_insights = PersonalityInsightsV3(
    version='22-05-2020',
    authenticator=authenticator
)

personality_insights.set_service_url('https://api.eu-gb.personality-insights.watson.cloud.ibm.com/instances/3be001b5-9f13-46ec-bb07-286e363d8ba1')

samp = R'I don’t like personality tests! Whether they reveal something right or wrong about you, I don’t want to reduce people’s understanding of me to four letters, or five numbers, or a few signs. I could write many pages about how this slapdash way of “understanding” a person might lead to discrimination at work, misguided judgment, or violations of one’s privacy, but that’s not quite the point of this blogpost — though it is the motivation behind writing it.Here, I will focus on one specific new form of personality testing — one that relies on machine learning. I’m referring to the IBM Watson product called Personality Insights. According to IBM’s website, the tool “uses linguistic analytics to infer individuals’ intrinsic personality characteristics, including Big Five [or O.C.E.A.N], Needs, and Values, from digital communications such as email, text messages, tweets, and forum posts.” In addition, Personality Insights shows your consumption habits and “temporal behavior”.'

samp2 = R'(if the input text is timestamped).Let me show you what this means. I fed the tool with my Twitter feed and received this nice visualization of the tool’s output, supposedly showing my personality characteristics, consumer needs, and values:'
samp +=samp2
len(samp)
profile = personality_insights.profile(
    samp,
    'application/json',
    content_type='text/plain',
    consumption_preferences=True,
    raw_scores=True
).get_result()

print(profile)

print(json.dumps(profile,indent=2))
