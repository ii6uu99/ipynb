Function Set-WallPaper($Value)
{
 Set-ItemProperty -path 'HKCU:\Control Panel\Desktop\' -name wallpaper -value $value
 rundll32.exe user32.dll, UpdatePerUserSystemParameters
}


Set-Location "~\"
$nasa = Invoke-WebRequest -Uri "https://apod.nasa.gov/apod/astropix.html" -UseBasicParsing
$imageUrl = ($nasa.Links | where {$_.outerHTML -like "*href=`"image/*"}[0]).href
$image = Invoke-WebRequest -Uri ("https://apod.nasa.gov/apod/" + $imageUrl) -UseBasicParsing
[io.file]::WriteAllBytes(".\Desktop\picture_of_the_day.jpg",$image.Content)
Set-WallPaper -value ($env:USERPROFILE + "\Desktop\picture_of_the_day.jpg" )