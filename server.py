#!element/bin/python
# -*- coding: utf-8 -*-

"""This is a awesome
        python script!"""

from flask import Flask, jsonify, abort, make_response, request
import hashlib, json
app = Flask(__name__)

domain=u'domain.tld'
salt_key=b'toto'

urls = {
    'e1ea94a8d3': 'https://google.com',
    '2b039fbaa1': 'https://tigwali.fr'
}

@app.route('/api/v1/lookup/<identifier>', methods=['GET'])
def get_url(identifier):
    if identifier in urls:
        return urls[identifier]
    else:
        abort(404)

@app.route('/api/v1/list', methods=['GET'])
def get_urls():
    json_object = json.dumps(urls, indent = 4) 
    return json_object, 200

@app.route('/api/v1/shorten', methods=['POST'])
def create_url():
    if not request.json or not 'url' in request.json:
        abort(400)
    id = hashlib.blake2b(str(request.json['url']).encode('utf-8'), digest_size=5, salt=salt_key).hexdigest()
    urls[id] = request.json['url']
    return 'https://%s/%s' % (domain, id), 200

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
