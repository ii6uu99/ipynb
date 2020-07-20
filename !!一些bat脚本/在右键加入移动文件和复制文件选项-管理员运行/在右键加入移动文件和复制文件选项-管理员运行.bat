@echo off 2>nul 3>nul
set reg=HKCR\AllFilesystemObjects\shellex\ContextMenuHandlers
reg query "%reg%\Copy To"&&reg query "%reg%\Move To"&&(
        title delete
        reg delete "%reg%\Copy To" /f
        reg delete "%reg%\Move To" /f
        rem 两个键值都存在则删除
)||(
        title add
        reg add "%reg%\Copy To" /ve /d "{C2FBB630-2971-11D1-A18C-00C04FD75D13}"
        reg add "%reg%\Move To" /ve /d "{C2FBB631-2971-11D1-A18C-00C04FD75D13}"
        rem 两个键值中只要有一个不存在，就添加
)
pause