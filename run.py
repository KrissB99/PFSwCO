from flask import Flask, request
import datetime
import socket

# Dane autora serwera
autor_imie = "Krystyna"
autor_nazwisko = "Banaszewska"

# Port, na którym serwer nasłuchuje
port = 8000

# Adres IP serwera
adres_ip = socket.gethostbyname(socket.gethostname())

# Tworzenie obiektu aplikacji Flask
app = Flask(__name__)

# Obsługa żądania GET
@app.route("/")
def index():
    # Pobranie adresu IP klienta
    adres_ip_klienta = request.remote_addr

    # Pobranie daty i godziny w strefie czasowej klienta
    teraz = datetime.datetime.now()
    strefa_czasowa = datetime.timezone(datetime.timedelta(hours=0))
    teraz_klienta = teraz.astimezone(strefa_czasowa)

    # Tworzenie treści strony informacyjnej
    content = f"<h1>Informacje o kliencie</h1>"
    content += f'<p>Klient: {autor_imie} {autor_nazwisko}</p>'
    content += f"<p>Adres IP klienta: {adres_ip_klienta}</p>"
    content += f"<p>Data i godzina w strefie czasowej klienta: {teraz_klienta}</p>"

    return content

# Uruchomienie serwera
if __name__ == "__main__":
    # Logowanie informacji o uruchomieniu serwera
    teraz = datetime.datetime.now()
    log_info = f"Serwer uruchomiony przez {autor_imie} {autor_nazwisko} na porcie {port} (Adres IP: {adres_ip})"
    print(log_info)

    app.run(host='0.0.0.0', port=port)
