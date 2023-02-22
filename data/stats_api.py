import json
import main

stats_file = str(main.config.get('statsDataPath'))


def set_level(level: int):
    with open(stats_file, "r") as file:
        data = json.load(file)
    data["level"] = level
    with open(stats_file, "w") as file:
        json.dump(data, file, indent=4, encodings="utf-8")


def get_level():
    with open(stats_file, "r") as file:
        data = json.load(file)
    return data["level"]


def set_played_games(value: int):
    with open(stats_file, "r") as file:
        data = json.load(file)
    data["played_games"] = value
    with open(stats_file, "w") as file:
        json.dump(data, file, indent=4, encodings="utf-8")


def get_played_games():
    with open(stats_file, "r") as file:
        data = json.load(file)
    return data["played_games"]


def set_shots(value: int):
    with open(stats_file, "r") as file:
        data = json.load(file)
    data["shots"] = value
    with open(stats_file, "w") as file:
        json.dump(data, file, indent=4, encodings="utf-8")


def get_shots():
    with open(stats_file, "r") as file:
        data = json.load(file)
    return data["shots"]


def get_key(key: str):
    with open(stats_file, "r") as file:
        data = json.load(file)
    return data[key]
