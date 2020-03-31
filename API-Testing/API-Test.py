# importing the requests library
import requests
import json

# api-endpoint 
GET_URL = "https://postman-echo.com/get?foo1=bar1&foo2=bar2"
POST_URL = "https://reqres.in/api/users"
# sending get request and saving the response as response object
r = requests.get(url = GET_URL)
print(json.dumps(r.json(), indent=2))

# Post payload to API
user_payload = {
                "name": "person1",
                "job": "Helpdesk"
               }

post = requests.post(url = POST_URL, data = user_payload)
print("Post results: %s" % post.json())

