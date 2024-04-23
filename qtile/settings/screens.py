from libqtile import bar, widget, layout
from libqtile.config import Screen, Match
from libqtile.lazy import lazy

from settings.variables import *
from settings.layouts import *
from settings.widgets import *

screens = [
    Screen(
        top=bar.Bar(
            [
                # Imagen Alacritty -----------------
                Spacer(5, colorIMG), 
                widget.Image(
                    filename="~/.config/qtile/alacritty.png",
                    margin=4,
                    background=colorIMG,
                    mouse_callbacks = {
                        'Button1': lazy.spawn("alacritty"),
                    }
                ),
                #TextIcon(text=" ", padding=-12, foreground=colorFecha, background=colorIMG, fontsize=36),
                Spacer(5, colorIMG), 

                # Groups ---------------------------
                widget.GroupBox(
                    active=colorBlanco,
                    inactive=colorBlanco,
                    background=colorIMG,
                    other_screen_border=OtherFocus,
                    this_current_screen_border=ThisFocus,
                    other_current_screen_border=ThisFocus,
                    this_screen_border=OtherFocus,
                    borderwidth=5,
                    highlight_method='block',
                    hide_unused=True,
                    disable_drag=True,
                    center_aligned=True,
                ),
                TextIcon(text=" ", padding=-12, foreground=colorIMG, background=colorBarra, fontsize=36),
                Spacer(10, colorBarra), 

                # Window name ----------------------
                widget.Prompt(),
                widget.WindowName(),
                

                # Temperaturas ---------------------
                TextIcon(text=" ", padding=-12, foreground=colorTemperaturas, background=colorBarra, fontshadow=colorNegro, fontsize=36),
                TextIcon(text="", foreground=colorBlanco, background=colorTemperaturas, fontshadow=colorNegro, fontsize=16),
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
                
                # Layout --------------------------
                TextIcon(text=" ", padding=-12, foreground=colorLayout, background=colorTemperaturas, fontshadow=colorTemperaturas, fontsize=36),
                TextIcon(text="", foreground=colorBlanco, background=colorLayout, fontshadow=colorNegro, fontsize=16),
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

                Spacer(5, colorBarra),

                widget.Systray(
                    background=colorBarra
                ),
                
                Spacer(10, colorBarra),

                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
            ],
            tamanoBarra,
            background=colorBarra,
            margin=[5,10,5,10],
            opacity=1,
            
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
