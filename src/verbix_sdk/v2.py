import requests


V2_BASE_URL = "https://api.verbix.com/conjugator/json/6153a464-b4f0-11ed-9ece-ee3761609078/v2/{}/{}"
V2_USES = {
    0: "regular",
    1: "regular with ortographical changes",
    2: "irregular",
    3: "dialectal/archaic",
    4: "not in use, hypothetical",
}


def does_it_exist(lang, verb):
    url = V2_BASE_URL.format(lang, verb)
    response = requests.get(url, headers={"User-Agent": "Chrome/83.0.4103.116"})
    response.raise_for_status()
    results = response.json()
    return results.get("exists")


def get_conjugation(lang, verb):
    response = requests.get(V2_BASE_URL.format(lang, verb), headers={"User-Agent": "Chrome/83.0.4103.116"})
    response.raise_for_status()
    results = response.json()
    if not results.get("exists"):
        raise ValueError("Verb does not exist!")

    conjugation = {}
    for tense_data in results["tenses"].values():
        if "name" in tense_data:

            mode, tense = "", ""
            names = tense_data["name"].split(" ", maxsplit=2)
            if len(names) == 1:
                mode = names[0]
            elif len(names) == 2:
                mode, tense = names

            if mode not in conjugation:
                conjugation[mode] = {}

            conjugation[mode][tense] = {}
            for person in tense_data["forms"]:
                conjugation[mode][tense][person["pronoun"]] = {"value": person["form"], "type": V2_USES[person["use"]]}

    return conjugation
