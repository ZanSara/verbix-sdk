import requests
from verbix_sdk.constants import API_KEY


V2_BASE_URL = "https://api.verbix.com/conjugator/json/{}/v2/{}/{}"
V2_USES = {
    0: "regular",
    1: "regular with ortographical changes",
    2: "irregular",
    3: "dialectal/archaic",
    4: "not in use, hypothetical",
}


def is_known_verb(lang, verb, api_key=API_KEY):
    url = V2_BASE_URL.format(api_key, lang, verb)
    response = requests.get(url, headers={"User-Agent": "Chrome/83.0.4103.116"})
    response.raise_for_status()
    results = response.json()
    return results.get("exists")


def get_conjugation(lang, verb, api_key=API_KEY):
    response = requests.get(V2_BASE_URL.format(api_key, lang, verb), headers={"User-Agent": "Chrome/83.0.4103.116"})
    response.raise_for_status()
    results = response.json()
    if not results.get("exists"):
        raise ValueError("Verb does not exist!")
    
    conjugation = {}
    for tense_data in results["tenses"].values():
        if "name" in tense_data:
            conjugation[tense_data["name"]] = {}
            for idx, person in enumerate(tense_data["forms"]):
                if not person["pronoun"]:
                    person["pronoun"] = idx
                conjugation[tense_data["name"]][person["pronoun"]] = {"value": person["form"], "type": V2_USES[person["use"]]}

    return conjugation
