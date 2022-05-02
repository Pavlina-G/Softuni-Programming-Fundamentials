import re
text = input()

title_regex = r"(?<=<title>).*[^\n](?=</title>)"
body_regex = r"(?<=<body).*(?=\/body>)"
content_regex = r">([^><]*)<" # group = null

title = re.findall(title_regex, text)
if len(title) > 0:
    print(f"Title: {''.join(title)}")

body = re.findall(body_regex, text)
body = ''.join(body)

content = ''.join(re.findall(content_regex, body)).replace("\\n","")
print(f"Content: {content}")