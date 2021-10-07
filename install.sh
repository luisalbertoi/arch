#!/bin/bash

# intro
cat <<EOF
***********************************************
Session Manager: Ly                                           
Desktop Environment: Qtile                    *
Theme Desktop: Arc Dark                       *
Wallpaper: Unsplash                                           
***********************************************
EOF

echo "¡Hello $USER!"
echo "To continue enter your password..."
sudo pacman -Syu --noconfirm || exit

# global
route=$(dirname $(realpath "$0"))

function install() {
  pacman -Qi $1 | grep -o $1 > /dev/null
  if [ $? -ne 0 ]; then
    echo "installing $1..."
    $2 --noconfirm
  fi
}

# pacman
list='
  xorg
  ntfs-3g
  alsa-utils
  pulseaudio mesa
  pulseaudio-alsa
  brightnessctl firefox
  redshift python qtile
  python-psutil python-iwlib
  ttf-anonymous-pro noto-fonts
  base-devel alacritty rsync
  picom nemo rofi
  neofetch tree
  feh git
'

for name in $list; do
  install $name "sudo pacman -S $name"
done

# AUR - YAY
url="https://aur.archlinux.org/yay"
cd /tmp/ && git clone $url && cd yay/
install yay "makepkg -si"

# list
aur='
  gotop
  rofi-calc ly
  arc-gtk-theme
  arc-icon-theme
'

for name in $aur; do
  install $name "yay -S $name"
done

# config system
gsettings set org.cinnamon.desktop.default-applications.terminal exec alacritty

access="$USER ALL=(ALL) NOPASSWD: /bin/poweroff, /bin/reboot, /bin/pacman -Syu, /bin/pacman -Syup"
sudo sed -i "84 i $access" /etc/sudoers

# copy files
sudo rsync -rvh $route/source/system/. /etc/
rsync -rvh $route/source/config/. ~/.config/

# enable services
sudo systemctl enable ly
systemctl --user enable redshift

# clean cache
yay -Sc --noconfirm

# reboot system
sudo reboot