from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from os.path import realpath

def new_file(event=None):
    global file_name
    file_name = "Untitled"
    root.title(file_name)
    content_text.delete(1.0, END)   

def open_file(event=None):
    global file_name
    #input_file_name = askopenfilename(defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    input_file_name = askopenfilename()
    print(input_file_name)
    if input_file_name:
        root.title(realpath(input_file_name))
        content_text.delete(1.0, END)
        with open(input_file_name) as the_file:
            content_text.insert(1.0, the_file.read())
            file_name = input_file_name

def write_to_file(output_file_name):
    try:
        content = content_text.get(1.0, 'end')
        with open(output_file_name, 'w') as the_file:
            the_file.write(content)
    except IOError:
        pass

def save_as(event=None):
    global file_name
    #input_file_name = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    input_file_name = asksaveasfilename()
    if input_file_name:
        write_to_file(input_file_name)
        root.title(realpath(input_file_name))
        file_name = input_file_name

def save(event=None):
    global file_name
    if file_name == "Untitled":
        save_as() 
    else:
        write_to_file(file_name)

root = Tk()
root.geometry('500x250')
file_name = "Untitled"
root.title(file_name)
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='New',
                      accelerator='Ctrl+N',
                      command=new_file)
file_menu.add_command(label='Open',
                      accelerator='Ctrl+O',
                      command=open_file)
file_menu.add_command(label='Save',
                      accelerator='Ctrl+S',
                      command=save)
file_menu.add_command(label='Save as',
                      accelerator='Shift+Ctrl+S',
                      command=save_as)
menu_bar.add_cascade(label='File', menu=file_menu)
content_text = Text(root,
                    font=['Courier', 18],
                    wrap='word')
content_text.pack()
root.config(menu=menu_bar)
root.mainloop()
