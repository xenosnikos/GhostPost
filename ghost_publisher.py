import requests
import jwt
from datetime import datetime as date
from config import GHOST_API_KEY
import logging
import json


# Split the key into ID and SECRET
id, secret = GHOST_API_KEY.split(':')

# Prepare header and payload
iat = int(date.now().timestamp())

header = {'alg': 'HS256', 'typ': 'JWT', 'kid': id}
payload = {
    'iat': iat,
    'exp': iat + 30 * 60,
    'aud': '/admin/'
}


    
   
# Create the token (including decoding secret)




def publish_article(address, title, description, content,image_url):
    
    token = jwt.encode(payload, bytes.fromhex(secret), algorithm='HS256', headers=header)

    # Make an authenticated request to create a post
    url = 'https://staggering.ghost.io/ghost/api/admin/posts?formats=mobiledoc%2Clexical'
    headers = {'Authorization': 'Ghost {}'.format(token)}

    html = x = content.replace("\n", "\\n")



    post_data = {
        "title": title,
        "mobiledoc": "{\"version\":\"0.3.1\",\"atoms\":[],\"cards\":[[\"html\",{\"html\":\"<!DOCTYPE html>\\n<html lang=\\\"en\\\">\\n  <head>\\n    <!-- Required meta tags -->\\n    <meta charset=\\\"utf-8\\\" />\\n    <meta name=\\\"viewport\\\" content=\\\"width=device-width, initial-scale=1\\\" />\\n    <link rel=\\\"preconnect\\\" href=\\\"https://fonts.googleapis.com\\\" />\\n    <link rel=\\\"preconnect\\\" href=\\\"https://fonts.gstatic.com\\\" crossorigin />\\n    <link\\n      href=\\\"https://fonts.googleapis.com/css2?family=Lato:wght@100;300;400;700;900&display=swap\\\"\\n      rel=\\\"stylesheet\\\"\\n    />\\n    <link rel=\\\"stylesheet\\\" href=\\\"https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap-grid.min.css\\\" integrity=\\\"sha512-EAgFb1TGFSRh1CCsDotrqJMqB2D+FLCOXAJTE16Ajphi73gQmfJS/LNl6AsjDqDht6Ls7Qr1KWsrJxyttEkxIA==\\\" crossorigin=\\\"anonymous\\\" referrerpolicy=\\\"no-referrer\\\" />\\n    \\n    <!-- Bootstrap CSS -->\\n\\n    <title>Documnet</title>\\n      <style>\\n          \\n.post-content {\\n    font-size: 2rem;\\n    max-width: 100%;\\n    margin: 0 auto 14vh;\\n}\\n          </style>\\n  </head>\\n  <body>\\n    <div class=\\\"row\\\">\\n      <div class=\\\"col-sm-3\\\" >\\n        <img style=\\\"\\n        height:440px;\\n        width: 280px;\\n        padding:15px;\\n        \\\"  src=\\\"https://i.ibb.co/KKBQdkQ/poster-design-template-d882fb9ef961fa63654e94bc76600f8b-screen.jpg\\\" alt=\\\"\\\">\\n     </div>\\n         <div class=\\\"col-sm-6\\\">\\n          <div style=\\\"\\n          max-width: 900px;\\n          margin-left: auto;\\n          margin-right: auto;\\n          padding-left: 12px;\\n          padding-right: 12px; \\n         \\\">\\n     "+html+"      </div>\\n    <section style=\\\"padding-top: 48px; padding-bottom: 48px\\\">\\n      <div\\n        style=\\\"\\n          max-width: 900px;\\n          margin-left: auto;\\n          margin-right: auto;\\n          padding-left: 12px;\\n          padding-right: 12px;\\n        \\n        \\\"\\n      >\\n        <div\\n          style=\\\"\\n            display: flex;\\n            flex-wrap: nowrap;\\n            margin-left: -12px;\\n            margin-right: -12px;\\n            flex-direction: row;\\n            align-items: center;\\n            box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.15);\\n            border-radius: 10px;\\n            margin: 0px;\\n            background-color:white;\\n          \\\"\\n        >\\n          <div\\n            style=\\\"\\n              width: 60.66%;\\n              padding: 48px;\\n              background: linear-gradient(264.53deg, #2b531e 0%, #272727 100%);\\n              border-radius: 10px 0px 0px 10px;\\n            \\\"\\n            class=\\\"col-md-8 p-4 p-lg-5\\\"\\n          >\\n            <div\\n              style=\\\"display: flex; align-items: center\\\"\\n              class=\\\"flex-column flex-sm-row\\\"\\n            >\\n              <div>\\n                <div\\n                  style=\\\"\\n                    border: 3px solid #b2ef56;\\n                    border-radius: 50%;\\n                    padding: 5px 5px 2px 5px;\\n                    display: inline-block;\\n                  \\\"\\n                >\\n                  <img\\n                    style=\\\"width: 135px; height: 135px; border-radius: 50%\\\"\\n                    src=\\\"https://cdn.sportsbettingdime.com/app/uploads/media/3/icon-draftkings.png\\\"\\n                    alt=\\\"...\\\"\\n                  />\\n                </div>\\n              </div>\\n              <div style=\\\"padding-left: 16px\\\" class=\\\"ps-sm-3 text-center\\\">\\n                <h4\\n                  style=\\\"\\n                    font-size: 32px;\\n                    font-weight: 900;\\n                    color: white;\\n                    font-family: Lato;\\n                    margin-bottom: 0px;\\n                    margin: 0px;\\n                  \\\"\\n                  class=\\\"pt-4 pt-sm-0\\\"\\n                >\\n                  DRAFTKINGS SPORTSBOOK\\n                </h4>\\n                <p\\n                  style=\\\"\\n                    font-size: 19px;\\n                    font-weight: 900;\\n                    font-family: Lato;\\n                    margin: 16px 0px 24px 24px;\\n                    color: white;\\n                  \\\"\\n                >\\n                  Sign Up Today & Receive Up to <br />\\n                  $1,050 in Bonuses!\\n                </p>\\n                <button\\n                  style=\\\"\\n                    border: none;\\n                    padding: 8px 12px;\\n                    border-radius: 4px;\\n                    background-color: white;\\n                    color: black;\\n                    font-weight: 900;\\n                    font-size: 14px;\\n                    font-family: Lato;\\n                    cursor: pointer;\\n                  \\\"\\n                >\\n                  LOCK IN PROMO\\n                </button>\\n              </div>\\n            </div>\\n          </div>\\n          <div\\n            style=\\\"width: 21.33%; text-align: center\\\"\\n            class=\\\"col-md-4 py-3 py-md-0\\\"\\n          >\\n            <p\\n              style=\\\"\\n                margin-top: 0px;\\n                margin-bottom: 0px;\\n                padding-bottom: 24px;\\n                font-size: 20px;\\n                font-weight: 900;\\n                font-family: Lato;\\n                color: black;\\n                margin-left: 10px;\\n               \\\"\\n            >\\n              SIGNUP PROMO\\n            </p>\\n            <h5\\n              style=\\\"\\n                font-size: 30px;\\n                font-weight: 900;\\n                margin: 0px;\\n                font-family: Lato;\\n                color: black;\\n              \\\"\\n            >\\n              SIGN UP <br />\\n              <span style=\\\"white-space: nowrap\\\"> & GET $1,050</span>\\n            </h5>\\n            <p\\n              style=\\\"\\n                color: black;\\n                font-size: 12px;\\n                font-family: Lato;\\n                font-weight: 500;\\n                white-space: nowrap;\\n              \\\"\\n            >\\n              BONUS BETS + DEPOSIT BONUS\\n            </p>\\n            <button\\n              style=\\\"\\n                cursor: pointer;\\n                border-radius: 4px;\\n                font-weight: 900;\\n                font-family: Lato;\\n                font-size: 14px;\\n                background-image: linear-gradient(to bottom, #16ba5e, #0a9547);\\n                box-shadow: 0 3px 8px 0 rgb(0 0 0 / 20%);\\n                color: #ffffff;\\n                padding: 10px 30px;\\n                border-radius: 3px;\\n                border: none;\\n                margin-left: 15px;\\n              \\\"\\n              class=\\\"get_btn border-0 rounded fw-bold font_lato font_xsm\\\"\\n            >\\n              GET PROMO\\n            </button>\\n          </div>\\n        </div>\\n      </div>\\n    </section> \\n         </div>\\n      <div class=\\\"col-sm-3\\\" style=\\\"padding-left:40px ;\\\">\\n        <img style=\\\"\\n            height:440px;\\n            width: 280px;\\n            padding:15px;\\n            \\\" \\n            src=\\\"https://i.ibb.co/wC9Y9cz/home-loan-design-template-79e0e03d9d0dfc508d86075ccc8cb428-screen.jpg\\\"  alt=\\\"home loan\\\"> \\n      </div>\\n    </div>\\n  </body>\\n</html>\"}]],\"markups\":[],\"sections\":[[10,0],[1,\"p\",[]]],\"ghostVersion\":\"4.0\"}",

        "meta_title": title,
        "meta_description": description,
        "status": "published",
        "feature_image": image_url,
        # "feature_image_alt": description[:125],
        "published_at": date.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        #"tags": [],
        #"authors": []
    }



    
    

    post = {
        "posts": [post_data]
    }

    with open("log.txt", "w") as outfile:
       json.dump(post, outfile)

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
        print(response.json())  # Add this line to print the response JSON
