#!/usr/bin/env bash

#login to 'devbox' container.
#Password for user 'devbox' is 'asdf'
ssh devbox@127.0.0.1

#start xpra
xpra start --windows --no-microphone --no-webcam --no-speaker --pulseaudio=no --printing=no :10

#alternative version of above command
#xpra start --windows --no-microphone --no-webcam --no-speaker --pulseaudio=no --printing=no --xvfb="Xorg -noreset -nolisten tcp +extension GLX -config /etc/xpra/xorg.conf +extension RANDR +extension RENDER -logfile ${HOME}/.xpra/Xorg-10.log" :10

#verify logs if needed
#less /home/devbox/.xpra/:10.log

#start firefox
DISPLAY=:10 firefox

# now go to back to windows CMD
