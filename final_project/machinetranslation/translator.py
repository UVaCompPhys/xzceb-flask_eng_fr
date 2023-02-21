"""En-Fr, Fr-En Language Translator"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

#apikey = os.environ['apikey']
#url = os.environ['url']

apikey='AjqpVEQeVg-Ri_uUBcNvdC0IokVTbYR3IYgbyHF5vj5l'
url='https://api.us-east.language-translator.watson.cloud.ibm.com/instances/20549ced-79d0-4833-886f-2342752c1e22'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def englishToFrench(english_text):
    """English to French Translator"""
    french_translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()

    french_full_string = str(french_translation['translations'][0])
    final_french_string = str(french_full_string[17:len(french_full_string)-2])
    return final_french_string


def frenchToEnglish(french_text):
    """French to English Translator"""
    english_translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()

    english_full_string = str(english_translation['translations'][0])
    final_english_string = str(english_full_string[17:len(english_full_string)-2])
    return final_english_string
