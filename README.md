# verbix-sdk

[![PyPI - Version](https://img.shields.io/pypi/v/verbix-sdk.svg)](https://pypi.org/project/verbix-sdk)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/verbix-sdk.svg)](https://pypi.org/project/verbix-sdk)

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install verbix-sdk
```

## Usage

This SDK offers two functions: `get_conjugation` and `is_known_verb`.

### `is_known_verb`:

Params:

- `lang`: the language of the verb. See [Supported Languages](https://api.verbix.com/conjugator/json#LanguageCodes).
- `verb`: the verb to conjugate
- `api_key`: your Verbix API key. You can use the one used by the website or reach out to [them](https://airtable.com/shrDJCA8nF96cmtSH) to get your own.

Output: returns `True` if the verb exists on Verbix for the given language and `False` otherwise.

Example:

```python
is_known_verb("por", "fazer")
```

returns True.

```python
is_known_verb("por", "hacer")
```

return False.

### `get_conjugation`

Params:

- `lang`: the language of the verb. See [Supported Languages](https://api.verbix.com/conjugator/json#LanguageCodes).
- `verb`: the verb to conjugate
- `api_key`: your Verbix API key. You can use the one used by the website or reach out to [them](https://airtable.com/shrDJCA8nF96cmtSH) to get your own.

Output: returns a complete JSON representation of the conjugated verb. Note that the output is simplified with respect to the original output of the Verbix API.

Example:

```python
get_conjugation("por", "fazer")
```

returns

```json
{
    "Indicative Present": {
        "eu": {
            "value": "faço",
            "type": "irregular"
        },
        "tu": {
            "value": "fazes",
            "type": "regular"
        },
        "ele": {
            "value": "faz",
            "type": "irregular"
        },
        "nós": {
            "value": "fazemos",
            "type": "regular"
        },
        "vós": {
            "value": "fazeis",
            "type": "regular"
        },
        "eles": {
            "value": "fazem",
            "type": "regular"
        }
    },
    "Subjunctive Present": {
        "eu": {
            "value": "faça",
            "type": "irregular"
        },
        "tu": {
            "value": "faças",
            "type": "irregular"
        },
        "ele": {
            "value": "faça",
            "type": "irregular"
        },
        "nós": {
            "value": "façamos",
            "type": "irregular"
        },
        "vós": {
            "value": "façais",
            "type": "irregular"
        },
        "eles": {
            "value": "façam",
            "type": "irregular"
        }
    },
    "Indicative Past": {
        "eu": {
            "value": "fazia",
            "type": "regular"
        },
        "tu": {
            "value": "fazias",
            "type": "regular"
        },
        "ele": {
            "value": "fazia",
            "type": "regular"
        },
        "nós": {
            "value": "fazíamos",
            "type": "regular"
        },
        "vós": {
            "value": "fazíeis",
            "type": "regular"
        },
        "eles": {
            "value": "faziam",
            "type": "regular"
        }
    },
    "Subjunctive Past": {
        "eu": {
            "value": "fizesse",
            "type": "irregular"
        },
        "tu": {
            "value": "fizesses",
            "type": "irregular"
        },
        "ele": {
            "value": "fizesse",
            "type": "irregular"
        },
        "nós": {
            "value": "fizéssemos",
            "type": "irregular"
        },
        "vós": {
            "value": "fizésseis",
            "type": "irregular"
        },
        "eles": {
            "value": "fizessem",
            "type": "irregular"
        }
    },
    "Indicative Preterite": {
        "eu": {
            "value": "fiz",
            "type": "irregular"
        },
        "tu": {
            "value": "fizeste",
            "type": "irregular"
        },
        "ele": {
            "value": "fez",
            "type": "irregular"
        },
        "nós": {
            "value": "fizemos",
            "type": "irregular"
        },
        "vós": {
            "value": "fizestes",
            "type": "irregular"
        },
        "eles": {
            "value": "fizeram",
            "type": "irregular"
        }
    },
    "Indicative Future": {
        "eu": {
            "value": "farei",
            "type": "irregular"
        },
        "tu": {
            "value": "farás",
            "type": "irregular"
        },
        "ele": {
            "value": "fará",
            "type": "irregular"
        },
        "nós": {
            "value": "faremos",
            "type": "irregular"
        },
        "vós": {
            "value": "fareis",
            "type": "irregular"
        },
        "eles": {
            "value": "farão",
            "type": "irregular"
        }
    },
    "Subjunctive Future": {
        "eu": {
            "value": "fizer",
            "type": "irregular"
        },
        "tu": {
            "value": "fizeres",
            "type": "irregular"
        },
        "ele": {
            "value": "fizer",
            "type": "irregular"
        },
        "nós": {
            "value": "fizermos",
            "type": "irregular"
        },
        "vós": {
            "value": "fizerdes",
            "type": "irregular"
        },
        "eles": {
            "value": "fizerem",
            "type": "irregular"
        }
    },
    "Conditional": {
        "eu": {
            "value": "faria",
            "type": "irregular"
        },
        "tu": {
            "value": "farias",
            "type": "irregular"
        },
        "ele": {
            "value": "faria",
            "type": "irregular"
        },
        "nós": {
            "value": "faríamos",
            "type": "irregular"
        },
        "vós": {
            "value": "faríeis",
            "type": "irregular"
        },
        "eles": {
            "value": "fariam",
            "type": "irregular"
        }
    },
    "Imperative": {
        "tu": {
            "value": "faze",
            "type": "irregular"
        },
        "ele": {
            "value": "faça",
            "type": "irregular"
        },
        "nós": {
            "value": "façamos",
            "type": "irregular"
        },
        "vós": {
            "value": "fazei",
            "type": "regular"
        },
        "eles": {
            "value": "façam",
            "type": "irregular"
        }
    },
    "Indicative Pluperfect": {
        "eu": {
            "value": "tinha feito",
            "type": "regular"
        },
        "tu": {
            "value": "tinhas feito",
            "type": "regular"
        },
        "ele": {
            "value": "tinha feito",
            "type": "regular"
        },
        "nós": {
            "value": "tínhamos feito",
            "type": "regular"
        },
        "vós": {
            "value": "tínheis feito",
            "type": "regular"
        },
        "eles": {
            "value": "tinham feito",
            "type": "regular"
        }
    },
    "Indicative Perfect": {
        "eu": {
            "value": "tenho feito",
            "type": "regular"
        },
        "tu": {
            "value": "tens feito",
            "type": "regular"
        },
        "ele": {
            "value": "tem feito",
            "type": "regular"
        },
        "nós": {
            "value": "temos feito",
            "type": "regular"
        },
        "vós": {
            "value": "tendes feito",
            "type": "regular"
        },
        "eles": {
            "value": "têm feito",
            "type": "regular"
        }
    },
    "Subjunctive Perfect": {
        "eu": {
            "value": "tenha feito",
            "type": "regular"
        },
        "tu": {
            "value": "tenhas feito",
            "type": "regular"
        },
        "ele": {
            "value": "tenha feito",
            "type": "regular"
        },
        "nós": {
            "value": "tenhamos feito",
            "type": "regular"
        },
        "vós": {
            "value": "tenhais feito",
            "type": "regular"
        },
        "eles": {
            "value": "tenham feito",
            "type": "regular"
        }
    },
    "Subjunctive Pluperfect": {
        "eu": {
            "value": "tivesse feito",
            "type": "regular"
        },
        "tu": {
            "value": "tivesses feito",
            "type": "regular"
        },
        "ele": {
            "value": "tivesse feito",
            "type": "regular"
        },
        "nós": {
            "value": "tivéssemos feito",
            "type": "regular"
        },
        "vós": {
            "value": "tivésseis feito",
            "type": "regular"
        },
        "eles": {
            "value": "tivessem feito",
            "type": "regular"
        }
    },
    "Indicative Future Perfect": {
        "eu": {
            "value": "terei feito",
            "type": "regular"
        },
        "tu": {
            "value": "terás feito",
            "type": "regular"
        },
        "ele": {
            "value": "terá feito",
            "type": "regular"
        },
        "nós": {
            "value": "teremos feito",
            "type": "regular"
        },
        "vós": {
            "value": "tereis feito",
            "type": "regular"
        },
        "eles": {
            "value": "terão feito",
            "type": "regular"
        }
    },
    "Subjunctive Future Perfect": {
        "eu": {
            "value": "tiver feito",
            "type": "regular"
        },
        "tu": {
            "value": "tiveres feito",
            "type": "regular"
        },
        "ele": {
            "value": "tiver feito",
            "type": "regular"
        },
        "nós": {
            "value": "tivermos feito",
            "type": "regular"
        },
        "vós": {
            "value": "tiverdes feito",
            "type": "regular"
        },
        "eles": {
            "value": "tiverem feito",
            "type": "regular"
        }
    },
    "Conditional Perfect": {
        "eu": {
            "value": "teria feito",
            "type": "regular"
        },
        "tu": {
            "value": "terias feito",
            "type": "regular"
        },
        "ele": {
            "value": "teria feito",
            "type": "regular"
        },
        "nós": {
            "value": "teríamos feito",
            "type": "regular"
        },
        "vós": {
            "value": "teríeis feito",
            "type": "regular"
        },
        "eles": {
            "value": "teriam feito",
            "type": "regular"
        }
    },
    "Personal Infinitive": {
        "0": {
            "value": "fazer",
            "type": "regular"
        },
        "1": {
            "value": "fazeres",
            "type": "regular"
        },
        "2": {
            "value": "fazer",
            "type": "regular"
        },
        "3": {
            "value": "fazermos",
            "type": "regular"
        },
        "4": {
            "value": "fazerdes",
            "type": "regular"
        },
        "5": {
            "value": "fazerem",
            "type": "regular"
        }
    },
    "Infinitive": {
        "0": {
            "value": "fazer",
            "type": "regular"
        }
    },
    "Gerund": {
        "0": {
            "value": "fazendo",
            "type": "regular"
        }
    },
    "Past Participle": {
        "0": {
            "value": "feito",
            "type": "irregular"
        }
    },
    "Personal Infinitive Perfect": {
        "0": {
            "value": "ter feito",
            "type": "regular"
        },
        "1": {
            "value": "teres feito",
            "type": "regular"
        },
        "2": {
            "value": "ter feito",
            "type": "regular"
        },
        "3": {
            "value": "termos feito",
            "type": "regular"
        },
        "4": {
            "value": "terdes feito",
            "type": "regular"
        },
        "5": {
            "value": "terem feito",
            "type": "regular"
        }
    }
}
```

## License

`verbix-sdk` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
