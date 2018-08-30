from flask import Flask, request
from subprocess import call

app = Flask(__name__)

@app.route('/webhook', methods = ['POST'])
def webhook():
    call(["git", "pull"])
    return("Done")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
