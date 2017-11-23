import io
from google.cloud import vision
from google.oauth2 import service_account
#
# from oauth2client.client import GoogleCredentials
# credentials = GoogleCredentials.get_application_default()
# credentials = service_account.Credentials.from_service_account_file("gcloudcredentials.json")
vision_client = vision.Client()
# file_name = 'Guido_van_Rossum_OSCON_2006_cropped.png'
# file_name='anatomy_of_matplotlib_plots.png'

# with io.open(file_name, 'rb') as image_file:
#     content = image_file.read()
#     image = vision_client.image(
#         content=content, )
#
# labels = image.detect_labels()
# for label in labels:
#     print(label.description)

file_name = 'block-of-text.png'
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()
    image = vision_client.image(
        content=content, )
# print(dir(image))
# print(image.detect_full_text().text)
labels = image.detect_labels()
# for label in labels:
    # print(label.description, label.score)


from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def print_result(annotations, entities):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        print('Sentence {} has a sentiment score of {}'.format(
            index, sentence_sentiment))

    print('Overall Sentiment: score of {} with magnitude of {}'.format(
        score, magnitude))


    print(entities)
    return 0

def language_analysis(text):
    # language.LanguageServiceClient
    client = language.LanguageServiceClient()
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)
    # document = client.document_from_text(text)
    sent_analysis = client.analyze_sentiment(document=document)
    dir(sent_analysis)
    # sentiment = sent_analysis.sentiment
    doc = types.Document(
        content='python, oracle are very powerful language and tool.',
        type=enums.Document.Type.PLAIN_TEXT)
    ent_analysis = client.analyze_entities(document=doc)
    # print(dir(ent_analysis))
    # entities = ent_analysis.entities

    return print_result(sent_analysis,ent_analysis)

example_text = image.detect_full_text().text
language_analysis(example_text)
