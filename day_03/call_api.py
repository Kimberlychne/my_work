import requests

# Use requests package to call your api address http://127.0.0.1:5000/api/joke to display a funny joke

url = "https://127.0.0.1:5000"

print("1. Getting one random joke:")
response = requests.get(url+"/api/joke")
joke_data = response.json
print("Q:"+joke_data['setup'])
print("A:" + joke_data['punchline'])
print()

print('2. Getting three random jokes:')
response = requests.get(url + "/api/jokes/3")
jokes_data = response.json()

counter = 1
for joke in jokes_data:
    print("Joke #" +str(counter)+ ":")
    print("Q: " + joke['setup'])
    print("A: "+ joke ['punchline'])
    print()
    counter += 1
