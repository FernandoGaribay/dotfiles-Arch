from libqtile import bar, widget, layout
from libqtile.config import Screen, Match
from libqtile.lazy import lazy

from settings.variables import *
from settings.layouts import *

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active=colorActivo,
                    borderwidth=2,
                    disable_drag=True,
                ),
                widget.Prompt(),
                widget.WindowName(),
                
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),

                widget.TextBox(
                    text = "",
                    foreground="#F2C979",
                    padding=-12,
                    fontsize = 36,
                ),
                widget.TextBox(
                    text="󰥔",
                    fontshadow=colorNegro,
                    background="#F2C979",
                ),
                widget.Pomodoro(
                    prefix_inactive="POMODORO",
                    prefix_active="Trabajo: ",
                    prefix_break="Descanso: ",
                    background="#F2C979",
                    fontshadow=colorNegro,
                    fmt='<b>{}</b>',
                    color_inactive="#FFF"
                ),
                widget.TextBox(
                    text = " ",
                    foreground=colorTemperaturas,
                    background="#F2C979",
                    fontshadow=colorNegro,
                    padding=-12,
                    fontsize = 36,
                ),
                widget.TextBox(
                    text = "",
                    fontshadow=colorNegro,
                    background=colorTemperaturas,
                ),
                widget.CPU(
                    fmt='<b>{}</b>',
                    background=colorTemperaturas,
                    fontshadow=colorNegro,
                ),
                widget.ThermalSensor(
                    tag_sensor='Tctl',
                    format='<b>: {temp:.0f}{unit}</b>',
                    background=colorTemperaturas,
                    fontshadow=colorNegro,
                ),
                widget.TextBox(
                    text = " ",
                    foreground=colorLayout,
                    background=colorTemperaturas,
                    padding=-12,
                    fontsize = 36,
                ),
                widget.TextBox(
                    text="",
                    fontshadow=colorNegro,
                    background=colorLayout,
                ),
                widget.CurrentLayout(
                    background=colorLayout,
                    fmt='<b>{}</b>',
                    fontshadow=colorNegro,
                ),
                widget.TextBox(
                    text = " ",
                    foreground=colorFecha,
                    background=colorLayout,
                    padding=-12,
                    fontsize = 36,
                ),
                widget.TextBox(
                    text="󰃰",
                    fontshadow=colorNegro,
                    background=colorFecha,
                ),
                widget.Clock(
                    format="%Y-%m-%d %a %I:%M %p",
                    fmt='<b>{}</b>',
                    background=colorFecha,
                    fontshadow=colorNegro,
                ),
                widget.TextBox(
                    text = " ",
                    foreground=colorBarra,
                    background=colorFecha,
                    padding=-12,
                    fontsize = 36,
                ),

                
                widget.Systray(
                    background=colorBarra
                ),
                
                widget.TextBox(
                    text="⏻",
                    background=colorBarra,
                    padding=15,
                    fontsize=15,
                    mouse_callbacks={'Button1': lazy.spawn('bash /home/fernando/.config/qtile/shutdownOptions.sh')}
                ),
            ],
            tamanoBarra,
            background=colorBarra,
            #border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            #border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
            #border_color=["ffffff", "ffffff", "ffffff", "ffffff"]
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),

    Screen(
        top=bar.Bar(
            [
                widget.WindowName(),
            ],
            tamanoBarra,
            background=colorBarra,
        ),
        #layouts=[
        #    layout.Max(),
        #],
    ),
]
