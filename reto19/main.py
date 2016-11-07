import json
from collections import OrderedDict

file = open("19.in",'r')

text = file.read()

json_loaded = json.loads(text, object_pairs_hook=OrderedDict)
print(json.dumps(json_loaded, indent=2))
