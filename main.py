import tkinter as tk
import tkinter.simpledialog as simpledialog

class Project:
    
	name = "新規プロジェクト"

	#コンストラクタ
	def __init__(self):
		self.name = "新規プロジェクト"
	
    #コンストラクタ
	def __init__(self, name):
		self.name = name
        
	# 名称変更メソッド
	def rename(self, name):
		self.name = name
		print("プロジェクト名を" + name + "に変更しました。")


# 名称変更のためのポップアップを表示する
def input_name_window():
	
	input = tk.Tk()
	input.geometry('400x150')
	input.title('window')
	input.lift()
	
	lbl = tk.Label(input, text='名称を入力してください。')
	lbl.place(x=30, y=50)
	txt = tk.Entry(input, width=30)
	txt.place(x=30, y=80)
	btn = tk.Button(input, text='作成', bg='gray', fg='white', width=10)
	btn.place(x=250, y=75)

	input.mainloop()
	


	

#project_name = simpledialog.askstring('dialogbox', 'プロジェクト名を入力してください。')
project_name = input_name_window()

root = tk.Tk()
root.geometry('600x400')
root.title(project_name)

root.mainloop()



