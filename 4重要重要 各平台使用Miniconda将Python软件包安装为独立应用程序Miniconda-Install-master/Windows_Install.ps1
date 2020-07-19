$ErrorActionPreference = "Stop"

# 要安装的应用程序的名称 
$AppName="minconda"

# 在这里设置项目的安装目录名
$InstallDir="minconda"

#conda安装的依赖项 
# 如果没有Conda依赖项，请推荐下一行
$CondaDeps="numpy","scipy","scikit-learn","pandas" # some examples

# 用pip安装的依赖项
#如果没有PyPi依赖项，请注释掉下一行
$PyPiPackage="mypackage"

# 要安装的本地软件包
# 如果您的应用程序不在PyPi中，则很有用
# 用.tar.gz分发它并使用此变量
# 如果没有要安装的本地软件包，请注释下一行
$LocalPackage="mypackage.tar.gz"

# 要添加到路径的入口点
# 注释掉没有入口点的下一行
#  （尽管不确定为什么该脚本否则会很有用）
$EntryPoint="minconda"

Write-Host ("`nInstalling $AppName to "+(get-location).path+"\$InstallDir")


#下载最新的Miniconda安装程序
Write-Host "`nDownloading Miniconda Installer...`n"

(New-Object System.Net.WebClient).DownloadFile("https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-py38_4.8.2-Windows-x86_64.exe", "$pwd\Miniconda_Install.exe")

#通过Miniconda安装Python环境
Write-Host "Installing Miniconda...`n"
Start-Process Miniconda_Install.exe "/S /AddToPath=0 /D=$pwd\$InstallDir" -Wait

# 将依赖项安装到新的Python环境
$env:Path = "$pwd\$InstallDir\Scripts;" + $env:Path

# 使新的python环境完全独立 
# 修改site.py文件，以便不导入USER_SITE 
$site_program = @"
import site
site_file = site.__file__.replace('.pyc', '.py');
with open(site_file) as fin:
    lines = fin.readlines();
for i,line in enumerate(lines):
    if(line.find('ENABLE_USER_SITE = None') > -1):
        user_site_line = i;
        break;
lines[user_site_line] = 'ENABLE_USER_SITE = False\n'
with open(site_file,'w') as fout:
    fout.writelines(lines)
"@
python -c $site_program

if(Test-Path variable:CondaDeps)
{
    Write-Host "Installing Conda dependencies...`n"
    conda install $CondaDeps -y
}

if(Test-Path variable:PyPiPackage)
{
    Write-Host "Installing PyPi dependencies...`n"
    pip install $PyPiPackage
}

if(Test-Path variable:LocalPackage)
{
    Write-Host "Installing Local package...`n"
    pip install $LocalPackage
}

# Cleanup
Remove-Item "Miniconda_Install.exe"
conda clean -iltp --yes

# Add Entry Point to path

if(Test-Path variable:EntryPoint)
{
    # Move entry-point executable to an isolated folder
    $script_folder = "$pwd\$InstallDir\PathScripts"
    New-Item $script_folder -type directory | Out-Null
    Move-Item $pwd\$InstallDir\Scripts\$EntryPoint.exe $script_folder

    # Ask user if they want to update path
    $title = "Update Path"
    $message = "`nDo you want to add the $EntryPoint script to your User PATH?"

    $yes = New-Object System.Management.Automation.Host.ChoiceDescription "&Yes", `
        "Prepends the User PATH variable with the location of the $EntryPoint script"

    $no = New-Object System.Management.Automation.Host.ChoiceDescription "&No", `
        "User PATH is not modified"

    $options = [System.Management.Automation.Host.ChoiceDescription[]]($yes, $no)

    $result = $host.ui.PromptForChoice($title, $message, $options, 0) 

    if($result -eq 0)
    {
        # Update the user's path
        $old_path = (Get-ItemProperty -Path HKCU:\Environment).Path
        $new_path = $script_folder + ";" + $old_path
        cmd /c "setx PATH $new_path"
        Set-ItemProperty -Path HKCU:\Environment -Name PATH -Value $new_path
        Write-Host "User PATH has been updated"
        Write-Host "Open a new command prompt to see the change"
    }
    else
    {
        Write-Host "User PATH was not modified.`n"
        Write-Host "You may want to add the $EntryPoint script to your path."
        Write-Host "It is located in: $script_folder`n"
    }
}

Write-Host "`n$AppName Successfully Installed"

Write-Host "Press any key to continue ..."

$x = $host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
