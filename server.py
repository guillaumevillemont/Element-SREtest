#!element/bin/python
from flask import Flask, jsonify, abort, make_response, request
#import hashlib
from hashlib import blake2b
app = Flask(__name__)

domain='domain.tld'
blake2b(digest_size=20)
urls = [
    {
        'id': 1,
        'url': u'https://google.com'
    },
    {
        'id': 2,
        'url': u'https://tigwali.fr'
    }
]

@app.route('/api/v1/lookup/<int:identifier>', methods=['GET'])
def get_url(identifier):
    url = [url for url in urls if url['id'] == identifier]
    if len(url) == 0:
        abort(404)
    return jsonify({'url': url[0]})
@app.route('/api/v1/shorten', methods=['POST'])
def create_url():
    if not request.json or not 'url' in request.json:
        abort(400)
    id = blake2b(str(request.json['url']).encode('utf-8')).hexdigest()
    item = {
        'id': id,
        'url': request.json['url']
    }
    urls.append(item)
    return 'http://%s/%s' % (domain, id), 200
    #return jsonify({'url': url}), 201
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)