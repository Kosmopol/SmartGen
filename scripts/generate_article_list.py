import os
import json

# Chemin vers le dossier des articles
posts_folder = "content/posts"
output_file = "articles.json"

# Lister tous les fichiers .md triés par date (du plus récent au plus ancien)
articles = sorted(
    [f for f in os.listdir(posts_folder) if f.endswith(".md")],
    reverse=True
)

# Générer la structure JSON
article_data = [{"file": file} for file in articles]

# Écrire dans le fichier articles.json
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(article_data, f, indent=2, ensure_ascii=False)

print(f"articles.json mis à jour avec {len(articles)} articles.")
