from flask import Flask, send_file

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return 'server is running...'

@app.route('/flag')
def flag():
    return 'CE441{test_flag_value}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
