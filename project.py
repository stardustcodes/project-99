import shutil
import os

a=os.listdir('C:/Users/Dell/OneDrive/Desktop/my files/work/coding stuff/Python/Backup/folder')
print(a)

for g in a:
    h=os.path.splitext(g)
    if h[1]=='.py':
        source='C:/Users/Dell/OneDrive/Desktop/my files/work/coding stuff/Python/Backup/folder/' + g
        destination='C:/Users/Dell/OneDrive/Desktop/my files/work/coding stuff/Python/Backup/python/'
        shutil.move(source, destination)
    elif h[1]=='.txt':
        source='C:/Users/Dell/OneDrive/Desktop/my files/work/coding stuff/Python/Backup/folder/' + g
        destination='C:/Users/Dell/OneDrive/Desktop/my files/work/coding stuff/Python/Backup/text/'
        shutil.move(source, destination)
