from libqtile import layout
from libqtile.config import Match
from .helpers import color

border = lambda x: color[x][0]

layouts = [
    layout.MonadTall(
        border_width=1,
        border_focus=border('focus'),
        border_normal=border('normal')
    ),
    layout.Max()
]

floating_layout = layout.Floating(float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),
    Match(wm_class='makebranch'),
    Match(wm_class='maketag'),
    Match(wm_class='ssh-askpass'),
    Match(title='branchdialog'),
    Match(title='pinentry'),
],
border_normal=border('normal'),
border_focus=border('focus')
)