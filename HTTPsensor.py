import urllib.request

req = urllib.request.Request('http://192.168.0.2')

with urllib.request.urlopen(req) as response:
    the_page = response.getheaders()

print(the_page)