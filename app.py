from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return jsonify(message="this is my first flask app, yay!")

if __name__ == '__main__':
    app.run(debug = True) 
