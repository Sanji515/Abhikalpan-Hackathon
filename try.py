import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, KeywordsOptions,EntitiesOptions, RelationsOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2018-11-16',
    iam_apikey='sgggLr1OhziffHvNtMnrcXAZdrwlhRdk_khhWV1BFK_o',
    url='https://gateway-fra.watsonplatform.net/natural-language-understanding/api'
)
def recognize(input_text):
	response = natural_language_understanding.analyze(
	    text=input_text,
	    features=Features(
	        entities=EntitiesOptions(model ='73914a25-4c07-4174-923e-74852b373117')))
	return(response.result['entities'])

x = raw_input()
result = recognize(x)
for i in result:
	print(i['text'])
	print(i['type'])