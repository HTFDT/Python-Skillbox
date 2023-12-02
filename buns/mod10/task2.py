import requests
import re


def main():
    data = requests.get("http://www.columbia.edu/~fdc/sample.html")
    if data.status_code != 200:
        raise ValueError()
    h3_regex = re.compile(r"<h3[\s=\"\w]*?>(.*?)</h3>")
    print(h3_regex.findall(data.text))


if __name__ == "__main__":
    main()
