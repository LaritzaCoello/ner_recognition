from flask import Flask, jsonify, request
from utils import ner_sentence

app = Flask(__name__)

@app.route('/ner_recognition/', methods=['POST'])
def ner_recognition():
    sentences = request.json.get('sentences', [])

    results = []
    for sent in sentences:
        tmp = ner_sentence(sent)
        results.append({'sentence': sent, 'entities': tmp})
    
    return jsonify({'results': results}), 200

if __name__ == '__main__':
    app.run(debug=True)



