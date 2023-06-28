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

html_content1 = """ <section style="padding-top: 48px; padding-bottom: 48px">
      <div
        style="
          max-width: 900px;
          margin-left: auto;
          margin-right: auto;
          padding-left: 12px;
          padding-right: 12px;
        "
      >
        <div
          style="
            display: flex;
            flex-wrap: nowrap;
            margin-left: -12px;
            margin-right: -12px;
            flex-direction: row;
            align-items: center;
            box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.15);
            border-radius: 10px;
            margin: 0px;
          "
        >
          <div
            style="
              width: 66.66%;
              padding: 48px;
              background: linear-gradient(264.53deg, #2b531e 0%, #272727 100%);
              border-radius: 10px 0px 0px 10px;
            "
            class="col-md-8 p-4 p-lg-5"
          >
            <div
              style="display: flex; align-items: center"
              class="flex-column flex-sm-row"
            >
              <div>
                <div
                  style="
                    border: 3px solid #b2ef56;
                    border-radius: 50%;
                    padding: 5px 5px 2px 5px;
                    display: inline-block;
                  "
                >
                  <img
                    style="width: 135px; height: 135px; border-radius: 50%"
                    src="https://cdn.sportsbettingdime.com/app/uploads/media/3/icon-draftkings.png"
                    alt="..."
                  />
                </div>
              </div>
              <div style="padding-left: 16px" class="ps-sm-3 text-center">
                <h4
                  style="
                    font-size: 40px;
                    font-weight: 900;
                    color: white;
                    font-family: Lato;
                    margin-bottom: 0px;
                    margin: 0px;
                  "
                  class="pt-4 pt-sm-0"
                >
                  DRAFTKINGS SPORTSBOOK
                </h4>
                <p
                  style="
                    font-size: 19px;
                    font-weight: 900;
                    font-family: Lato;
                    margin: 16px 0px 24px 24px;
                    color: white;
                  "
                >
                  Sign Up Today & Receive Up to <br />
                  $1,050 in Bonuses!
                </p>
                <button
                  style="
                    border: none;
                    padding: 8px 12px;
                    border-radius: 4px;
                    background-color: white;
                    color: black;
                    font-weight: 900;
                    font-size: 14px;
                    font-family: Lato;
                    cursor: pointer;
                  "
                >
                  LOCK IN PROMO
                </button>
              </div>
            </div>
          </div>
          <div
            style="width: 33.33%; text-align: center"
            class="col-md-4 py-3 py-md-0"
          >
            <p
              style="
                margin-top: 0px;
                margin-bottom: 0px;
                padding-bottom: 24px;
                font-size: 20px;
                font-weight: 900;
                font-family: Lato;
                color: black;
              "
            >
              SIGNUP PROMO
            </p>
            <h5
              style="
                font-size: 40px;
                font-weight: 900;
                margin: 0px;
                font-family: Lato;
              "
            >
              SIGN UP <br />
              <span style="white-space: nowrap"> & GET $1,050</span>
            </h5>
            <p
              style="
                color: black;
                font-size: 14px;
                font-family: Lato;
                font-weight: 500;
                white-space: nowrap;
              "
            >
              BONUS BETS + DEPOSIT BONUS
            </p>
            <button
              style="
                cursor: pointer;
                border-radius: 4px;
                font-weight: 900;
                font-family: Lato;
                font-size: 14px;
                background-image: linear-gradient(to bottom, #16ba5e, #0a9547);
                box-shadow: 0 3px 8px 0 rgb(0 0 0 / 20%);
                color: #ffffff;
                padding: 10px 50px;
                border-radius: 3px;
                border: none;
              "
              class="get_btn border-0 rounded fw-bold font_lato font_xsm"
            >
              GET PROMO
            </button>
          </div>
        </div>
      </div>
    </section>
  </body>
</html>"""



html_content = """<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Lato:wght@100;300;400;700;900&display=swap"
      rel="stylesheet"
    />
    <!-- Bootstrap CSS -->

    <title>Documnet</title>
  </head>
  <body>"""
    
   
# Create the token (including decoding secret)
token = jwt.encode(payload, bytes.fromhex(secret), algorithm='HS256', headers=header)

# Make an authenticated request to create a post
url = 'https://staggering.ghost.io/ghost/api/admin/posts/?source=html'
headers = {'Authorization': 'Ghost {}'.format(token)}


def publish_article(address, title, description, content,image_url):
    # print("content....===>"+f'{content}'+"--------enddddd")
    
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

