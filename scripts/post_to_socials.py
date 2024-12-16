import os
import requests
import yaml
import glob

# Charger la configuration
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
    for line in lines:
        if line.startswith("title:"):
            title = line.replace("title:", "").strip().strip('"')
            break

# Générer l'URL du post
post_url = site_url + latest_post.replace("content/posts/", "").replace(".md", ".html")

# Contenu du message
status_message = f"{title}\n{post_url}\n{tags}"

# Configuration Mastodon
mastodon_instance = "https://mastodon.social"  # Remplace par l'instance Mastodon de ton choix
access_token = os.environ.get("MASTODON_ACCESS_TOKEN")

if not access_token:
    raise ValueError("❌ MASTODON_ACCESS_TOKEN manquant dans les variables d'environnement.")

# URL de l'API Mastodon pour publier un statut
url = f"{mastodon_instance}/api/v1/statuses"

# En-têtes et données pour la requête
headers = {"Authorization": f"Bearer {access_token}"}
payload = {"status": status_message}

# Envoyer le statut à Mastodon
response = requests.post(url, headers=headers, data=payload)

# Vérifier la réponse
if response.status_code in [200, 202]:
    print("✅ Statut publié avec succès sur Mastodon !")
else:
    print(f"❌ Erreur {response.status_code}: {response.text}")
    response.raise_for_status()
