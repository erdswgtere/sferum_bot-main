from vk.types import UserCredentials 
import requests


def get_user_credentials(auth_cookie) -> UserCredentials:
    cookies = {
        "remixdsid": auth_cookie,
    }

    query = {
        "act": "web_token",
        "app_id": 8202606
    }
    
    req = requests.get("https://web.vk.me/", params=query,
                        cookies=cookies, allow_redirects=False)
    
    print(req.json())

    return UserCredentials(**req.json()[1])
