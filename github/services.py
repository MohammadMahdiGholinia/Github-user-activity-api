import requests

def get_github_user_events(username):
    url = f"https://api.github.com/users/{username}/events"

    try :
        response = requests.get(url, timeout = 10)

    except requests.Timeout:
        return {"error": "Request timed out. Please try again later."}
    
    except requests.RequestException:
        return {"Could not connect to GitHub API"}
    
    if response.status_code == 404:
        raise LookupError("Github user not found")
    
    if response.status_code in (403, 429):
        raise PermissionError("GitHub API request limit or access restriction")
    
    if not response.ok:
        raise RuntimeError("GitHub API returned an error")
    
    return response.json()





    # response = requests.get(url)

    # return response.json()




