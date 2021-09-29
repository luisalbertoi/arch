from libqtile.lazy import lazy
from libqtile.config import Key

mod = "mod4"
terminal = "alacritty"

keys = [
  Key([mod], "h", lazy.layout.left()),
  Key([mod], "l", lazy.layout.right()),
  Key([mod], "j", lazy.layout.down()),
  Key([mod], "k", lazy.layout.up()),

  Key([mod], "Return", lazy.spawn(terminal)),

  Key([mod], "Tab", lazy.next_layout()),
  Key([mod], "w", lazy.window.kill()),

  Key([mod, "control"], "r", lazy.restart()),
  Key([mod, "control"], "q", lazy.shutdown()),

  Key([mod], "r", lazy.spawn("rofi -show")),
  Key([mod], "c", lazy.spawn("rofi -show calc")),

  Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 5%-")),
  Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 5%+")),
  Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle")),

  Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
  Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]