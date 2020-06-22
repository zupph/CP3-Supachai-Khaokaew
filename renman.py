from tkinter import *
from tkinter import filedialog


def file_dialog(event):
    file_dialog = filedialog.askdirectory()
    file_text.delete(0, END)
    file_text.insert(0, file_dialog)


main_window = Tk()
main_window.geometry('800x600')

file_text = Entry(main_window, width=50)
file_text.place(x=5, y=5)
file_button = Button(main_window, width=1, height=1, text="...")
file_button.place(x=420, y=5)
file_button.bind("<Button-1>", file_dialog)
frame = Frame(main_window)
frame.place(x=5, y=50)
listbox = Listbox(frame, width=50, height=20)
listbox.pack(side=LEFT, fill=Y)
scrollbar = Scrollbar(frame, orient="vertical")
scrollbar.pack(side=RIGHT, fill=Y)

for i in range(100):
    listbox.insert(END, i)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

main_window.mainloop()
