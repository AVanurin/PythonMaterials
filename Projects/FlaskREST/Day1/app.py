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


@app.route("/api/match/<int:Id>")
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


if __name__ == "__main__":
    app.run()
