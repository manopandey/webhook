from flask import Flask, request, Response
from subprocess import call

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def webhook():
    print("https://github.com/"+request.json['repository']['full_name'])
    #identify which repo
    #do a git pull in specified repo
    #run pm2 deploy script in repo
    return Response(status=202, mimetype='application/json')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
