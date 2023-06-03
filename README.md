# PFSwCO_Zadanie1

Programowanie Full-Stack w Chmurze Obliczeniowej

**1.1** Proszę napisać program serwera (dowolny język programowania), który realizować będzie następującą funkcjonalność:
- po uruchomieniu kontenera, serwer pozostawia w logach informację o dacie uruchomienia, imieniu i nazwisku autora serwera (imię i nazwisko studenta) oraz porcie
TCP, na którym serwer nasłuchuje na zgłoszenia klienta.
- na podstawie adresu IP klienta łączącego się z serwerem, w przeglądarce powinna zostać wyświetlona strona informująca o adresie IP klienta i na podstawie tego adresu IP, o dacie i godzinie w jego strefie czasowej.

Strona została stworzona przy użyciu języka Python z biblioteką Flask. Do odcztania adresu IP użyto biblioteki socket, pobieranie dat dzięki bibliotece datetime.

**linijka 13 w pliku run.py:** *socket.gethostbyname(socket.gethostname())* - pobranie adresu IP

**linijka  25 w pliku run.py:** *datetime.datetime.now()* - pobranie terazniejszej daty i czasu

**linijka 26 w pliku run.py:** *datetime.timezone(datetime.timedelta(hours=0))* - pobranie strefy czasowej

**linijka 27 w pliku run.py:** *astimezone()* - obecna data i czas u klienta

| Wyświetlenie strony poprzez wpisanie w przeglądarkę: *http://localhost:5000*

---

**1.2** Opracować plik Dockerfile, który pozwoli na zbudowanie obrazu kontenera realizującego funkcjonalność opisaną w punkcie 1. Przy ocenie brane będzie sposób opracowania tego pliku (wieloetapowe budowanie obrazu, ewentualne wykorzystanie warstwy scratch, optymalizacja pod kątem funkcjonowania cache-a w procesie budowania, optymalizacja pod kątem zawartości i ilości warstw, healthcheck itd ). Dockerfile powinien również zawierać informację o autorze tego pliku (ponownie imię oraz nazwisko studenta).

Plik Dockerfile z komentarzami dostępy w repozytorium.

---

**1.3** Niezbędne polecenia
    
a. Zbudowanie opracowanego obrazu kontenera

    *docker build -t my_container:1 -f Dockerfile .*

b. Uruchomienie kontenera na podstawie zbudowanego obrazu,

    *docker run -p 8000:8000 my_container:1*

c. Sposób uzyskania informacji, które wygenerował serwer w trakcie uruchamiana kontenera (patrz: punkt 1a),

    *docker logs my_container*

d. Ilość warstw zbudowanego obrazu.

    *docker history my_container:1*
