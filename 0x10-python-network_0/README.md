python network #0
========== curl ==============
curl : Client URL Rrquest Library
it allows senidng data over urls using cmd(upload(POST), download(GET))
u can use it to transfer files between machines

[curl www.exp.com] // will return the full page, sometimes an empty page if there's
a redirect to another link

curl -L www.exp.com // will return the full page considering redirects
returned data can be stored using this '>' or '-o' after the command

u can also curl an API, test this : [curl http://wttr.in/tunis]

the -b option is useful for scenarios where you need to interact with web applications that rely on cookies to track sessions or user-specific data. => [curl -b "session_id=abc123" http://example.com]

[curl -X POST http://example.com/resource] => defining http method using -X

-s // fetching resources without showing progress results on terminal
-d // used to sendd data in the body of http request
[curl -d "username=user1&password=pass123" http://example.com/login]

-H "headerVar : value" // sets http header to specific value (before each new var)


======= HTTP ================================================================
default port number is 80 // it depends on the protocol used (afp = 548)
if port number specified(google.com : 8080), then default is ignored
a subdomain is like test in test.google.com

HTTPS encrypts data being exchanged
5xx, stands for server error status codes

======= bash ================================================================
when taking argument use $1 for 1st, $2 for 2nd ...
grep word is a filter that takes only lines with 'word' key
to have substrings , u can use cut d 'separation_base' -fstart-
// -f index1,index2 will get specified elements




0.0.0.0:5000/route_