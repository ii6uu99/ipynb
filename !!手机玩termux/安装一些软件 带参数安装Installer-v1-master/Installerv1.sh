#!/data/data/com.termux/files/usr/bin/bash
clear
figlet Installer

echo "Create By Raihan R"
echo "------------------------------------------------"
echo " 1.Untuk Meng-install"
echo "------------------------------------------------"
echo " 2.Untuk Keluar"
echo "------------------------------------------------"


read -p ">" test

if [ $test = 1 ]
then														 
clear 
echo "Sedang Meng-install"

apt update && apt upgrade 
pkg install python2 
pkg install python 
pkg install php 
pkg install pip 
pkg install python2-dev 
pkg install git 
pkg install ruby 
pkg install perl 
pkg install pip mechanize 
pkg install pip 
pkg install nano 
pkg install figlet 
pkg install sh
pkg install toilet
pip install --upgrade pip

fi


if [ $test = 2 ]
then
exit 
fi
