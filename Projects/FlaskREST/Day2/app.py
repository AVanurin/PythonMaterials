from flask import Flask
from flask import request
import sqlite3
import json


PATH_DB = "db.sqlite3"

app = Flask(__name__)


@app.route("/api/matches", methods=["GET"])
def all_matches():

    country_filter = request.args.get('country')

    connection = sqlite3.connect(PATH_DB)
    c = connection.cursor()

    if not country_filter:

        cmd = """
        SELECT id, team1, team2, score1, score2 FROM matches;
        """

    else:

        cmd = f"""
        SELECT id, team1, team2, score1, score2 FROM matches WHERE team1="{country_filter}" OR team2="{country_filter}";
        """

    c.execute(cmd)
    mathces = c.fetchall()

    return json.dumps({"matches": mathces})


@app.route("/api/match/<int:Id>", methods=["GET"])
def match_with(Id):
    connection = sqlite3.connect(PATH_DB)

    c = connection.cursor()

    cmd = f"""
    SELECT * FROM matches WHERE id={Id};
    """

    c.execute(cmd)
    data = c.fetchone()

    d = {
        "team_1": data[1],
        "team_2": data[2],
        "place": {
            "country": data[3],
            "city": data[4]
        },
        "score": f"{data[5]}-{data[6]}",
    }

    return json.dumps(d)


@app.route("/api/match/<int:Id>", methods=["DELETE"])
def delete_match(Id):
    connection = sqlite3.connect(PATH_DB)

    c = connection.cursor()

    cmd = f"""
    DELETE FROM matches WHERE id={Id};
    """

    c.execute(cmd)
    connection.commit()

    connection.close()

    return json.dumps({})


@app.route("/api/match/<int:Id>", methods=["PUT"])
def update_match(Id):
    data = request.data.decode("utf-8")
    data_json = json.loads(data)

    team1 = data_json["team1"]
    team2 = data_json["team2"]
    country = data_json["country"]
    city = data_json["city"]
    score1 = data_json["score1"]
    score2 = data_json["score2"]

    connection = sqlite3.connect(PATH_DB)
    c = connection.cursor()

    cmd = f"""
    UPDATE matches SET 
    team1 = "{team1}",
    team2 = "{team2}",
    country = "{country}",
    city = "{city}",
    score1 = {score1},
    score2 = {score2} WHERE Id = {Id};
    """

    c.execute(cmd)
    connection.commit()
    connection.close()

    return "{}"


if __name__ == "__main__":
    app.run()
