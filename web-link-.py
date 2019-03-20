import chardet
from urllib import parse,request
from html.parser import HTMLParser
from tkinter import *
from datetime import datetime
import tkinter.messagebox as messagebox
url=[]
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag=='a':
             if len(attrs) > 0:
                 #print(attrs)
                 if 'href' in attrs[0]:
                     #print(attrs[0][1])
                     for i in attrs[0]:
                        url.append(i)

def xmlDefend(name):
    req=request.Request(name)
    html=request.urlopen(req,timeout=5).read()
    # print(html.decode("gbk"))
    cha=chardet.detect(html)
    parser=MyHTMLParser()
    parser.feed(html.decode(cha['encoding']))
a=1
class   App(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWifght()
    def createWifght(self):
        self.namePut=Entry(self)
        self.namePut.pack()
        self.hellos=Label(self,text='输入地址进行解析')
        self.hellos.pack()
        self.alertbutton=Button(self,text='开始解析',command=self.hello)
        self.alertbutton.pack()
        self.button=Button(self,text='查看数据',command=self.jx)
        self.button.pack()
        self.button_1=Button(self,text='保存数据',command=self.save)
        self.button_1.pack()
    def jx(self):
        messagebox.showinfo('解析结果',url[1::2])
    def hello(self):
        name='http://'+self.namePut.get()
        if len(name)>10:
          xmlDefend(name)
          messagebox.showinfo('反馈','解析完毕')
        else:
         messagebox.showinfo('没有输入解析地址','请输入解析地址')
    def save(self):
        with open(str(self.namePut.get())[0:15]+'网站链接解析.txt','w') as f:
            for i in url[1::2]:
                f.write(i+'\n')
        messagebox.showinfo('','保存完毕，已保存在当前目录下')

# with open('解析地址.txt','w') as f:
#     for i in url:
#       f.write(i+'\n')
# print(url)
app=App()
app.master.title('刻骨铭心网站链接解析')
app.mainloop()
