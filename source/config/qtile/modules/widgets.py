from libqtile import widget
from .helpers import route, color

class create():
  def icon(name):
    path=route + "/icons/"
    return widget.Image(
      filename=path + name + ".png",
      margin=3.8,
    )
  def space():
    return widget.Sep(
      linewidth=0,
      padding=6,
    )

def cutter(text):
    rev = text[::-1]
    def position(x):
        value = False
        for i in ['—', '-']:
            if x.find(i) != -1:
                value = x.find(i)+2
        return value
    string = lambda x, p: x[:p][::-1]
    if position(rev):
        name = string(rev, position(rev))
        stat = text[:text.find(name)]
        if len(stat) >= 50:
            return stat[:50] + name
        else:
            return text
    else:
        return text

graph = dict(
  line_width=1,
  border_width=0.8,
  border_color=color['normal'],
  graph_color=color['border'],
)

navigation = [
  widget.GroupBox(
    margin_x=0,
    padding_y=3,
    padding_x=6.5,
    active=color['active'],
    inactive=color['inactive'],
    urgent_text=color['active'],
    this_screen_border=color['border'],
    this_current_screen_border=color['border'],
    other_current_screen_border=color['other'],
    other_screen_border=color['other'],
    urgent_border=color['urgent'],
    urgent_alert_method="block",
    highlight_method="block",
    disable_drag=True,
    rounded=False
  ),
  create.space(),
  widget.WindowName(
    parse_text=cutter,
  ),
  create.space(),
  widget.Systray(
    icon_size=17,
    padding=8,
  ),
  create.space(),
  widget.MemoryGraph(
    **graph, width=18
  ),
  create.space(),
  widget.CPUGraph(
    **graph, width=50
  ),
  create.space(),
  create.icon("connection"),
  widget.Wlan(
    interface="wlp3s0",
    format="{quality}↯70"
  ),
  create.space(),
  create.icon("volume"),
  widget.Volume(),
  create.space(),
  create.icon('bright'),
  widget.Backlight(
      backlight_name="intel_backlight"
  ),
  create.space(),
  create.icon('updates'),
  widget.CheckUpdates(
    distro="Arch",
    no_update_string="N/A",
    display_format="{updates}",
    colour_no_updates=color['text'],
    colour_have_updates=color['success'],
    custom_command_modify=lambda x: x - 4 if x - 4 > 0 else False,
    custom_command='sudo pacman -Syup',
  ),
  create.space(),
  create.icon('calendar'),
  widget.Clock(format='%a  %I:%M %p'),
]

widget_defaults = dict(
  font='Noto Sans Medium',
  foreground=color['text'],
  fontsize=12,
  padding=2
)
extension_defaults = widget_defaults.copy()