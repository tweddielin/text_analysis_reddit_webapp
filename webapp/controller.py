from flask import render_template, request, url_for, jsonify
from webapp import app, model, draw

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        posttext = request.form['posttext']
        if posttext is not "":
            result = model.find_most_similar_topic(posttext, 10)
            labels = list(map(lambda i: i[0], result))
            values = list(map(lambda i: i[1], result))
            script, div = draw.make_bar_plot(labels, values)
            return render_template("index.html", results=result, script=script, div=div)
    return render_template("index.html")

@app.route('/get_similar_word', methods=['GET'])
def get_similar():
    word = str(request.args.get('word'))
    topn = int(request.args.get('topn'))
    try:
        result = model.find_most_similar(word, topn)
        return jsonify(results=result)
    except:
        print('there are some problems')
        return jsonify({"sorry": "Sorry, no results! Please try again."}), 500


@app.route('/get_similar_words', methods=['GET'])
def get_similar_words():
    words = str(request.args.get('word'))
    topn = int(request.args.get('topn'))
    try:
        result = model.fine_most_similar_words(words, topn)
        return jsonify(results=result)
    except:
        print('there are some problems')
        return jsonify({"sorry": "Sorry, no results! Please try again."}), 500
