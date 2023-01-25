#coding:utf-8
import cgi

print("Content type: text/html; charset=utf-8\n")

html = """<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <title>test serveur http python</title>
</head>
<body>
    <h1>Bienvenue</h1>
    <p>test d'un server http en python</p>
</body>
</html>
"""
print(html)