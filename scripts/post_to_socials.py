import os
import requests
import yaml
import glob
import datetime

with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

site_url = config["site_url"]
tags = config["social_tags"]

# Trouver le dernier article généré
posts = glob.glob("content/posts/*.md")
posts.sort(reverse=True)
latest_post = posts[0]

# Extraire le titre du front matter
title = ""
with open(latest_post, "r", encoding="utf-8") as f:
    lines = f.readlines()
    # front matter
    # titre est après title:
    for line in lines:
        if line.startswith("title:"):
            title = line.replace("title:", "").strip().strip('"')
            break

# URL du post (en supposant qu'il suffit du nom de fichier)
post_url = site_url + latest_post.replace("content/posts/", "").replace(".md", ".html")

tweet_text = f"{title}\n{post_url}\n{tags}"

twitter_bearer_token = os.environ.get("TWITTER_BEARER_TOKEN")

# Poster sur Twitter (X)
# Depuis nov. 2023 : Il faut un niveau d'accès approprié à l'API Twitter. Exemple:
# Ici, on simule avec l'endpoint v2 pour créer un tweet (nécessite Elevated access)

url = "https://api.twitter.com/2/tweets"
headers = {
    "Authorization": f"Bearer {twitter_bearer_token}",
    "Content-Type": "application/json"
}
data = {
    "text": tweet_text
}

response = requests.post(url, headers=headers, json=data)
response.raise_for_status()
print("Tweet publié:", response.json())
