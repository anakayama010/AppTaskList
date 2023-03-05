# テキストボックスに入力されている文字列を取得して、メッセージを表示する

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

# 関数namingの定義
def naming():
    messagebox.showinfo("入力内容", "新規プロジェクト名：" + entry.get())


# ウィンドウの作成
root = tk.Tk()
root.title("文字列の取得・クリア")
root.geometry("600x800")

# フレームの作成と配置
frame = ttk.Frame(root) #rootウィンドウにフレームを作成
frame.grid(column=0, row=0, sticky=tk.NSEW, padx=5, pady=10)

# 各種ウィジェットの作成
label = ttk.Label(frame, text = "入力してください。")
entry = ttk.Entry(frame)
button_execute = ttk.Button(frame, text="作成", command=naming)

# 各種ウィジェットの設置
label.grid(row=0, column=0)
entry.grid(row=0, column=1)
button_execute.grid(row=1, column=1)

# Entryウィジェットへ文字列をセットしておく
entry.insert(tk.END,"新しいプロジェクト")

root.mainloop()