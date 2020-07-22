#!/bin/bash

BAK_DIR=~/.vimrcs.bak
rm -rf ${BAK_DIR}
mkdir ${BAK_DIR}
cp ~/.vimrc.local ${BAK_DIR}/.vimrc.local
cp ~/.vimrc.before.local ${BAK_DIR}/.vimrc.before.local
cp ~/.vimrc.bundles.local ${BAK_DIR}/.vimrc.bundles.local
cp ~/idlang.vim ${BAK_DIR}/idlang.vim
cp ~/.ctags ${BAK_DIR}/.ctags
rm ~/.vimrc.local
rm ~/.vimrc.before.local
rm ~/.vimrc.bundles.local
rm ~/idlang.vim
rm ~/.ctags

BASE_DIR=~/.lukevim
ln -s ${BASE_DIR}/.vimrc.local ~/.vimrc.local
ln -s ${BASE_DIR}/.vimrc.before.local ~/.vimrc.before.local
ln -s ${BASE_DIR}/.vimrc.bundles.local ~/.vimrc.bundles.local
ln -s ${BASE_DIR}/idlang.vim ~/idlang.vim
ln -s ${BASE_DIR}/ctags.cnf ~/.ctags

if [[ "$FULL_INSTALL" == "TRUE" ]]; then
    mv -f ~/.spf13-vim-3 ~/bak.spf13-vim-3
    sh <(curl https://j.mp/spf13-vim3 -L)
elif [[ "$UPDATE_INSTALL" == "TRUE" ]]; then
    sh <(curl https://j.mp/spf13-vim3 -L)
fi

