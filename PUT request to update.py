import requests

post_id = 123
url = f"https://api.news.com/posts/{post_id}"
data = {"title": "Updated title", "body": "Updated body"}
headers = {"Content-Type": "application/json"}
response = requests.put(url, json=data, headers=headers)

if response.status_code == 200:
    post = response.json()
    print(post)
else:
    print("Failed to update post")