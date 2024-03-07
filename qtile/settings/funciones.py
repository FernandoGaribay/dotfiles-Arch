import os
import subprocess
from libqtile import hook

from typing import List

from libqtile import bar, layout, widget
from libqtile.config import Group, Match, Screen
from libqtile.utils import guess_terminal

def fc_separador():
    return widget.Sep(
        linewidth = 0,
        padding = 16,
        background = "#282a36"
    )
