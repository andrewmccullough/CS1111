import urllib.request

url = "http://google.com"
f = urllib.request.urlopen(url)
t = f.read()

print(t)
