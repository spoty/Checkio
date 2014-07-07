from collections import OrderedDict


def flatten(dictionary):
    stack = [((), dictionary)]
    result = {}
    while stack:
        path, current = stack.pop()
        for k, v in current.items():
            if v == {}:
                result["/".join((path + (k,)))] = ''
            if isinstance(v, dict):
                stack.append((path + (k,), v))
            else:
                result["/".join((path + (k,)))] = v
    return result

print flatten({"name": {
    "first": "One",
    "last": "Drone"},
    "job": "scout",
    "recent": {},
    "additional": {
    "place": {
        "zone": "1",
        "cell": "2"}}}
) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}

