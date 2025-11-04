import requests
from kestra import Kestra


def get_quote_of_the_day():
    try:
        response = requests.get(
            "https://www.forbes.com/forbesapi/thought/uri.json?enrich=true&query=1"
        )  # Example API
        response.raise_for_status()  # Raise an exception for bad status codes
        quote_data = response.json()
        thought = quote_data["thought"]

        return f"\"{thought['quote'].strip()}\" - {thought['thoughtAuthor']['name']}"
    except requests.exceptions.RequestException as e:
        return f"Error fetching quote: {e}"


if __name__ == "__main__":
    print("Quote of the Day:")
    quote = get_quote_of_the_day()
    Kestra.output({"quote": quote})
    print(quote)
