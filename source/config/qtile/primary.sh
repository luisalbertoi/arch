#!/bin/sh

#directory and variables
path=$(dirname $(realpath "$0"))
images="$path/images"

#load background
feh --recursive --bg-fill --randomize $images &

#blue light filter
redshift -l 4.7:74.0 -t 5700:3500 &

#load opacity
picom -b &