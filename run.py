import datetime
import socket
import json
from flask import Flask, request

app = Flask(__name__)

def get_client_ip() -> str:
  "Pobieranie adresu IP klienta"
    if 'X-Forwarded-For' in request.headers:
        ip = request.headers['X-Forwarded-For']
    else:
        ip = request.remote_addr
    return ip

def get_client_datetime(ip) -> datetime:
    "Zwracanie informacji o dacie i godzinie w strefie czasowej klienta"
    client_datetime = datetime.datetime.now()
    return client_datetime.strftime('%Y-%m-%d %H:%M:%S')

@app.route('/')
def index():
  "Obsługa żądania klienta"
    client_ip = get_client_ip()
    client_datetime = get_client_datetime(client_ip)
    response = {
        'client_ip': client_ip,
        'client_datetime': client_datetime
    }
    return json.dumps(response)

if __name__ == '__main__':
    author = 'Krystyna Banaszewska'
    port = 5000

    start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'Server started at {start_time}')
    print(f'Author: {author}')
    print(f'Listening on port: {port}')

    app.run(host='0.0.0.0', port=port)
