# PFSwCO_Zadanie1

Programowanie Full-Stack w Chmurze Obliczeniowej

**Zadanie 1**

* **1.1**
> Proszę napisać program serwera (dowolny język programowania), który realizować będzie następującą funkcjonalność:
>- po uruchomieniu kontenera, serwer pozostawia w logach informację o dacie uruchomienia, imieniu i nazwisku autora serwera (imię i nazwisko studenta) oraz porcie
TCP, na którym serwer nasłuchuje na zgłoszenia klienta.
>- na podstawie adresu IP klienta łączącego się z serwerem, w przeglądarce powinna zostać wyświetlona strona informująca o adresie IP klienta i na podstawie tego adresu IP, o dacie i godzinie w jego strefie czasowej.

Strona została stworzona przy użyciu języka Python z biblioteką Flask. Do odcztania adresu IP użyto biblioteki socket, pobieranie dat dzięki bibliotece datetime.

**linijka 13 w pliku run.py:** *socket.gethostbyname(socket.gethostname())* - pobranie adresu IP
**linijka  25 w pliku run.py:** *datetime.datetime.now()* - pobranie terazniejszej daty i czasu
**linijka 26 w pliku run.py:** *datetime.timezone(datetime.timedelta(hours=0))* - pobranie strefy czasowej
**linijka 27 w pliku run.py:** *astimezone()* - obecna data i czas u klienta

| Wyświetlenie strony poprzez wpisanie w przeglądarkę: 

*http://localhost:5000*

* **1.2**
>Opracować plik Dockerfile, który pozwoli na zbudowanie obrazu kontenera realizującego funkcjonalność opisaną w punkcie 1. Przy ocenie brane będzie sposób opracowania tego pliku (wieloetapowe budowanie obrazu, ewentualne wykorzystanie warstwy scratch, optymalizacja pod kątem funkcjonowania cache-a w procesie budowania, optymalizacja pod kątem zawartości i ilości warstw, healthcheck itd ). Dockerfile powinien również zawierać informację o autorze tego pliku (ponownie imię oraz nazwisko studenta).

Plik Dockerfile z komentarzami dostępy w repozytorium.

* **1.3** 

>Opracować plik Dockerfile, który pozwoli na zbudowanie obrazu kontenera realizującego funkcjonalność opisaną w punkcie 1. Przy ocenie brane będzie sposób opracowania tego pliku
(wieloetapowe budowanie obrazu, ewentualne wykorzystanie warstwy scratch, optymalizacja pod kątem funkcjonowania cache-a w procesie budowania, optymalizacja pod kątem zawartości i ilości
warstw, healthcheck itd ). Dockerfile powinien również zawierać informację o autorze tego pliku (ponownie imię oraz nazwisko studenta).

Oto przykład bardziej zaawansowanego pliku Dockerfile, który spełnia wymagania i uwzględnia optymalizację, takie jak wieloetapowe budowanie, minimalizacja warstw, wykorzystanie scratch, optymalizacja cache'a, użycie health check itd.:

# Autor pliku Dockerfile
MAINTAINER Krystyna Banaszewska

# Etap 1: Budowanie aplikacji w języku Python
FROM python:3.9-slim AS builder

# Instalacja zależności systemowych
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Skopiowanie tylko pliku requirements.txt w celu optymalizacji cache'a
COPY requirements.txt .

# Instalacja zależności Python
RUN --mount=type=cache,target=/root/.cache \
    pip install --no-cache-dir -r requirements.txt

# Skopiowanie kodu aplikacji
COPY server.py .

# Etap 2: Budowanie minimalnego obrazu
FROM scratch

# Kopiowanie tylko niezbędnych plików i katalogów z etapu 1
COPY --from=builder /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/
COPY --from=builder /app/server.py /app/

# Ustawienie zmiennej środowiskowej dla Flask
ENV FLASK_APP=/app/server.py

# Definiowanie health check
HEALTHCHECK CMD wget --quiet --tries=1 --spider http://localhost:5000/ || exit 1

# Otwarcie portu
EXPOSE 8000

# Uruchomienie serwera
CMD ["python", "/app/server.py"]
