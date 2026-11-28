import json
import sys
import urllib.request


def revenue_cents(payload):
    return sum(order.get("total_cents", 0) for order in payload["orders"])


def main(url):
    with urllib.request.urlopen(url) as resp:
        payload = json.load(resp)
    print(f"revenue: {revenue_cents(payload) / 100:.2f}")


if __name__ == "__main__":
    main(sys.argv[1])
