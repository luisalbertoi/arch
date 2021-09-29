from libqtile import widget
from .helpers import route, color

class create():
  def Icon(name):
    path=route + "/icons/"
    return widget.Image(
      filename=path + name + ".png",
      margin=4,
    )
  def Separator():
    return widget.TextBox(
      text='⁝',
      fontsize=14
    )
  def space():
    return widget.Sep(
      linewidth=0,
      padding=4
    )

def handler(text):
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

primary = [
  widget.GroupBox(
    margin_x=0,
    padding_y=4,
    padding_x=6.5,
    active=color['active'],
    inactive=color['inactive'],
    highlight_method='block',
    this_screen_border=color['button'],
    this_current_screen_border=color['button'],
    other_current_screen_border=color['secundary'],
    other_screen_border=color['secundary'],
    disable_drag=True
  ),
  create.space(),
  widget.WindowName(
    parse_text=handler,
  ),
  widget.Systray(
    icon_size=15
  ),
  create.space(),
  create.Icon("chipset"),
  widget.CPU(
    format="{load_percent}%"
  ),
  create.Separator(),
  create.Icon("wifi"),
  widget.Wlan(
    interface="wlp3s0",
    format="{quality}/70"
  ),
  create.Separator(),
  create.Icon("volume"),
  widget.Volume(),
  create.Separator(),
  create.Icon('bright'),
  widget.Backlight(
      backlight_name="intel_backlight"
  ),
  create.Separator(),
  create.Icon('update'),
  widget.CheckUpdates(
    distro="Arch",
    no_update_string="N/A",
    display_format="{updates}",
    custom_command='sudo pacman -Syup',
    custom_command_modify=lambda x: x - 4 if x - 4 > 0 else False 
  ),
  create.Separator(),
  create.Icon('calendar'),
  widget.Clock(format='%a %I:%M %p'),
]

widget_defaults = dict(
    font='Noto Sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()