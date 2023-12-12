import requests


URL = "https://hotell.difi.no/api/json/mattilsynet/smilefjes/tilsyn?"

# parameters:
# tilsynsobjektid; -Nøkkel for å identifisere tilsynsobjektet
#! navn; -Navnet på tilsynsobjektet

#! adrlinje1; -Adresse
#! poststed; -Poststed


#! dato; -Dato tilsynet er utført (ddmmyyyy)
#! karakter; -Smilefjeskarakter for hele tilsynet

# tema_karakter1; -Temanavn:karakter (Ledelse og rutiner)
# tema_karakter2; -Temanavn:karakter (Lokaler og utstyr)
# tema_karakter3; -Temanavn:karakter (Mattilberedning og håndtering)
# tema_karakter4; -Temanavn:karakter (Sporbarhet og Merking)

parameters = {
    # "navn": "",
    # "adrlinje1": "",
    "poststed": "HAMAR",
    "dato": 21012016,
    "tema_karakter1": 0,
    "tema_karakter2": 0,
    "tema_karakter3": 0,
    "tema_karakter4": 0,
}

page = requests.get(URL, params=parameters)
print(page.json())
