import requests
import jwt
from datetime import datetime as date
from config import GHOST_API_KEY
import logging

# Split the key into ID and SECRET
id, secret = GHOST_API_KEY.split(':')

# Prepare header and payload
iat = int(date.now().timestamp())

header = {'alg': 'HS256', 'typ': 'JWT', 'kid': id}
payload = {
    'iat': iat,
    'exp': iat + 5 * 60,
    'aud': '/admin/'
}

# Create the token (including decoding secret)
token = jwt.encode(payload, bytes.fromhex(secret), algorithm='HS256', headers=header)

# Make an authenticated request to create a post
url = 'https://staggering.ghost.io/ghost/api/admin/posts/'
headers = {'Authorization': 'Ghost {}'.format(token)}


def publish_article(address, title, description, content):
    post = {
        "title": title,
        "html": content,
        "meta_title": title,
        "meta_description": description,
        "status": "published",
        "published_at": date.now().isoformat(),
        "tags": [],
        "authors": []
    }
    try:
        response = requests.post(
            url,
            json=post,
            headers=headers
        )
        response.raise_for_status()


        print("Post published successfully")
    except requests.exceptions.RequestException as e:
        print(f"Error publishing post: {e}")

