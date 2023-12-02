import requests
import json


def get_data(url: str):
    res = requests.get(url)
    if res.status_code == 200:
        return json.loads(res.text)
    raise ValueError(f"wrong url: {url}")


def get_pilot_info(url: str):
    keys = {"name", "homeworld", "height", "mass"}
    pilot_info = get_data(url)
    filtered_info = {k: pilot_info[k] for k in keys}
    homeworld_info = get_data(filtered_info["homeworld"])
    homeworld = homeworld_info["name"]
    filtered_info["homeworld_url"] = filtered_info["homeworld"]
    filtered_info["homeworld"] = homeworld
    return filtered_info


def main():
    data = get_data("https://swapi.dev/api/starships/?search=Millennium%20Falcon")
    ship_info: dict = data["results"][0]
    keys = {"name", "starship_class", "max_atmosphering_speed", "pilots"}
    filtered_info = {k: ship_info[k] for k in keys}
    filtered_info["pilots"] = [get_pilot_info(pilot) for pilot in filtered_info["pilots"]]
    print(filtered_info)
    with open("Millenium Falcon.json", "w") as f:
        json.dump(filtered_info, f, indent=4)


if __name__ == "__main__":
    main()




