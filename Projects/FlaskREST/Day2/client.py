import requests
import json

BASE_URL = "http://127.0.0.1:5000/api"


def get_matches():
    response = requests.get(BASE_URL + "/matches")
    return response.content


def get_match():
    response = requests.get(BASE_URL + "/match/107")
    if response.status_code == 200:
        return response.content
    else:
        return None


def delete_match():
    response = requests.delete(BASE_URL + "/match/774")


def update_match():

    new_match = {
        "team1": "Russia",
        "team2": "Germany",
        "country": "Italy",
        "city": "Rome",
        "score1": 0,
        "score2": 0
    }

    response = requests.put(BASE_URL + "/match/400", data=json.dumps(new_match))


if __name__ == "__main__":
    pass
