#!/bin/sh

# Configuracion de monitores
xrandr --output DP-0 --off --output DP-1 --mode 1280x768 --pos 0x156 --rotate normal --output DP-2 --off --output DP-3 --off --output HDMI-0 --primary --mode 1920x1080 --pos 1280x0 --rotate normal --output DP-4 --off --output DP-5 --off --output None-2-1 --off --output HDMI-1-1 --off --output DVI-D-1-1 --off --output HDMI-1-2 --off &

# Configuracion del teclado en latinoamerica
setxkbmap latam &

# Inicializar Picom para efectos visuales
picom -f --xrender-sync-fence &

# Inicializar nitrogen (fondo de pantalla)
nitrogen --restore &

# Iconos del sistema
udiskie -t &
nm-applet &
volumeicon &
cbtticon -u 5 &
