import yaml
from jinja2 import Template
import datetime
from ai_agent import AIAgent
from get_trending_topics import get_trending_topic
import random

with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

api_key = config["openai_api_key"]
aff_links = ", ".join(config["affiliation_links"])
article_length = config["article_length"]

# Récupérer un sujet tendance
topic = get_trending_topic()

# Charger le template du prompt
with open("templates/prompt.txt", "r", encoding="utf-8") as f:
    prompt_template = f.read()

prompt = Template(prompt_template).render(
    article_length=article_length,
    topic=topic,
    affiliation_links=aff_links
)

agent = AIAgent(api_key=api_key)
article_content = agent.generate_text(prompt)

# Nom de fichier
date_str = datetime.datetime.utcnow().strftime("%Y-%m-%d")
slug = topic.lower().replace(" ", "-").replace(":", "").replace("?", "").replace("!", "")[:50]
post_filename = f"content/posts/{date_str}-{slug}.md"

post_header = f"""---
title: "{topic}"
date: {date_str}
---

"""

with open(post_filename, "w", encoding="utf-8") as f:
    f.write(post_header + article_content)

print(post_filename)
