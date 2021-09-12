import json
from os import path

# location qtile config
route = path.join(path.expanduser('~'), ".config", "qtile")

# load theme
def load_theme():
  file = path.join(route, "theme.json")
  if path.isfile(file):
    with open(file, "r") as f:
      return json.load(f)
  else:
    raise Exception("Theme Error")

if __name__ == "modules.helpers":
  color = load_theme()