import requests
import jwt
from datetime import datetime as date
from config import GHOST_API_KEY
import logging

# Split the key into ID and SECRET
id, secret = GHOST_API_KEY.split(':')

# Prepare header and payload



    
   
# Create the token (including decoding secret)

# Make an authenticated request to create a post
url = 'https://staggering.ghost.io/ghost/api/admin/posts/?source=html'



def publish_article(address, title, description, content,image_url):
    # print("content....===>"+f'{content}'+"--------enddddd")
    iat = int(date.now().timestamp())
    header = {'alg': 'HS256', 'typ': 'JWT', 'kid': id}
    payload = {
    'iat': iat,
    'exp': iat + 5 * 60,
    'aud': '/admin/'
    }
    token = jwt.encode(payload, bytes.fromhex(secret), algorithm='HS256', headers=header)
    headers = {'Authorization': 'Ghost {}'.format(token)}



    post_data = {
        "title": title,
        "html": f'{content}',
        "meta_title": title,
        "meta_description": description,
        "status": "published",
        "feature_image": image_url,
        "feature_image_alt": description[:125],
        "published_at": date.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        #"tags": [],
        #"authors": []
    }
    
    logging.info(f"Request body: {post_data}")  # Add this line to log the request body

    post = {
        "posts": [post_data]
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
        # print(response.json())  # Add this line to print the response JSON

