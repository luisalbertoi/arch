from libqtile.lazy import lazy
from libqtile.config import Key

mod = "mod4"
terminal = "alacritty"

keys = [
  Key([mod], "Right", lazy.layout.next()),
	Key([mod], "Left", lazy.layout.previous()),

  Key([mod, "shift"], "Up", lazy.layout.grow()),
	Key([mod, "shift"], "Down", lazy.layout.shrink()),

  Key([mod], "m", lazy.layout.maximize()),
  Key([mod], "n", lazy.layout.normalize()),

  Key([mod, "shift"], "space", lazy.layout.flip()),

  Key([mod], "Tab", lazy.next_layout()),
  Key([mod], "w", lazy.window.kill()),

  Key([mod], "Return", lazy.spawn(terminal)),

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