import json

file = open("19.in",'r')

text = file.read()

json_loaded = json.loads(text)

print(json.dumps(json_loaded, indent=2))
