import os
import pyperclip


temp=pyperclip.paste()

num=10
while True:
    tit=input('请输入题目:\n')
    input('请输入内容')
    con=pyperclip.paste().split('?')[0]
    with open('Vidoe %d.rst' %num,'w',encoding='utf-8') as f:
        con=temp.replace('Name',tit).replace('lianjie',con)
        f.write(con)
    num=num+1


