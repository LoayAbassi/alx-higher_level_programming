source : https://docs.python.org/3/howto/urllib2.html
==============url's====================================================

urllib.request // library name
x = urllib.request.urlopen("example.com")// sends a request to server and returns object in response
x.read() // will take the content of the object returned and stored in x
{
with urllib.request.urlopen('http://python.org/') as response:
html = response.read()
}

{
urllib.request.Request(link)// helps with head customizations
Request('http://python.org/', headers={'User-Agent': 'Mozilla/5.0'}) // like this
}

======================== temporary files + copying ==============================

tempfile // library name
tempfile.mkstemp() // creates a temporary file and returns a tuple of file name and file

#use it inside a 'with' clause to automate the process of opening and closing :
{
with tempfile.NamedTemporaryFile(delete=False) as tmp_file :
// file will be deleted once block ends
tmp_file.write(b'Hello World')
}

#it is possible to copy url's ressources inside a temp file 'shutil library'
{
with urllib.request.urlopen('http://python.org/') as response:
with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
shutil.copyfileobj(response, tmp_file)
}

========================= encoding ==============================
urllib.parse //library
by default browsers execute post request with forms, sometimes we need it for more
{
values = {'name' : 'Michael Foord',
'location' : 'Northampton',
'language' : 'Python' }

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii') # data should be bytes
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
    the_page = response.read()

}

========================= requests library ==============================

{
import requests
url = 'http://httpbin.org/post'
data = {'key1': 'value1', 'key2': 'value2'}
response = requests.post(url, data=data)
print(response.text)

}

=========================exception handeling ==============================

urllib.error //library
{
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
}

=============================== Openers & Handlers ==================================
urllib.request.OpenerDirector
openers use handlers, each handler knows how to open urls for particular scheme(http, ftp,...)
or how handle an aspect of URL opening, for example HTTP redirections or HTTP cookies.

To create an opener, instantiate an OpenerDirector, and then call .add_handler(some_handler_instance) repeatedly.

# create a password manager

password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

# Add the username and password.

# If we knew the realm, we could use it instead of None.

top_level_url = "http://example.com/foo/"
password_mgr.add_password(None, top_level_url, username, password)

handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

# create "opener" (OpenerDirector instance)

opener = urllib.request.build_opener(handler)

# use the opener to fetch a URL

opener.open(a_url)

# Install the opener.

# Now all calls to urllib.request.urlopen use our opener.

urllib.request.install_opener(opener)

======================================
some urls might not return expected results so u need to use more advanced libraries (cloudscraper)
it's good for antibot error
