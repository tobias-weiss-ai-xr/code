# https://www.youtube.com/watch?v=qbLc5a9jdXo
# https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request
# source ~/venv/python311/bin/activate
# pip install requests
import requests
import json

response = requests.get(
    "http://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow"
)

for data in response.json()["items"]:
    if data["answer_count"] == 0:
        print(data["title"])
        print(data["link"])
    else:
        print("skipped")
    print()
