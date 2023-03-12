import json
import main

stats_file = str(main.config.get('stats_data_path'))


def add_level():
    with open(stats_file, "r") as file:
        data = json.load(file)
    data["level"] = (data["level"] + 1)
    with open(stats_file, "w") as file:
        json.dump(data, file, indent=4, encodings="utf-8")


def get_level():
    with open(stats_file, "r") as file:
        data = json.load(file)
    return data["level"]


def add_played_game():
    with open(stats_file, "r") as file:
        data = json.load(file)
    data["played_games"] = (data["played_games"] + 1)
    with open(stats_file, "w") as file:
        json.dump(data, file, indent=4, encodings="utf-8")


def get_played_games():
    with open(stats_file, "r") as file:
        data = json.load(file)
    return data["played_games"]


def add_win():
    with open(stats_file, "r") as file:
        data = json.load(file)
    data["won_games"] = (data["won_games"] + 1)
    with open(stats_file, "w") as file:
        json.dump(data, file, indent=4, encodings="utf-8")


def get_wins():
    with open(stats_file, "r") as file:
        data = json.load(file)
    return data["won_games"]


def add_lose():
    with open(stats_file, "r") as file:
        data = json.load(file)
    data["lost_games"] = (data["lost_games"] + 1)
    with open(stats_file, "w") as file:
        json.dump(data, file, indent=4, encodings="utf-8")


def get_loses():
    with open(stats_file, "r") as file:
        data = json.load(file)
    return data["lost_games"]


def get_key(key: str):
    with open(stats_file, "r") as file:
        data = json.load(file)
    return data[key]
