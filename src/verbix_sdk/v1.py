import requests
from bs4 import BeautifulSoup

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


def get_conjugation(lang, verb):
    page = requests.get(V1_BASE_URL.format(V1_LANG_CODES[lang], verb), headers={"User-Agent": "Chrome/83.0.4103.116"})
    page.raise_for_status()
    data = page.json()
    table = data['p1']["html"]

    soup = BeautifulSoup(table, 'html.parser')
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

