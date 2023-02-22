from flask import Flask, request, jsonify, redirect, url_for
from langdetect import detect, detect_langs
from iso639 import languages
# import json

app = Flask(__name__)

@app.route('/')
def home():
    return {'value': 'landingpage'}

@app.route('/lg', methods=['GET'])
def languages_route():
    text = request.args.get('id')
    if len(text) == 0:
        return ''
    return detect_language(text)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def default(path):
    return redirect('http://127.0.0.1:5000/', code=302)

def detect_language(text: str) -> dict:

    # detect language
    lang = detect_langs(text)

    # build response 
    response = {'reliable':'', 'language':'', 'short':'', 'prob':''}
    if int(float(str(lang[0])[3::])*100) >= 50:
        response['reliable'] = True
    else:
        response['reliable'] = False
    print(str(lang[0])[0:2])

    # get long name of language
    response['language'] = str(languages.get(alpha2=str(lang[0])[0:2]).name)
    response['short'] = str(lang[0])[0:2]
    print(str(lang[0])[3::])

    # calculate probability
    response['prob'] = int(float(str(lang[0])[3::])*100)

    print(type(response))

    return response