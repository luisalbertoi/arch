#!/bin/sh

#directory and variables
path=$(dirname $(realpath "$0"))
images="$path/images"

#load background
feh --recursive --bg-fill --randomize $images

#load opacity
picom -b