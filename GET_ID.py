import requests

post_id = 123
url = f"https://api.news.com/posts/{post_id}"
response = requests.get(url)

if response.status_code == 200:
    post = response.json()
    print(post)
else:
    print("Failed to get post")