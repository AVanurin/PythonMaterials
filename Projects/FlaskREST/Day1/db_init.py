import sqlite3
import random


DB_PATH = 'db.sqlite3'


def init():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.executescript(open('shema.sql', 'r').read())
    connection.commit()
    connection.close()


countries = [
    "Russia",
    "England",
    "Italy",
    "Germany",
    "Spain",
    "Portugal",
    "Denmark",
    "Iceland",
    "Mexico"
]

cities = {
    "Russia": ["Moscow", "SP", "Krasnodar"],
    "England": ["London", "Manchester"],
    "Italy": ["Rome", "Milan"],
    "Germany": ["Berlin", "Frankfurt"],
    "Spain": ["Barcelona", "Madrid"],
    "Portugal": ["Lisbon"],
    "Denmark": ["Copenhagen"],
    "Iceland": ["Reykjavik"],
    "Mexico": ["Mexico"]
}


def next_match():
    if True:
        team1 = random.choice(countries)
        while True:
            team2 = random.choice(countries)
            if team1 != team2:
                break
        country = random.choice(countries)
        city = random.choice(cities[country])
        score1 = random.randint(0, 5)
        score2 = random.randint(0, 5)
        return team1, team2, country, city, score1, score2


def make_data():
    connection = sqlite3.connect(DB_PATH)
    c = connection.cursor()
    for i in range(1000):
        match = next_match()
        cmd = f"""
        INSERT INTO matches VALUES(
            {i},
            "{match[0]}",
            "{match[1]}",
            "{match[2]}",
            "{match[3]}",
            "{match[4]}",
            "{match[5]}"
        );
        """
        c.execute(cmd)
    connection.commit()
    connection.close()


def check_table():
    connection = sqlite3.connect(DB_PATH)
    c = connection.cursor()
    cmd = "SELECT * FROM matches"
    c.execute(cmd)
    r = c.fetchall()
    for i in r:
        print(i)

    connection.close()


if __name__ == "__main__":
    init()
    make_data()
    check_table()
