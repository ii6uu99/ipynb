#window使用右斜杠 (\)
# linux是用左斜杠 (/)

import os

os.path.join('usr', 'bin', 'spam') 
# >> Prints 'usr\\bin\\spam        --- ( 双反斜杠将转义前一个斜杠 .)

＃您可以使用os.path.join在列表中创建文件名字符串。
myFiles - ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
	print(os.path.join('C:\\Users\\YourName', filename))
# >> C:\\Users\YourName\accounts.txt
# >> C:\\Users\YourName\details.csv
# >> C:\\Users\YourName\invite.docx

＃您甚至可以使用os.getcwd（）来获取当前的工作目录
os.getcwd()
# >> C:\\Python36

＃甚至更改目录
os.chdir('C:\\Windows\System32')
# >> Now you're in C:\\Windows\\System32

＃您可能已经猜到了-我们也可以创建目录。
os.makedirs('C:\\secretfiles\\supersecretfiles\\totallynotporn')


"""  查找文件的大小以及文件夹的内容 . """

os.path.getsize(path_here) # 以字节为单位返回文件的大小（由path_name替换） .

os.listdir(path) 
＃返回path参数中每个文件的文件名STRINGS列表。

＃如果要获取整个目录的总大小，可以通过将两者合并
## getsize() and listdir() 一起，在循环的帮助下
totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'): #您应该考虑删除此目录，以节省空间\ s 
	totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))

print(totalSize) # >> 3129873 bytes 

#使用此模块，我们还可以检查路径或文件是否存在。这是巨大的，因为最终会有大量的Python函数
##因尝试向他们提供不存在的路径而导致错误崩溃。

 # returns TRUE if the file or folder placed in the argument exists, and FALSE if not.
os.path.exits(path) #如果放置在参数中的文件或文件夹存在，则返回TRUE，否则返回FALSE。

os.path.isfile(path) 
#如果path参数存在并且是文件，则＃将返回TRUE，否则返回FALSE。

os.path.isdir(path) #如果path参数存在并且是文件夹，则将返回TRUE，否则将返回FALSE 


# 如果我们将这些功能放入外壳中 : 
os.path.exists('C:\\Windows')
# >>>>>> True
os.path.exists('C:\\Not_System_32')
# >>>>>> False
os.isdir('C:\\Windows\\System32')
# >>>>>> True
os.isfile('C:\\Windows\\System32')
# >>>>>> False
os.isdir('C:\\Windows\\System32\\calc.exe')
# >>>>>> False
os.path.isfile('C:\\Windows\\System32\\calc.exe')
# >>>>>> True

# 您甚至可以检查系统上是否装有CD驱动器，甚至还可以检查USB记忆棒。 

os.path.exists('D:\\')
# >>>>>> False/True


""" FILE READING AND WRITING """
＃一旦您习惯于处理文件夹和路径，我们就可以指定要读取/写入的位置。
##以下示例暂时仅处理PLAINTEXT文件-表示文件扩展名为.txt或.py
###如果您尝试打开其他类型的二进制文件（对于那些对自己的ge感到困惑的文件，这是我的意思，是的。）
＃＃＃＃ 继续。如果您尝试打开其他文件，则会看到编码混乱。稍后再处理。 

""" There's THREE steps to reading or writing files in Python. """
“”“使用Python读取或写入文件需要三个步骤。”“”
# 1. Call the open() function to return a FILE object.
＃1.调用open（）函数以返回FILE对象。
# 2. Call the read() or write() method ON the FILE object.
＃2.在FILE对象上调用read（）或write（）方法。
＃3.通过在FILE对象上调用close（）方法关闭文件。 

"""			OPENING FILES WITH open() 		"""
# In order to open a file with the open() function, we need to pass it a string path, indicating the file we want open
＃为了使用open（）函数打开文件，我们需要向其传递一个字符串路径，指示要打开的文件ed.
## 然后，这将返回一个FILE对象。我已经在名为secretmessage.txt的文档中创建了一个.txt文档。在Python IDLE中： 

secretFile = open('C:\\Users\\Documents\\secretmessage.txt')
# If you're using Linux/OsX:
secretFile = open('/Users/home_folder_here/secretmessage.txt')

＃这两个命令都将以“读取明文”模式打开文件。这使您可以从文件中读取数据，但不能
##以任何方式写入或修改文件。这是默认模式，但是您可以通过传递第二秒钟来明确指定模式
您的open（）函数的###参数如下所示： 
secretFile = open('C:\\Users\\Documents\\secretmessage.txt', 'r')
＃这与前者相同。

＃通过调用open（），这将返回一个FILE对象。该对象在python中存储为“值”，因此为什么我们将其存储在var中 
""" READING THE CONTENTS OF FILES """
＃现在我们有了FILE对象，我们可以开始读取其内容了。如果我们想读取文件的全部内容
##作为STRING值，我们可以使用FILE对象的read（）方法。因此，在之前的代码之上，我们将调用：
secretMessage = secretFile.read() # 将read（）函数传递给新值，然后我们将该值称为 
secretMessage
# >>>>>>>>>>>> 'wang'			# hah. My message said wang
＃或者，我们可以使用readlines（）方法获取字符串值的LIST。每行文本一个字符串。

＃如果我们要写入到我们以读取模式打开的文件-我们不能。我们需要以“写明文”模式打开它，或者
##'附加明文'。 （'w'，'a'）

＃写模式-覆盖现有文件并从头开始。就像我们覆盖变量一样。
＃APPEND MODE-将文本添加到文件末尾。

＃如果不存在通过OPEN（）的文件名：'w'和'a'都将创建一个新的空白文件。
##完成读写文件后，在再次打开文件之前调用close（）方法。 