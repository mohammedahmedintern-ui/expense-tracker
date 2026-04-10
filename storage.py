#storing data

import json

def load_expenses():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except:
        return []


def save_expenses(expenses):
    with open("data.json", "w") as f:
        json.dump(expenses, f)