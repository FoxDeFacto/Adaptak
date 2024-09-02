
# Adapťák VŠPJ

Tento projekt je jednoduchá webová aplikace vytvořená v Pythonu pro organizaci adaptačního kurzu VŠPJ.

## Požadavky

- Python 3.8+
- Flask 2.0+
- Bootstrap 5
- Font Awesome 6

## Instalace

1. Klonujte tento repozitář do svého místního stroje:

    ```bash
    git clone https://github.com/FoxDeFacto/Adaptak.git
    cd Adaptak
    ```

2. Vytvořte virtuální prostředí a aktivujte ho:

    ```bash
    python -m venv venv
    # Na Windows
    venv\Scripts\activate
    # Na macOS/Linux
    source venv/bin/activate
    ```

3. Spusťte aplikaci:

    ```bash
    flask run
    ```

Aplikace bude dostupná na `http://127.0.0.1:5000/`.

## Struktura projektu

- `app/` – Zdrojové soubory aplikace
- `templates/` – HTML šablony
- `static/` – Statické soubory (CSS, JS, obrázky)
- `requirements.txt` – Závislosti Pythonu
