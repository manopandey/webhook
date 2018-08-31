from flask import Flask, request, Response
from subprocess import call

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def webhook():
    print(request.json)
    return Response(status=202, mimetype='application/json')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
