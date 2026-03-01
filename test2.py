import json
import tkinter as tk
from tkinter import ttk
import os

# JSON 読み込み
with open("sample.json", "r", encoding="shift_jis") as f:
    data = json.load(f)

# キー一覧（プルダウンに表示する項目）
keys = list(data.keys())

def on_select(event):
    selected_key = combo.get()
    selected_value = data[selected_key]
    print("選択されたキー:", selected_key)
    print("対応する値:", selected_value)

    # 例：PDF を開く（Windows）
    if os.path.exists(selected_value):
        os.startfile(selected_value)
    else:
        print("ファイルが見つかりません:", selected_value)

# GUI 作成
root = tk.Tk()
root.title("JSON プルダウンツール")
root.geometry("400x150")

label = tk.Label(root, text="項目を選択してください：")
label.pack(pady=10)

combo = ttk.Combobox(root, values=keys, state="readonly", width=40)
combo.pack()

combo.bind("<<ComboboxSelected>>", on_select)

root.mainloop()
