import tkinter as tk

root = tk.Tk()

root.geometry("1000x500")
root.title("hi")
label = tk.Label(root, text="hi this is my first program on python", font=('Arial', 18))
label.pack(padx=30, pady=30)
root.mainloop()



print("hi")