pip install virtualenv virtualenvwrapper
mkdir %USERPROFILE%\.virtualenvs
(
echo export WORKON_HOME=$HOME/.virtualenvs
echo source "C:\Program Files (x86)\Python36-32\Scripts\virtualenvwrapper.sh"
)>%USERPROFILE%\.bashrc
