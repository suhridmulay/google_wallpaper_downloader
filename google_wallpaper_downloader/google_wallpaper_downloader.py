import requests


for i in range(1500, 1600):
    url = "https://earthview.withgoogle.com/download/" + str(i) + ".jpg"
    img = requests.get(url)
    img.status_code()
    if img.status_code != 404:
        filename = str(i) + '.jpg'
        open(filename, 'wb').write(img.content)
