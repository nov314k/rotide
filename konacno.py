from tkinter import *
from tkinter.filedialog import *

PROGRAM_NAME = "4edI"

def new_file(event=None):
    global file_name
    file_name = "Untitled"
    root.title("Untitled")
    content_text.delete(1.0, END)
    

def open_file(event=None):
    global file_name
    input_file_name = askopenfilename(defaultextension=".txt",
                                      filetypes=[
                                          ("Text Documents", "*.txt"),
                                          ("All Files", "*.*")])
    if input_file_name:
        file_name = input_file_name
        root.title('{} - {}'.format(os.path.basename(file_name),
                                    PROGRAM_NAME))
        content_text.delete(1.0, END)
        with open(file_name) as _file:
            content_text.insert(1.0, _file.read())
            

def write_to_file(file_name):
    try:
        content = content_text.get(1.0, 'end')
        with open(file_name, 'w') as the_file:
            the_file.write(content)
    except IOError:
        pass
    

def save_as(event=None):
    global file_name
    input_file_name = asksaveasfilename(
                        defaultextension=".txt",
                        filetypes=[("Text Documents", "*.txt"),
                                   ("All Files", "*.*")])
    if input_file_name:
        file_name = input_file_name
        write_to_file(file_name)
        root.title('{} - {}'.format(os.path.basename(file_name),
                                    PROGRAM_NAME))
    return "break"
    

def save(event=None):
    global file_name
    if file_name == "Untitled":
        save_as() 
    else:
        write_to_file(file_name)
    return "break"


root = Tk()
root.geometry('500x250')
file_name = "Untitled"
root.title(file_name + " - " + PROGRAM_NAME)
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


