# import packages
from os import path
from subprocess import call

from libqtile import hook, bar
from libqtile.config import Group, Screen, Key
from libqtile.command import lazy

# import modules
from modules.mouse import *
from modules.layouts import *
from modules.keyboard import keys, mod
from modules.helpers import route
from modules.widgets import *

# create groups
groups = [Group(i) for i in ["NET", "DEV", "TERM", "MEDIA"]]

# convert
def number(num):
  return num if num < len(groups) else 0

# add keys to groups
for i, group in enumerate(groups):
  index = str(number(i + 1))
  keys.extend([
    Key([mod], index, lazy.group[group.name].toscreen()),
    Key([mod, "shift"], index, lazy.window.togroup(group.name))
  ])

#create screens 
#navigation from widgets
screens = [
  Screen(
    top=bar.Bar(
      navigation, 24,
      opacity=0.90
    )
  )
]

# others
cursor_warp = False
auto_fullscreen = True
dgroups_key_binder = None
follow_mouse_focus = True
bring_front_click = False
focus_on_window_activation = "smart"
reconfigure_screens = True
dgroups_app_rules = []
auto_minimize = True
wmname = "LG3D"

# auto start
@hook.subscribe.startup
def autostart():
  call(['sh', path.join(route, 'launch.sh')])