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
    """Function adds a new player to the team"""
    players.append(player)
    return players


def players_del(players: list[dict], name: str) -> list[dict]:
    """The function removes a player from the team by name"""
    for player in players:
        if player["name"] == name:
            players.remove(player)
            return players

    return players  # Если player не найден


def players_find(players: list[dict], field: str, value: Any) -> list[dict]:
    """The function finds a player in a team"""
    result = []
    for player in players:
        if player[field] == value:
            result.append(player)
            return result

    return result  # Если player не найден


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
        while True:
            name = input("What`s name: ").title().strip()
            if name.isalpha():
                break
        while True:
            age = input("What`s age: ").strip()
            if age.isdigit():
                break
        while True:
            number = input("What`s number: ").strip()
            if number.isdigit():
                break
        return {"name": name, "age": int(age), "number": int(number)}

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

        elif usr_inp == "add":
            players_add(my_team, add_dict())

        elif usr_inp == "del":
            players_del(my_team, add_name())

        elif usr_inp == "find":
            field, value = add_field_value()
            result = players_find(my_team, field, value)
            for player in result:
                print(
                    f'name: {player["name"]}, '
                    f'age: {player["age"]}, '
                    f'number: {player["number"]}'
                )

        elif usr_inp == "get":
            rslt = players_get_by_name(my_team, add_name())
            print(
                f'name: {rslt["name"]}, '  # type: ignore
                f'age: {rslt["age"]}, '  # type: ignore
                f'number: {rslt["number"]}'  # type: ignore
            )


if __name__ == "__main__":
    main()
