from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def get_public_ip():
    public_ip = requests.get('https://api64.ipify.org?format=json').json()['ip']
    return f"Your Public IP Address: {public_ip}"

if __name__ == '__main__':
    app.run()
