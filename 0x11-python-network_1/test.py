import urllib.request
import urllib.error
import urllib.parse

url = 'http://www.someserver.com/cgi-bin/register.cgi'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
values = {'name': 'Michael Foord', 'location': 'Northampton', 'language': 'Python'}
headers = {'User-Agent': user_agent}

data = urllib.parse.urlencode(values).encode('ascii')
req = urllib.request.Request(url, data, headers)
try:
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(the_page)
except urllib.error.URLError as e:
    print(f'URL Error: {e.reason}')
except urllib.error.HTTPError as e:
    print(f'HTTP Error: {e.code} - {e.reason}')
except Exception as e:
    print(f'General Error: {e}')