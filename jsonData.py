import json

x='{"name":"John","age":23}'
y=json.loads(x)
print(type(y),y)
print(y["name"])
z=json.dumps(y)
print(type(z),z)