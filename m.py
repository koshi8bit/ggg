from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def i_am_alive():
    return "I am alive 5551!"


@app.route('/tyty', methods=['GET'])
def i_am_alive2():
    return "sam tyty!"


if __name__ == '__main__':
    # app.run(debug=True, port=8080)
    app.run(debug=True, port=5001)