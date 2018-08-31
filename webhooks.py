from flask import Flask, request, Response
import os

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def webhook():
    os.system('( cd /var/www/html/'request.json['repository']['name']' ; sudo git pull )')
    return(str(request.json['repository']['clone_url']))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

