import tkinter as tk

CELL_SIZE =40
ROWS =10
COLS=10

class EraserClass:

    def __init__(self,root):
        self.canvas = tk.Canvas(root, width=CELL_SIZE * COLS, height=CELL_SIZE * ROWS)
        self.canvas.pack()

        self.cell = []

        for row in range(ROWS):
           for col in range(COLS):

            x1 = COLS * CELL_SIZE
            y1 = ROWS * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE

            react = self.canvas.create_rectangle(x1,y1,x2,y2)
            self.cell.append(react)
    
        root.mainloop()
        




# import tkinter as tk

# CELL_SIZE = 40
# ROWS = 10
# COLS = 10

# class EraserCanvas:
#     def __init__(self, root):
#         self.canvas = tk.Canvas(root, width=CELL_SIZE * COLS, height=CELL_SIZE * ROWS)
#         self.canvas.pack()

#         self.cells = []
#         for row in range(ROWS):
#             for col in range(COLS):
#                 x1 = col * CELL_SIZE
#                 y1 = row * CELL_SIZE
#                 x2 = x1 + CELL_SIZE
#                 y2 = y1 + CELL_SIZE
#                 rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="white")
#                 self.cells.append(rect)

#         self.eraser = self.canvas.create_rectangle(0, 0, CELL_SIZE * 2, CELL_SIZE * 2, outline="red", width=2)
#         self.canvas.bind("<B1-Motion>", self.move_eraser)

    
# root.mainloop()
