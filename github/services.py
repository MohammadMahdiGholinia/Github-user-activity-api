import requests

def get_github_user_events(username):
    url      = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)

    return response.json()




