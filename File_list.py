import os
#import os.path
rootdir="E:\BaiduYunDownload"
#dll

"""
os.system(“net use z: \\192.168.0.6\zz”）
需要验证的共享文件夹映射操作方法
os.system('net use z: \\192.168.0.6\zz /user:admin /password:123')
"""

for parent,dirnames,filenames in os.walk(rootdir):
    """for dirname in dirnames:
        print("parent is :"+parent)
        print("dirname is :"+dirname)
        """
    for filename in filenames:
        if filename.find('.rar')!=-1:
            print(os.path.join(parent,filename))