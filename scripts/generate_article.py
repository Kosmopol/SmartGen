import yaml
from jinja2 import Template
import datetime
from ai_agent import AIAgent
from get_trending_topics import get_trending_topic
import os

# Récupérer la clé OpenAI depuis l'environnement
openai_api_key = os.environ.get("OPENAI_API_KEY")

with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

# Récupérer les paramètres du config.yaml
aff_links = ", ".join(config["affiliation_links"])
article_length = config["article_length"]

# Créer un agent IA avec la clé provenant des variables d'environnement
agent = AIAgent(api_key=openai_api_key)

# Obtenir un sujet tendance
topic = get_trending_topic()

# Charger le template de prompt
with open("templates/prompt.txt", "r", encoding="utf-8") as f:
    prompt_template = f.read()

# Créer le prompt
prompt = Template(prompt_template).render(
    article_length=article_length,
    topic=topic,
    affiliation_links=aff_links
) + "\n\nThe article must be written in English."

# Générer le contenu de l'article
article_content = agent.generate_text(prompt)

# Créer un nom de fichier basé sur la date et le sujet
os.makedirs("content/posts", exist_ok=True)
date_str = datetime.datetime.utcnow().strftime("%Y-%m-%d")
slug = topic.lower().replace(" ", "-").replace(":", "").replace("?", "").replace("!", "")[:50]
post_filename = f"content/posts/{date_str}-{slug}.md"

# Mettre des métadonnées dans le front matter
post_header = f"""---
title: "{topic}"
date: {date_str}
---

"""

# Écrire l'article dans le fichier
with open(post_filename, "w", encoding="utf-8") as f:
    f.write(post_header + article_content)

print(post_filename)
