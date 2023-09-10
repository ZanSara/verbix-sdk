import json
import requests
from bs4 import BeautifulSoup

V1_LANG_CODES={
    "spa": "Spanish",
    "por": "Portuguese",
    "fra": "French",
    "ita": "Italian",
    "ron": "Romanian",
    "glg": "Galician",
    "cat": "Catalan",
    "oci": "Occitan",
    "lat": "Latin",
    "fin": "Finnish",
    "got": "Gothic",
    "eng": "English",
    "swe": "Swedish",
    "deu": "German",
    "ang": "Old English",
    "nld": "Dutch",
    "nob": "Norwegian (bokmål)",
    "dan": "Danish",
    "isl": "Icelandic",
    "tur": "Turkish",
    "pdt": "Plautdietsch",
    "jpn": "Japanese",
    "nno": "Norwegian (Nynorsk)",
    "ltz": "Luxembourgish",
    "kal": "Greenlandic",
    "ell": "Greek",
    "hun": "Hungarian",
    "rus": "Russian",
    "ukr": "Ukrainian",
    "lit": "Lithuanian",
    "tib": "Tibetan",
    "bul": "Bulgarian",
    "ind": "Indonesian",
    "dlm": "Dalmatian",
    "epo": "Esperanto",
    "est": "Estonian",
    "kor": "Korean",
    "mkd": "Macedonian",
    "tha": "Thai",
}
V1_LANG_CODES = {
    "spa": "3/101",
    "por": "3/102",
    "fra": "3/103",
    "ita": "4/104",
    "eng": "20/120",
    "hun": "121/221",
    "fin": "10/110",
}
V1_BASE_URL = "https://api.verbix.com/conjugator/iv1/6153a464-b4f0-11ed-9ece-ee3761609078/1/{}/{}"

V2_BASE_URL = "https://api.verbix.com/conjugator/json/6153a464-b4f0-11ed-9ece-ee3761609078/v2/{}/{}"
V2_USES = {
    0: "regular",
    1: "regular with ortographical changes",
    2: "irregular",
    3: "dialectal/archaic",
    4: "not in use, hypothetical",
}

def get_conjugation(lang, verb):
    response = requests.get(BASE_URL.format(lang, verb), headers={"User-Agent": "Chrome/83.0.4103.116"})
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


######################


def parse_tense(columns_sub):
    sub_block = {}
    table = columns_sub.find(class_="verbtense")
    if table:
        for idx, row in enumerate(table.find_all("tr")):
            cells = row.find_all("td")
            if len(cells) == 2:
                sub_block[cells[0].text] = {"value": cells[1].text, "type": cells[1].find("span").attrs.get("class")[0]}
            else:
                sub_block[idx] = {"value": cells[0].text, "type": cells[0].find("span").attrs.get("class")[0]}
    return sub_block


def does_it_exist(lang, verb):
    url = V2_BASE_URL.format(lang, verb)
    response = requests.get(url, headers={"User-Agent": "Chrome/83.0.4103.116"})
    response.raise_for_status()
    results = response.json()
    return results.get("exists")


def get_conjugation(lang, verb):
    if not does_it_exist(lang, verb):
        raise ValueError(f"Verb {verb} does not exist in {lang}!")

    # download the webpage from the URL with a chrome user agent
    page = requests.get(V1_BASE_URL.format(V1_LANG_CODES[lang], verb), headers={"User-Agent": "Chrome/83.0.4103.116"})
    print(page.url)
    
    page.raise_for_status()
    data = page.json()
    table = data['p1']["html"]

    # parse the html using beautiful soup and store in variable 'soup'
    soup = BeautifulSoup(table, 'html.parser')

    # find the element with class "conjugation"
    columns = soup.find(class_="columns-main")

    blocks = {}
    for columns_main in columns.find_all("div"):
        if title := columns_main.find("h3"):
            block = {}

            if title.text == "Nominal Forms":
                for child in columns_main.find("p"):
                    if child.name == "b":
                        key = child.text
                    if child.name == "span":
                        block[key] = {"type": child.attrs.get("class")[0], "value": child.text}

            elif columns_div := columns_main.find(class_="columns-sub"):
                block = {}
                for columns_sub in columns_div.find_all("div"):
                    sub_title = columns_sub.find("h4")
                    sub_block = parse_tense(columns_sub)
                    block[sub_title.text] = sub_block
            else:
                block = parse_tense(columns_main)
                
            blocks[title.text] = block

    blocks = {key: value for key, value in blocks.items() if value}
    return blocks



if __name__ == "__main__":
    conj = get_conjugation("por", "fazer")
    print(json.dumps(conj, indent=4, ensure_ascii=False))






