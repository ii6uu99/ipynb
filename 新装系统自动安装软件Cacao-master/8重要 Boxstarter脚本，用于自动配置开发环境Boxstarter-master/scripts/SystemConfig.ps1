#--- Enable developer mode on the system ---
Set-ItemProperty -Path HKLM:\Software\Microsoft\Windows\CurrentVersion\AppModelUnlock -Name AllowDevelopmentWithoutDevLicense -Value 1

#--- Add Run As Different User option
Set-ItemProperty -Path HKCU:\Software\Policies\Microsoft\Windows\Explorer -Name ShowRunasDifferentuserinStart -Value 1
