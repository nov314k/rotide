from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import askyesno
from os.path import realpath

def new_file(event=None):
    global file_name
    file_name = "Untitled"
    root.title(file_name)
    content_text.delete(1.0, END)
    clear_status_bar()

def open_file(event=None):
    global file_name
    #input_file_name = askopenfilename()
    input_file_name = askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if input_file_name:
        root.title(realpath(input_file_name))
        content_text.delete(1.0, END)
        with open(input_file_name) as the_file:
            content_text.insert(1.0, the_file.read())
            file_name = input_file_name
        clear_status_bar()

def write_to_file(output_file_name):
    try:
        content = content_text.get(1.0, END)
        with open(output_file_name, 'w') as the_file:
            the_file.write(content)
    except IOError:
        pass

def save(event=None):
    global file_name
    if file_name == "Untitled":
        save_as() 
    else:
        write_to_file(file_name)
    clear_status_bar()

def save_as(event=None):
    global file_name
    #input_file_name = asksaveasfilename()
    input_file_name = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if input_file_name:
        write_to_file(input_file_name)
        root.title(realpath(input_file_name))
        file_name = input_file_name

def exit_editor(event=None):
    global content_changed
    if content_changed:
        if askyesno("Quit", "Save the file?"):
            save()
            root.destroy()
        else:
            root.destroy()
    else:
        root.destroy()
    
def clear_status_bar():
    global content_changed
    content_changed = False
    status_bar.config(state='normal')
    status_bar.delete('1.0', END)
    status_bar.insert('1.0', 'github.com/novakpetrovic/rotide')
    status_bar.config(state='disabled')
    
def on_content_changed(event=None):
    global content_changed
    content_changed = True
    status_bar.config(state='normal')
    status_bar.delete('1.0', END)
    status_bar.insert('1.0', 'FILE CHANGED')
    status_bar.config(state='disabled')

# Root
root = Tk()
root.geometry('500x250')
file_name = "Untitled"
content_changed = False
root.title(file_name)
# Menu bar 1
menu_bar = Menu(root)
# File menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='New',
                      accelerator='Ctrl+N',
                      underline=0,
                      command=new_file)
file_menu.add_command(label='Open',
                      accelerator='Ctrl+O',
                      underline=0,
                      command=open_file)
file_menu.add_command(label='Save',
                      accelerator='Ctrl+S',
                      underline=0,
                      command=save)
file_menu.add_command(label='Save as',
                      accelerator='Shift+Ctrl+S',
                      underline=5,
                      command=save_as)
file_menu.add_command(label='Exit',
                      accelerator='Ctrl+Q',
                      underline=1,
                      command=exit_editor)
# Menu bar 2
menu_bar.add_cascade(label='File',
                     underline=0,
                     menu=file_menu)
# Icons bar
new_file_icon = PhotoImage(file='icons/new_file.gif')
open_file_icon = PhotoImage(file='icons/open_file.gif')
save_file_icon = PhotoImage(file='icons/save.gif')
exit_editor_icon = PhotoImage(file='icons/exit_editor.gif')
shortcut_bar = Frame(root, height=25)
shortcut_bar.pack(fill='x')
icons = ('new_file', 'open_file', 'save', 'exit_editor')
for i, icon in enumerate(icons):
    tool_bar_icon = PhotoImage(file='icons/{}.gif'.format(icon))
    cmd = eval(icon)
    tool_bar = Button(shortcut_bar, image=tool_bar_icon, command=cmd)
    tool_bar.image = tool_bar_icon
    tool_bar.pack(side='left')
# Content text
content_text = Text(root,
                    height=6,
                    font=['Courier', 18],
                    wrap='word')
content_text.pack(fill='both',
                  expand='y')
content_text.focus()
# Status bar
status_bar = Text(root,
                  height=1,
                  takefocus=0,
                  border=1,
                  background='khaki',
                  state='disabled',
                  wrap='none')
status_bar.pack(fill='x')
clear_status_bar()
# Configure menu bar
root.config(menu=menu_bar)
# Bind keyboard shortcuts
content_text.bind('<Control-N>', new_file)
content_text.bind('<Control-n>', new_file)
content_text.bind('<Control-O>', open_file)
content_text.bind('<Control-o>', open_file)
content_text.bind('<Control-S>', save)
content_text.bind('<Control-s>', save)
content_text.bind('<Control-Q>', exit_editor)
content_text.bind('<Control-q>', exit_editor)
content_text.bind('<Any-KeyPress>', on_content_changed)
# Start the main loop
root.mainloop()
# TODO Bind root window X to exit_editor()
# TODO Change from icons to capital letters, so that we don't need to carry icons around?