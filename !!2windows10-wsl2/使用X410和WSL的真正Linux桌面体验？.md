https://www.linuxlinks.com/real-linux-desktop-experience-X410-WSL/



# 使用X410和WSL的真正Linux桌面体验？

[五月29，2019](https://www.linuxlinks.com/real-linux-desktop-experience-x410-wsl/) [Steve Emms](https://www.linuxlinks.com/author/linuxlinks/)[ Desktop](https://www.linuxlinks.com/category/desktop/)，[ Office](https://www.linuxlinks.com/category/office/)，[生产率](https://www.linuxlinks.com/category/productivity/)，[评论](https://www.linuxlinks.com/category/reviews/)，[软件](https://www.linuxlinks.com/category/software/)

如果要在Windows中运行Linux，则有多种选择。最受欢迎的是使用虚拟机。它们允许您以访客身份运行任何操作系统。虚拟化软件（例如VirtualBox或VMWare Player）获得了广泛的报道。

Cygwin是不太受欢迎的解决方案。该软件不能在Windows上运行本机Linux应用程序，而是提供了大量为Windows编译的开源工具，这些工具提供的功能类似于Linux发行版。

虽然它实际上并没有在Windows上运行Linux软件，但也存在使用诸如SSH之类的协议的远程访问解决方案。

还有一种微软的方式。它称为“ Linux的Windows子系统”（WSL）。WSL是Windows 10的一项功能，可让您直接在Windows上运行本机Linux命令行工具，以及传统的Windows桌面和现代商店应用程序。

WSL针对希望在Windows上使用通用Linux工具链的Web开发人员。WSL提供了一个名为Bash.exe的应用程序，该应用程序打开一个运行Bash Shell的Windows控制台。使用Bash，您可以运行命令行Linux工具和应用程序。与完整的虚拟机相比，WSL需要更少的资源（CPU，内存和存储）。与虚拟机不同，您不需要分配资源。相反，WSL使用主机上可用的任何资源。

WSL有局限性。并非所有硬件资源在WSL中都可用。例如，不支持专用GPU，因此硬件加速不可行。并非所有Linux软件都能在WSL下完美运行。磁盘IO的速度不如本地Linux安装快，尽管在SSD上运行WSL会有所帮助。

对于许多人来说，WSL的最大问题是没有官方支持GUI桌面或应用程序。但是，如果将WSL与X服务器一起运行，则完全有可能使用WSL运行GUI应用程序。有一些适用于Windows 10的免费X服务器。我们一直在收到读者的反馈，有关X410是Windows 10的专有X服务器。

毫不奇怪，我们通常不会审查在Windows上运行的专有商业软件。这不是我们真正的领域。但是X410引起了我们的兴趣。这是我们对X410的看法。

#### 安装与配置

在安装X410之前，您需要有效地安装WSL。第一步是确保启用“ Linux的Windows子系统”可选功能。以管理员身份运行PowerShell，然后键入：

```
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```

然后重新启动计算机。

下一步是安装您选择的Linux发行版。使用Microsoft Store下载发行版（称为发行版）可能是最简单的。有相当多种发行版可供选择：Kali Linux，Ubuntu，Debian，openSUSE和SUSE Linux Enterprise。Arch Linux最近已添加到商店中。鉴于我最熟悉Ubuntu，因此选择了该发行版。

安装发行版后，可以从Microsoft Store安装X410。X410安装并运行后，最后一步是将DISPLAY环境变量设置为127.0.0.1:0.0。在bash中，键入：

```
export DISPLAY=127.0.0.1:0.0
```

然后，GUI应用程序将显示在X410中。默认情况下，没有声音。但是X410的开发人员已经编译了**[有用的指南](https://x410.dev/cookbook/wsl/enabling-sound-in-wsl-ubuntu-let-it-sing/)**，可以在WSL中启用声音。该指南易于遵循。

当您首次从商店安装Ubuntu / WSL时，它不包括任何与X Window相关的库或实用程序。我们建议在WSL中安装桌面环境，以便您充分体验真正的Linux GUI。

我选择了Xfce，这是一种流行的桌面环境，尽管还有更多的功能丰富的环境可用。请查看我们**[的桌面环境调查，](https://www.linuxlinks.com/survey-linux-desktop-environments/)**以了解其他替代方法。

要安装Xfce，请在WSL Shell中执行以下命令行。假设您使用的是Ubuntu / Debian，因为其他发行版使用了不同的打包软件。

```
$ sudo apt update && sudo apt -y upgrade`
`$ sudo apt install xfce4 xfce4-terminal
```

我们还建议创建一个批处理文件，以便自动启动X410，PulseAudio和Xfce。这是一个示例批处理文件，如果您使用其他桌面环境，则需要对其进行调整。我将批处理文件命名为“ start-ubuntu.bat”，存储在c：/ wsl中。

```
start /B x410.exe /desktop`
`start "" /B "C:\wsl\pulseaudio-1.1\bin\pulseaudio.exe"`
`#ubuntu1804.exe run "if [ -z \"$(pidof xfce4-session)\" ]; then export DISPLAY=127.0.0.1:0.0; export PULSE_SERVER=tcp:127.0.0.1; xfce4-session; pkill '(gpg|ssh)-agent'; taskkill.exe /IM x410.exe; taskkill.exe /IM pulseaudio.exe /F; fi;"
```

#### 运作中

X410提供了完整的桌面模式，使用传统的Linux桌面环境（例如Xfce）提供了完整的X Window桌面体验。

或者，您可以运行窗口化的应用程序，以便Linux GUI应用程序与Windows对应的应用程序并排出现。在窗口模式下，X410为Linux GUI应用程序使用其自己的窗口管理器，使您能够与Windows应用程序一起定位和调整应用程序的大小。

还有一个浮动桌面选项，其中X410显示为可调整大小的空白窗口，其中显示Linux GUI应用程序并将其限制在该窗口中。像完整桌面模式一样，您可以运行Linux桌面环境。

字体在所有模式下均呈现精美。

下图显示了浮动桌面模式下的X410。如果您熟悉Linux桌面，您将意识到该系统正在运行轻量级Xfce桌面环境。而且，桌面启动所需的时间不到三秒钟，速度之快令人难以置信。

![X410-Xfce](https://www.linuxlinks.com/wp-content/uploads/2019/05/X410-Xfce.jpg)

下图显示了在完全桌面模式下运行的X410。同样，桌面环境是Xfce。这次，该软件正在使用VLC媒体播放器播放1280×720的视频。我们还启动了终端机GIMP和LibreOffice Calc。当然，这些应用程序本身可用于Windows。但是，还有很多（实际上是很多）Linux GUI应用程序尚未移植到Windows，并且可能永远不会移植到Windows。即使本机Windows端口可用，它们也常常落后于Linux对应端口。

[![X410-全台式700](https://www.linuxlinks.com/wp-content/uploads/2019/05/X410-Full-Desktop-700.jpg)](https://www.linuxlinks.com/wp-content/uploads/2019/05/X410-Full-Desktop.jpg)点击图片查看图片的完整尺寸（2560×1440）

#### 性能

在性能方面，带有任何X服务器的WSL永远不会提供本机Linux X11服务器速度。但是，带有WSL的X410提供了非常好的性能，特别是如果您没有运行4K分辨率。延迟和渲染都非常好。X410中的桌面模式使用Direct3D。

请记住，将X410与WSL一起使用将消耗更多的CPU周期，特别是对于图形密集型软件（即使该软件很少/根本不使用硬件加速）。但是内存使用率很低。例如，以“窗口应用程序”模式启动X410时，它仅消耗约10MB的RAM。

作为渲染的指示，我们的经验是，只要您不尝试以非常高的分辨率全屏运行视频，视频播放就完美无缺。

我们已经使用WSL尝试了许多其他X服务器。X410的性能远远超过MobaXTerm，VcXsrc或Xming。其中，只有VcXsrc是开源软件。

#### 声音

WSL当前不支持声音设备。因此，当您在X410中打开GUI桌面或应用程序时，只会听到基本的系统铃声。但是，正如我们的安装部分所述，您可以使用PulseAudio来启动和运行声音。尽管只有预览二进制文件，但PulseAudio是已移植到Windows的声音系统。

播放视频时，音频回放效果不错，但偶尔出现故障时效果并不理想，尤其是在系统进行任何密集活动时。

#### 没有硬件加速

要记住的一件事是WSL和X410都不提供硬件加速。当您本机运行Linux时，X.Org服务器确实支持2D硬件加速。硬件加速是指将任务从CPU转移到其他更合适的设备/硬件。

许多桌面环境（和其他应用程序）将硬件加速用于其图形界面。因此，运行X410时，您需要相应地配置桌面环境，或使用不依赖硬件加速的桌面环境。否则，与桌面进行交互就感觉像是一触即发。

如果硬件加速对您很重要，则Oracle VM VirtualBox之类的虚拟化软件可能是更好的选择，因为该解决方案可为来宾应用程序提供3D图形和2D视频的硬件加速。

#### 其他特性

Windows托盘中添加了一个图标，其中提供了一个菜单，可以轻松在不同模式之间进行切换。

![X410托盘图标弹出菜单](https://www.linuxlinks.com/wp-content/uploads/2019/05/X410-tray-icon-popup-menu.png)

您会从菜单中看到DPI缩放比例。默认情况下，不应用DPI缩放。选择此选项后，X410会根据当前Windows显示设置自动缩放输出。如果您正在运行HiDPI监视器，或者您的X-Window应用程序不提供缩放选项，则此功能很有用。

X410在Windowed Apps模式下有两个DPI缩放选项：“默认”和“高质量”。“默认”选项使用快速的线性图像缩放算法，但输出模糊。“高质量”选项使用三次方算法并生成更清晰的输出，但需要更多的CPU周期。

X410仅允许环回网络连接来增强安全性。菜单选项还具有“公共访问”选项。此功能使您可以从本地虚拟机或受信任的远程计算机直接连接到X410。如果使用“公共访问”选项，则必须确保Windows防火墙限制了可以访问X410的主机。

X410使用X.Org代码，但不依赖Cygwin库。

#### 摘要

X410为无法在计算机上本机安装Linux（无论出于何种原因）并且想要运行Linux GUI应用程序而不必弄乱虚拟机的任何人提供了一个出色的解决方案。X410使您可以利用WSL的优势，并与Windows无缝集成。您将需要运行Windows 10。不支持旧版本的Windows。

在X服务器上花费49.99美元或40英镑左右可不是一笔小数目。但是，如果您想充分利用Windows上的Linux，X410绝对值得您进行调查。目前有80％的价格优惠。有15天免费试用，可提供全部功能。这足以让您评估该软件是否满足您的特定要求，而无需任何财务支出。

该软件通过Microsoft Store自动更新。它由Microsoft数字签名和认证。

注意，X410不仅适用于WSL。例如，您可以运行X410并通过SSH和X11转发连接到服务器。X410也可以与Windows的Docker无缝使用。

X410的开发人员还致力于使用Hyper-V套接字将X11从Hyper-V VM重定向到X410，而无需使用其TCP / IP堆栈来提供更好的解决方案。我们期待着这一发展的成果。

**网址：** [**x410.dev**](https://x410.dev/)
**价格：**通常为$ 49.99 [**/£41.74**](https://x410.dev/)。在发布时，该软件的价格降低了80％。
**支持：** [**Howto的**](https://x410.dev/cookbook/#wsl)
**开发人员：** Choung Networks
**许可证：**专有



