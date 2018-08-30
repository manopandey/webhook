from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods = ['POST'])
def webhook():
    return(str(request.json))







if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
