# HTTP protocol

Hvad betyder HTTP?

1. Åbner TCP-forbindelse (HTTP port 80)
2. Sender request-header:
```GET url HTTP/1.0```
3. Sender request headers
4. 2 x newline
5. modtager response headers
6. modtager indhold
7. forbindelsen lukkes

Eksempel:
```
$ nc 10.0.0.10 80
GET / HTTP/1.0

HTTP/1.1 200 OK
Server: nginx/1.18.0
Date: Tue, 26 Sep 2023 12:19:56 GMT
Content-Type: text/html
Content-Length: 150
Last-Modified: Tue, 26 Sep 2023 12:13:19 GMT
Connection: close
ETag: "6512cadf-96"
Accept-Ranges: bytes

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Nothing to see here</title>
</head>
<body>
Nothing to see here.
</body>
</html>
```

Vi kan også lave HTTPS-requests (hvis vi bruger openssl):

```openssl s_client --connect 10.0.0.10:443```

## Curl

HTTP (og HTTPS) requests fra kommandolinjen.

Simpelt request, output til stdout:

```curl http://10.0.0.10```

Options:

- `-i`: Include response headers
- `-v`: Verbose - request and response headers
- `-o`: Write output to file

## Firefox

Brug Firefox developer tools (F12).

Viser requests (i Network tab).

Edit and resend (højreklik på request).

Cookies kan modificeres i Storage.

Kan bruges til rigtig mange web-ctf-opgaver.

## HTTP-protokollen

https://datatracker.ietf.org/doc/html/rfc2616

https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers

## Cookies

Hvad er cookies?

Overføres via HTTP headers, gemmes på klienten (browseren)

