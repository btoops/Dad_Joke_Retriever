import requests
import pyfiglet
import termcolor
import colorama
from random import choice

colorama.init()
print(termcolor.colored(pyfiglet.figlet_format("Dad Joke Hub"), color="cyan"))

user_input = input("What would you like to search for? ")
if not user_input == "quit":
    url = "https://icanhazdadjoke.com/search"
    res = requests.get(
        url,
        headers={"Accept": "application/json"},
        params={"term": user_input}
    ).json()

    num_jokes = res["total_jokes"]
    results = res["results"]
    if num_jokes > 1:
        print(f"I found {num_jokes} jokes about {user_input}. Here's one:")
        print(choice(results)['joke'])
    elif num_jokes == 1:
        print(f"I found {num_jokes} jokes about {user_input}")
        print(results[0]['joke'])
    else:
        print(f"Could not find a joke for {user_input}")
