from libqtile import bar, widget, layout
from libqtile.config import Screen
from libqtile.lazy import lazy

from settings.variables import *

def Spacer(length=10, background=colorBarra):
    return  widget.Spacer(
        length=length,
        background=background,
    ) 
    
def TextIcon(text="", padding=0, foreground=colorIMG, background=colorBlanco, fontshadow=colorNegro, fontsize=36):
    return widget.TextBox(
        text=text,
        padding=padding,
        foreground=foreground,
        background=background,
        fontshadow=fontshadow,
        fontsize=fontsize,
    )
