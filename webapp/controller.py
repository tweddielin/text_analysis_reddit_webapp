from flask import render_template, request, url_for, jsonify
from webapp import app, model, draw


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template("index.html")

@app.route('/<word>/get_similar/', methods=['GET'])
def get_similar(word):
    try:
        return jsonify(results=result)
    except:
        print('there are some problems')
        return jsonify({"sorry": "Sorry, no results! Please try again."}), 500

