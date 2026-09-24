import os
import requests

DEEPSEEK_KEY = os.getenv("DEEPSEEK_API_KEY")
ETSY_KEY = os.getenv("ETSY_API_KEY")
SHOP_ID = os.getenv("ETSY_SHOP_ID")

# 1. Etsy se listings lao
def get_etsy_listings():
    url = f"https://openapi.etsy.com/v3/application/shops/{SHOP_ID}/listings"
    headers = {"x-api-key": ETSY_KEY}
    r = requests.get(url, headers=headers)
    return r.json().get('results', [])

# 2. DeepSeek se naya SEO title banao
def get_new_title(old_title):
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {"Authorization": f"Bearer {DEEPSEEK_KEY}"}
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": f"Rewrite this Etsy title for better SEO, keep 140 chars, add viral keywords: {old_title}"}]
    }
    res = requests.post(url, headers=headers, json=data)
    return res.json()['choices'][0]['message']['content']

# 3. Main kaam
listings = get_etsy_listings()
for item in listings[:5]: # Roz sirf 5 listing update karega taake free me rahe
    new_title = get_new_title(item['title'])
    print(f"Updated: {item['title']} -> {new_title}")
    # Yahan Etsy update API lag jayega
