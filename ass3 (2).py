import tkinter as tk

class Canvas(tk.Canvas):
    def __init__(self, parent):
        super().__init__(parent)
        self.bind('<Button-1>', self.on_left_click)

    def on_left_click(self, event):
        self.create_oval(event.x - 2, event.y - 2, event.x + 2, event.y + 2, fill='orange')

class MainWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Canvas Example")
        self.canvas = Canvas(self.window)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.window.mainloop()

if __name__ == "__main__":
    MainWindow()
