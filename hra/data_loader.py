import json
from pathlib import Path

DATA = Path(__file__).parent / "data"

def nacitaj(nazov):
    cesta = DATA / f"{nazov}.json"
    with cesta.open(encoding="utf-8") as f:
        return json.load(f)

TRIEDY = nacitaj("triedy")
NEPRIATELIA = nacitaj("nepriatelia")
PREDMETY = nacitaj("predmety")
