import aiohttp
from datetime import datetime as date
from pymongo import MongoClient
from config import MONGODB_CONNECTION
from ghost_publisher import publish_article
from article_generator import generate_article
from config import NEWS_API_KEY
import logging
mongo_client = MongoClient(MONGODB_CONNECTION)
mongo_db = mongo_client["autosite_db"]
mongo_collection = mongo_db["articles"]


async def persist_todb():
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey={NEWS_API_KEY}"
        ) as resp:
            data = await resp.json()
            for idx, article in enumerate(data["articles"]):
                article_data = generate_article(article["url"], article["title"], article["description"])
                image_url = article["urlToImage"]

                # Publish data to Ghost
                publish_article(
                    address="https://your-ghost-blog-url.com/ghost/api/v3/content/posts/",
                    title=article_data["title"],
                    description=article_data["description"],
                    content=article_data["content"]
                )

                # Save data to MongoDB
                mongo_collection.insert_one({
                    "title": article_data["title"],
                    "description": article_data["description"],
                    "content": article_data["content"],
                    "image_url": image_url,
                    "created_at": date.now()
                })
                logging.info(f"Saved article with title: {article_data['title']} to MongoDB")
                print(f"{100 / len(data['articles']) * (idx + 1)}%")
