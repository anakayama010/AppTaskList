# テキストボックスに入力されている文字列を取得して、メッセージを表示する

import tkinter as tk
from tkinter import messagebox

# 関数namingの定義
def naming():
    messagebox.showinfo("入力内容", "新規プロジェクト名：" + entry.get())


# ウィンドウの作成
root = tk.Tk()
root.title("文字列の取得・クリア")
root.geometry("600x800")

# フレームの作成と配置
frame = tk.Frame(
    root, width=600, height=400, bg="alice blue",padx=60, pady=30
) 
#frame.grid(column=0, row=0, sticky=tk.NSEW, padx=5, pady=10)
frame.pack()

# 各種ウィジェットの作成
label = tk.Label(frame, text = "入力してください。", bg="alice blue")
entry = tk.Entry(frame)
button_execute = tk.Button(frame, text="作成", command=naming)

# 各種ウィジェットの設置
#label.grid(row=0, column=0)
#entry.grid(row=0, column=1)
#button_execute.grid(row=1, column=1)
label.pack()
entry.pack()
button_execute.pack()

# Entryウィジェットへ文字列をセットしておく
entry.insert(tk.END,"新しいプロジェクト")

root.mainloop()