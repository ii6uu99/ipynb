https://github.com/tillhoff/automated-deployment

# 自述文件

## 在Linux上安装

请确保首先以root用户身份运行prerequisites.sh文件。随后`ansible-playbook ubuntu_1804_hyperv_quickcreate.yml --ask-become-pass`以普通用户身份运行。有关总体配置的更多信息，请参见readme_linux.md。

## 在Windows上安装

Ansible未用于Windows主机部署，因为Ansible需要linux控制例程。因此，为了实现类似的工作方式，使用了powershell。

启动Powershell（不以管理员身份）并运行Set-ExecutionPolicy绕过-Scope Process -Force; ./windows_10.ps1

### 在Windows上做

- 字体安装：不再要检查字体名称，还要检查子类（常规，细等）。
- 在每个月份更改上，检查是否已设置值。