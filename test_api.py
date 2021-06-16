import requests 
image_url = "https://raw.githubusercontent.com/alisaadati97/Pyteeth/master/examples/test_images/IMG_6031.JPG"

url = "http://127.0.0.1:8000/" 
data = {
  "url": image_url,
}
response = requests.post(url,json=data)
print(response.text)