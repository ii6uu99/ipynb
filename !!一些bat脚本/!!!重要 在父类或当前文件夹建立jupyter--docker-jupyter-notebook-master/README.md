

https://github.com/dirkarnez/docker-jupyter-notebook

# docker-jupyter-notebook

### 安装套件

- 康达

  ```
  import sys
  !conda install --yes --prefix {sys.prefix} numpy
  ```

- 点子

  ```
  import sys
  !{sys.executable} -m pip install numpy
  ```

- 参考

  - https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/