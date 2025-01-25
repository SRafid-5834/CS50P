# Bitcoin Price Index

import requests
import sys


def main():
    try:
        out = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        amount = out.get("bpi").get("USD").get("rate_float")
        print(f"${amount * get_multiplier():,.4f}")
    except (requests.RequestException, requests.ConnectionError, requests.HTTPError,
            requests.URLRequired, requests.ConnectTimeout, requests.ReadTimeout, requests.Timeout):
        pass


def get_multiplier():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) == 2:
        if not sys.argv[1].replace(".", "").isnumeric():
            sys.exit("Command-line argument is not a number")
        else:
            return float(sys.argv[1])


if __name__ == '__main__':
    main()
