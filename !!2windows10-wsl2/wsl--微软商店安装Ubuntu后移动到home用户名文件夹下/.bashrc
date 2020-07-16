HISTCONTROL=ignoreboth
shopt -s histappend
HISTSIZE=1000
HISTFILESIZE=2000
shopt -s checkwinsize

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '

alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias ll='ls -alFh'
alias la='ls -A'
alias l='ls -CF'

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

alias proxify='export http_proxy="http://0.0.0.0:8118";export https_proxy="https://0.0.0.0:8118";export HTTP_PROXY="http://0.0.0.0:8118";export HTTPS_PROXY="https://0.0.0.0:8118"'
alias unproxify='unset http_proxy; unset https_proxy; unset HTTP_PROXY; unset HTTPS_PROXY'

export PATH=$PATH:$HOME/local/go/bin:$HOME/go/bin
export PATH=$PATH:$HOME/.local/bin
alias jn="jupyter-notebook --no-browser"

# >>> conda initialize >>>
__conda_setup="$("/home/${USER}/miniconda3/bin/conda" 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/${USER}/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/home/${USER}/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/${USER}/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<


#增加wsl权限
#https://www.jianshu.com/p/4443a24139d0
if [[ "$(umask)"=='000' ]]; then
    umask 022
fi

