import tkinter as tk

# ウィンドウの作成
root = tk.Tk()
root.title("タスクリスト")
root.geometry("600x800")

# （新規作成されたら）メイン画面（水色）の作成
def create():
    pjFrame = tk.Frame(root, width=5oo, height=100, bg="alice blue")
    pjFrame.place(x=50, y=100)

# メニュー欄（ピンク）の作成
menu = tk.Frame(root, width=600, height=50,  bg="pink")
menu.place(x=0, y=0)
createButton = tk.Button(menu, width=10, height=1, text="新規作成", command=create)
createButton.place(x=100, y=10)
quitButton = tk.Button(menu, width=10, height=1, text="閉じる")
quitButton.place(x=400, y=10)




root.mainloop()