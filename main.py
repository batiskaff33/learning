import requests
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    currencies = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').text
    return currencies
    #return 'test'

if __name__ == "__main__":
    app.run()
