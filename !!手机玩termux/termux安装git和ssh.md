termux安装git和ssh

安装Git和SSH在运行安装命令之前，您需要更新和升级。为此，发出命令（图B）：

apt update && apt upgrade (enter)





升级完成后，就可以安装Git和SSH了。为此，发出命令：

apt install git openssh
这个命令(图C)将安装两个必要的应用程序。






设置Git存储现在是时候设置Termux存储了。这是通过以下命令（从Termux终端）完成的：

termux-setup-storage (enter)

运行该命令后，系统将提示您允许该应用访问存储。这样做，就可以开始使用Git了。





连接到GitHub有点棘手。从Termux终端，必须首先创建一个ssh密钥对。为此，发出命令：

ssh-keygen -t rsa -C yourName@gmail.com (enter)





登录到.ssh（cd .ssh（enter））

从该目录中，发出命令：

scp id_rsa.pub USER@IP:/home/USER/

其中USER是远程用户名，IP是与Android设备（接受SSH连接）在同一网络上的桌面的远程地址。

将文件存储在远程桌面上后，需要登录GitHub（从现在包含.pub文件的桌面上），然后转到“设置” |“设置”。SSH密钥。将该id_rsa.pub密钥复制到Git中并保存。





登录到Git现在，您已将SSH公钥复制到GitHub，您可以使用以下命令登录到GitHub帐户：

ssh -T git@github.com

一旦通过身份验证，就可以从Android设备开始使用Git了。创建存储库，推送，拉取等。您可能还想帮个忙，并通过Termux（使用apt install nano命令）安装nano编辑器，以便实际上可以编辑代码。

然后你去。在Android设备上使用Git的便捷方法。现在... git开始工作。