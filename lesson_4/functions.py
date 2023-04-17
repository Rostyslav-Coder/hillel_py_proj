"""This is module of HOME WORK 4 by Rostyslav P.
"""
from typing import Any


def players_repr(players: list[dict]) -> None:
    """The function displays information about players"""
    print(">>> TEAM <<<")
    for player in players:
        print(
            f'name: {player["name"]}, '
            f'age: {player["age"]}, '
            f'number: {player["number"]}'
        )


def players_add(players: list[dict], player: dict) -> list[dict]:
    """Function adds a new player to the team by name"""
    return players.append(player)


def players_del(players: list[dict], name: str) -> list[dict]:
    """The function removes a player from the team"""
    for player in players:
        if player["name"] == name:
            return players.remove(player)

    return players


def players_find(players: list[dict], field: str, value: Any) -> list[dict]:
    """The function finds a player in a team"""
    for player in players:
        if player[field] == value:
            return player

    return []


def players_get_by_name(players: list[dict], name: str) -> dict | None:
    """The function finds a player in a team by name"""
    for player in players:
        if player["name"] == name:
            return player

    return None


def main():
    """This function gives the user control over this module"""
    my_team = [
        {"name": "John", "age": 20, "number": 1},
        {"name": "Paul", "age": 18, "number": 2},
        {"name": "George", "age": 21, "number": 3},
        {"name": "Ringo", "age": 20, "number": 4},
    ]

    optns = ["repr", "add", "del", "find", "get"]

    def add_dict():
        name = input("What`s player name: ").title().strip()
        age = int(input("What`s player age: "))
        number = int(input("What`s player number: "))
        return {"name": name, "age": age, "number": number}

    def add_name():
        name = input("What`s name: ").title().strip()
        return name

    def add_field_value():
        field = input("What`s field: ").lower().strip()
        value = input("What`s value: ")
        if field == "name":
            value = value.title().strip()
        if field in ("age", "number"):
            value = int(value)
        return field, value

    while True:
        if not (usr_inp := input(f"Whot`s choice {optns}: ").lower().strip()):
            break

        if usr_inp == "repr":
            players_repr(my_team)

        if usr_inp == "add":
            players_add(my_team, add_dict())

        if usr_inp == "del":
            players_del(my_team, add_name())

        if usr_inp == "find":
            field, value = add_field_value()
            result = players_find(my_team, field, value)
            print(
                f'name: {result["name"]}, '
                f'age: {result["age"]}, '
                f'number: {result["number"]}'
            )

        if usr_inp == "get":
            rslt = players_get_by_name(my_team, add_name())
            print(
                f'name: {rslt["name"]}, '
                f'age: {rslt["age"]}, '
                f'number: {rslt["number"]}'
            )


if __name__ == "__main__":
    main()
