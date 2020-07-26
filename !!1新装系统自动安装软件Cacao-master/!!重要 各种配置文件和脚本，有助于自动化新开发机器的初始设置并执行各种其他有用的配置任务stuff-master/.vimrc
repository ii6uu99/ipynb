set nocompatible

"stuff required for vundle
filetype off
set rtp+=~/vimfiles/bundle/Vundle.vim "set the RunTimePath to include Vundle and initialize
call vundle#begin('~/vimfiles/bundle/')

"plugins go here
Plugin 'VundleVim/Vundle.vim' "why do I have to tell vundle that I'm using vundle?
Plugin 'NLKNguyen/papercolor-theme'
Plugin 'easymotion/vim-easymotion'
Plugin 'OrangeT/vim-csharp'
Plugin 'PProvost/vim-ps1'
Plugin 'tpope/vim-surround'
Plugin 'michaeljsmith/vim-indent-object'
Plugin 'kchmck/vim-coffee-script'

call vundle#end()
filetype plugin indent on
"end of stuff required for vundle

source $VIMRUNTIME/vimrc_example.vim
source $VIMRUNTIME/mswin.vim

"delete autocmds set from above files
autocmd! vimrcEx FileType text

behave mswin
set dir=%TMP%
set backupdir=%TMP%
set undofile
set undodir=%TMP%
set lines=60 columns=150
set ignorecase
set smartcase
set relativenumber
set number
set tabstop=4 shiftwidth=4 expandtab
set guifont=Cascadia_Code:h10
set enc=utf-8
set fileencoding=utf-8
set fileencodings=ucs-bom,utf8
set textwidth=0
set shell=powershell\ -noprofile
set shellcmdflag=-command
set shellxquote="
set splitbelow
set splitright
set diffopt=internal,filler,vertical

nnoremap ? /\v
vnoremap ? /\v
set gdefault
set incsearch
set showmatch
set hlsearch
set autoindent
set cursorline
set scrolloff=3

"this stuff from http://stevelosh.com/blog/2010/09/coming-home-to-vim/
"nnoremap <up> <nop>
"nnoremap <down> <nop>
"nnoremap <left> <nop>
"nnoremap <right> <nop>
"inoremap <up> <nop>
"inoremap <down> <nop>
"inoremap <left> <nop>
"inoremap <right> <nop>
nnoremap j gj
nnoremap k gk
nnoremap ; :
"inoremap jj <ESC>
nnoremap <Esc><Esc> :<C-u>nohlsearch<CR>
nnoremap <PageUp> <C-u>
nnoremap <PageDown> <C-d>
inoremap <Esc> <Esc>`^
inoremap <c-space> <c-n>

"set up leader
nnoremap <SPACE> <Nop>
let mapleader=" "

:se autochdir   "auto-set current working directory to current file's directory

"bad ideas regarding copy/paste that will be left for posterity
"nnoremap yy "+Y
"nnoremap P "+P
"set clipboard=unnamed

set guioptions-=m  "remove menu bar
set guioptions-=T  "remove toolbar
set guioptions-=r  "remove right-hand scroll bar

"Most Recently Used
:command MRU browse oldfiles
"
"doesn't make much sense - it's the alias for Invoke-Item in Powershell, used like "ii ./", just to keep the name the same
:command II !start explorer /select,%:p 

"opens current file as hexadecimal
:command HEX !start "C:\Program Files\HxD\HxD.exe" "%:p"

"plugins stuff

"easymotion
map f <Plug>(easymotion-s2)
let g:EasyMotion_smartcase = 1

"papercolor
set background=dark
colorscheme PaperColor

set diffexpr=MyDiff()
function MyDiff()
  let opt = '-a --binary '
  if &diffopt =~ 'icase' | let opt = opt . '-i ' | endif
  if &diffopt =~ 'iwhite' | let opt = opt . '-b ' | endif
  let arg1 = v:fname_in
  if arg1 =~ ' ' | let arg1 = '"' . arg1 . '"' | endif
  let arg2 = v:fname_new
  if arg2 =~ ' ' | let arg2 = '"' . arg2 . '"' | endif
  let arg3 = v:fname_out
  if arg3 =~ ' ' | let arg3 = '"' . arg3 . '"' | endif
  let eq = ''
  if $VIMRUNTIME =~ ' '
    if &sh =~ '\<cmd'
      let cmd = '""' . $VIMRUNTIME . '\diff"'
      let eq = '"'
    else
      let cmd = substitute($VIMRUNTIME, ' ', '" ', '') . '\diff"'
    endif
  else
    let cmd = $VIMRUNTIME . '\diff'
  endif
  silent execute '!' . cmd . ' ' . opt . arg1 . ' ' . arg2 . ' > ' . arg3 . eq
endfunction


