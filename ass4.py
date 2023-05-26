import tkinter as tk

class Canvas(tk.Canvas):
    def __init__(self, parent):
        super().__init__(parent)
        self.bind('<Button-1>', self.on_left_click)
        self.shape = None
        self.points = []

    def on_left_click(self, event):
        if self.shape is not None:
            self.points.append(event.x)
            self.points.append(event.y)
            if len(self.points) == 6:
                if self.shape == 'rectangle':
                    self.draw_rectangle()
                elif self.shape == 'triangle':
                    self.draw_triangle()

    def draw_rectangle(self):
        x1, y1, x2, y2, x3, y3 = self.points
        self.create_rectangle(x1, y1, x3, y3, outline='red')
        self.points = []

    def draw_triangle(self):
        x1, y1, x2, y2, x3, y3 = self.points
        self.create_polygon(x1, y1, x2, y2, x3, y3, outline='blue')
        self.points = []

class MainWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Canvas Example")

        self.canvas = Canvas(self.window)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.rect_button = tk.Button(self.window, text='Rectangle', command=self.on_rect_button)
        self.rect_button.pack(side=tk.LEFT)

        self.tri_button = tk.Button(self.window, text='Triangle', command=self.on_tri_button)
        self.tri_button.pack(side=tk.LEFT)

        self.window.mainloop()

    def on_rect_button(self):
        self.canvas.shape = 'rectangle'

    def on_tri_button(self):
        self.canvas.shape = 'triangle'

if __name__ == "__main__":
    MainWindow()
