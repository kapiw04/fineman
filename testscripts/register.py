# register a test user
import requests
import random
url = "http://127.0.0.1:5000/auth/register"
post = {"username": "filip"+str(random.randint(0, 10010)), "password":"haslofilipa", "email":"filip@agh.edu.pl"}
request = requests.post(url, json=post)
print(request.text)