from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def i_am_alive():
    return "I am alive 80!"


@app.route('/foo', methods=['GET'])
def i_am_alive2():
    return "bar"


if __name__ == '__main__':
    # app.run(debug=True, port=8080)
    # app.run(debug=True, port=80)
    app.run(host='0.0.0.0', port=80)
