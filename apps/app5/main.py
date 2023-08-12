import requests

api_key = "408a3d1dc3244c4785890da7bc8320d3"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-07-12&sortBy=publishedAt&" \
      "apiKey=408a3d1dc3244c4785890da7bc8320d3"

request = requests.get(url)
content = request.text
print(content)