import json
from verbix_sdk import get_conjugation


if __name__ == "__main__":
    print(json.dumps(get_conjugation("por", "fazer"), indent=4, ensure_ascii=False))
    