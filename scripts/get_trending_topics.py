import requests
import yaml

with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

news_api_key = config["news_api_key"]

def get_trending_topic():
    # Exemple avec NewsAPI
    url = f"https://newsapi.org/v2/top-headlines?language=fr&apiKey={news_api_key}"
    r = requests.get(url)
    data = r.json()
    articles = data.get("articles", [])
    if not articles:
        return "Les dernières tendances en IA"
    # Prendre le titre du premier article
    topic = articles[0]["title"]
    return topic

if __name__ == "__main__":
    print(get_trending_topic())
