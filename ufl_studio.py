import tkinter as tk
from tkinter import filedialog, messagebox

def evaluate_expression(expr, variables):
    try:
        return eval(expr, {}, variables)
    except Exception as e:
        raise e

def process_line(line, variables, gui_elements):
    try:
        if line.startswith('let '):
            parts = line.split(' ')
            var_name = parts[1]
            var_value = evaluate_expression(parts[3], variables)
            variables[var_name] = var_value
        elif line.startswith('say("') and line.endswith('")'):
            text = line.split('("')[1].split('")')[0]
            gui_elements['output'].insert(tk.END, text + "\n")
        elif line.startswith('button("') and line.endswith('")'):
            button_text = line.split('("')[1].split('")')[0]
            button = tk.Button(gui_elements['buttons_frame'], text=button_text, command=lambda bt=button_text: on_button_click(bt, gui_elements))
            button.pack(side=tk.LEFT)
        elif line.startswith('ifthis '):
            condition = line.split(' ')[1]
            if evaluate_expression(condition, variables):
                return True
        elif line.startswith('orelse'):
            return False
        elif line.startswith('initializeWindow'):
            initialize_window(gui_elements['root'])
        elif line.startswith('setTheme'):
            theme = line.split('(')[1].split(')')[0].strip('"')
            set_theme(gui_elements['root'], theme)
    except Exception as e:
        raise e

def initialize_window(root):
    root.geometry("300x400")
    root.title("UFL Studio")

def set_theme(root, theme):
    if theme == 'dark':
        root.configure(bg='black')
    elif theme == 'light':
        root.configure(bg='white')

def on_button_click(text, gui_elements):
    gui_elements['output'].insert(tk.END, f"Button {text} clicked\n")
    # Additional logic for button click handling can be added here

def interpret_ufl(file_path, gui_elements):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    variables = {}

    for line in lines:
        process_line(line.strip(), variables, gui_elements)

def browse_file(gui_elements):
    file_path = filedialog.askopenfilename(filetypes=[("UFL files", "*.ufl")])
    if file_path:
        interpret_ufl(file_path, gui_elements)

def main():
    root = tk.Tk()
    root.title("UFL Studio")
    root.geometry("400x200")

    file_frame = tk.Frame(root)
    file_frame.pack(pady=10)

    file_label = tk.Label(file_frame, text="<ufl filename>")
    file_label.pack(side=tk.LEFT, padx=5)

    browse_button = tk.Button(file_frame, text="Browse", command=lambda: browse_file(gui_elements))
    browse_button.pack(side=tk.LEFT, padx=5)

    launch_button = tk.Button(root, text="Launch", command=lambda: interpret_ufl(file_label.cget("text"), gui_elements))
    launch_button.pack(pady=10)

    gui_elements = {
        'root': root,
        'output': tk.Text(root, height=10),
        'buttons_frame': tk.Frame(root)
    }

    gui_elements['output'].pack()
    gui_elements['buttons_frame'].pack()

    root.mainloop()

if __name__ == "__main__":
    main()
