#! python3
# searchfile.py 通过遍历电脑上的所有文件形成一个列表，在列表中搜索我们想要查找的文件。-shy

#----设计基本框架----
import os
import tkinter
import tkinter.messagebox
win=tkinter.Tk()
win.geometry("800x600")
win.title("文件查找")

#-----设计功能函数----
var_filename=tkinter.StringVar()
var_filename.set('')
name=var_filename.get()
file_db=[]

def scan():
    print("正在初始化...")
    for url in ("C:\\","D:\\", "E:\\", "F\\", "G:\\", "H:\\"):   # 如果有更多磁盘，可以继续添加
        for root, dirs, files in os.walk(url):
            for file in files:
                file_db.append(os.path.join(root, file))
    tkinter.messagebox.showinfo(title='初始化',message='初始化完成')

def find():
    new_file_db = []
    name=var_filename.get()
    for file in file_db:
        if name in file:
            new_file_db.append(file)
    for num, add_new_file in enumerate(new_file_db):
        print(num+1, add_new_file)
        winoutputname.insert("insert",num+1)
        winoutputname.insert("insert",':')
        winoutputname.insert("insert",add_new_file)
        winoutputname.insert("insert",'\n')
    if new_file_db==[]:
        tkinter.messagebox.showinfo(title='提醒',message='未找到文件')

def cancel():
    var_filename.set('')
    winoutputname.delete("1.0","end")

#----设计提示标签、输入框和按钮----
#设计提示标签
labfilename=tkinter.Label(win,text='文件名称',width=80)
labinputname=tkinter.Label(win,text='输出结果',width=80)
labbeizhu=tkinter.Label(win,text='备注：请先点击初始化，等初始化完成后，再输入文件名称进行搜索',font=("黑体",17),fg="red")
labbeizhu2=tkinter.Label(win,text='备注：只需在程序运行之前初始化一次，后续查找文件无需再初始化',font=("黑体",17),fg="red")
#设计输入框
entfilename=tkinter.Entry(win,width=200,textvariable=var_filename)
#设计输出框
winoutputname=tkinter.Text(win,width=200,height=300)
#设计3个按钮
but_scan=tkinter.Button(win,text='初始化',command=scan)
but_find=tkinter.Button(win,text='查找',command=find)
but_cancel=tkinter.Button(win,text='重置',command=cancel)


#----设计组件布局----
labfilename.place(x=20,y=10,width=80,height=20)
labinputname.place(x=20,y=180,width=80,height=20)
entfilename.place(x=120,y=10,width=200,height=20)
winoutputname.place(x=120,y=40,width=600,height=300)
but_scan.place(x=140,y=380,width=50,height=20)
but_find.place(x=240,y=380,width=50,height=20)
but_cancel.place(x=340,y=380,width=50,height=20)
labbeizhu.place(x=20,y=420)
labbeizhu2.place(x=20,y=460)

win.mainloop()    #进入消息循环