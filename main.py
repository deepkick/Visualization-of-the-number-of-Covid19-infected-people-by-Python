import tkinter
import translate
from translate import translate
 
def btn_click():
    lang = str(translate(txt_1.get()))
    txt_2.insert(0, lang)
 
# 画面作成
tki = tkinter.Tk()
tki.geometry('300x300')
tki.title('翻訳機')
 
# ラベル
lbl_1 = tkinter.Label(text='英文:')
lbl_1.place(x=30, y=70)
lbl_2 = tkinter.Label(text='日本文:')
lbl_2.place(x=30, y=100)
 
# テキストボックス
txt_1 = tkinter.Entry(width=20)
txt_1.place(x=90, y=70)
txt_2 = tkinter.Entry(width=20)
txt_2.place(x=90, y=100)
 
# ボタン
btn = tkinter.Button(tki, text='翻訳', command=btn_click)
btn.place(x=140, y=170)
 
# 画面をそのまま表示
tki.mainloop()