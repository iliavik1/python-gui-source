import tkinter as tk

root = tk.Tk()

root.geometry("1000x500")
root.title("hi")
label = tk.Label(root, text="hi this is my first program on python", font=('Arial', 18))
label.pack(padx=30, pady=30)
label1 = tk.Label(root, text="this is made for github by iliavik1", font=('Arial', 30))
label1.pack(padx=30, pady=30)
root.mainloop()



print("hi")