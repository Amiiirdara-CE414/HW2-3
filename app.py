from flask import Flask, redirect

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def redirect_to_secret(path):
    return redirect('http://127.0.0.1:5004/secret', code=302)

if __name__ == '__main__':
    from os import getenv
    app.run(host='0.0.0.0', port=int(getenv('PORT', 10000)))
