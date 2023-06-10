# Sprawozdanie - Zadanie 2

## Repozytorium GitHub

Link do repozytorium GitHub zawierającego kod serwera oraz konfigurację Dockerfile i GitHub Actions:
[MojeRepozytorium](https://github.com/KrissB99/PFSwCO_Zadanie1)

## DockerHub

Link do repozytorium DockerHub, w którym przechowywane są obrazy kontenera:
[DockerHub](https://hub.docker.com/r/krissb99/pfswco)

## Opis zawartości repozytorium

Repozytorium zawiera następujące pliki:

- `run.py`: Kod serwera w języku Python, który realizuje funkcjonalność opisaną w zadaniu.
- `Dockerfile`: Plik Dockerfile do budowy obrazu kontenera z serwerem.
- `.github/workflows/build.yaml`: Plik konfiguracyjny GitHub Actions, który buduje obrazy kontenera dla różnych architektur i publikuje je na DockerHub.
- `zadanie2.md`: Plik sprawozdania, w którym opisane są informacje o repozytorium, linki do GitHub i DockerHub.

## Opis działania łańcucha GitHub Actions

1. Po każdym pushu do brancha `main`, łańcuch GitHub Actions jest uruchamiany.
2. Pobierany jest kod źródłowy z repozytorium przy użyciu akcji `actions/checkout`.
3. Następnie jest ustawiany QEMU dla obsługi architektury ARM64 i Docker Buildx dla wieloplatformowej budowy obrazów.
4. Dwie akcje `docker/build-push-action` są wykorzystywane do budowy i publikowania obrazów dla architektur `linux/arm64/v8` i `linux/amd64`.
5. Obrazy są budowane na podstawie pliku `Dockerfile` i oznaczane odpowiednimi tagami.
6. Zbudowane obrazy kontenera są publikowane w repozytorium DockerHub pod wskazanymi tagami.

