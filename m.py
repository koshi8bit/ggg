from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def i_am_alive():
    return "I am alive 80!"


@app.route('/t', methods=['GET'])
def i_am_alive2():
    return "sam tyty!"


if __name__ == '__main__':
    # app.run(debug=True, port=8080)
    app.run(debug=True, port=80)
    