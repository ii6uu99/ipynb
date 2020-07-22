call spf13-vim-windows-install.cmd

@if not exist "%HOME%" @set HOME=%HOMEDRIVE%%HOMEPATH%
@if not exist "%HOME%" @set HOME=%USERPROFILE%

@set BASE_DIR=%HOME%\.lukevim
call mklink %HOME%\.vimrc.local %BASE_DIR%\.vimrc.local
call mklink %HOME%\.vimrc.before.local %BASE_DIR%\.vimrc.before.local
call mklink %HOME%\.vimrc.bundles.local %BASE_DIR%\.vimrc.bundles.local
call mklink %HOME%\idllang.vim %BASE_DIR%\idllang.vim
call mklink %HOME%\ctags.cnf %BASE_DIR%\ctags.cnf

