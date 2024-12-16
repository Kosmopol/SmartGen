import markdown
import os
import glob

# Chemins des dossiers d'entrée et de sortie
input_folder = "content/posts"  # Dossier contenant les fichiers .md
output_folder = "content/html_posts"  # Dossier où les fichiers HTML seront sauvegardés

# Créer le dossier de sortie s'il n'existe pas
os.makedirs(output_folder, exist_ok=True)

# Convertir tous les fichiers Markdown en HTML
for md_file in glob.glob(f"{input_folder}/*.md"):
    with open(md_file, "r", encoding="utf-8") as f:
        md_content = f.read()
        html_content = markdown.markdown(md_content)

    # Créer un fichier HTML avec le même nom
    base_name = os.path.basename(md_file).replace(".md", ".html")
    output_path = os.path.join(output_folder, base_name)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"✅ {base_name} converti en HTML.")
