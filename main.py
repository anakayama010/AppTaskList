
import tkinter as tk
from tkinter import messagebox

# ウィンドウの作成
root = tk.Tk()
root.title("タスクリスト")
root.geometry("600x800")


class Project:
    
	name = ""

	def __init__(self):
		self.name = Create()

	def get_name(self):
		return self.name

	def set_name(self, name):
		self.name = name

class AskProjectName:

	name = ""
	bl = False

	@staticmethod
	def naming(self):
		self.name = self.entry.get()
		self.bl = True

	# 各種ウィジェットの作成
	frame = tk.Frame(root, width=600, height=400, bg="alice blue",padx=60, pady=30)
	entry = tk.Entry(frame)	
	entry.insert(tk.END,"新しいプロジェクト")# Entryウィジェットへ文字列をセットしておく
	label = tk.Label(frame, text = "入力してください。", bg="alice blue")
	button_execute = tk.Button(frame, text="作成", command=naming)

	def __init__(self):
		# 各種ウィジェットの設置
		self.frame.pack()
		self.label.pack()
		self.entry.pack()
		self.button_execute.pack()
	
	def get_name(self):
		return self.name
	
	def destroy_widget(self):
		self.frame.destroy()
		self.label.destroy()
		self.entry.destroy()
		self.button_execute.destroy()

class CreateProject:
	frame = tk.Frame(root, width=500, height=300, bg= "pink", padx=50, pady=50)
	label = tk.Label(frame)
	canvas = tk.Canvas(frame, width=300, height=300, bg="yellow")

	def __init__(self, p_name):
		self.frame.pack(anchor=tk.N)
		self.label = tk.Label(self.frame, text=p_name)
		self.label.pack(anchor=tk.W)
		self.canvas.pack(anchor=tk.W)
	
	

# メニューから呼び出される関数
def create_project():
	p = AskProjectName()
	while p.bl:
		p_name = p.get_name()
		p.destroy_widget()
		CreateProject(p_name)
		break
	
	
	
	

	

def close_disp():
    pass

# メニューバー作成
men = tk.Menu(root)
# メニューバーを画面にセット
root.config(menu=men)
# メニューに親メニュー（ファイル）を作成する
menu_file = tk.Menu(root)
men.add_cascade(label='ファイル', menu=menu_file)
# 親メニューに子メニュー（開く・閉じる）を追加する
menu_file.add_command(label='新規作成', command=create_project)
menu_file.add_separator()
menu_file.add_command(label='閉じる', command=close_disp)



root.mainloop()
