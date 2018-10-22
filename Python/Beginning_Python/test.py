import requests

email = "nishleymburu@gmail.com"
url = "http://picasaweb.google.com/data/entry/api/user/{}?alt=json".format(email)

data = requests.get(url).json()
image_url = data["entry"]["gphoto$thumbnail"]["$t"]

print(image_url)
