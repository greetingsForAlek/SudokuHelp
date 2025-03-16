import tkinter as tk
from tkinter import messagebox

# Import the functions from the sudoku_helper.py script
from sudoku_helper import print_board, find_empty, is_valid, solve

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.create_board()
        self.create_buttons()

    def create_board(self):
        frame = tk.Frame(self.root)
        frame.pack()

        for i in range(9):
            for j in range(9):
                cell = tk.Entry(frame, width=2, font=('Arial', 18), justify='center')
                cell.grid(row=i, column=j, padx=1, pady=1)
                self.cells[i][j] = cell

    def create_buttons(self):
        frame = tk.Frame(self.root)
        frame.pack()

        solve_button = tk.Button(frame, text="Solve", command=self.solve_board)
        solve_button.pack(side=tk.LEFT, padx=5, pady=5)

        clear_button = tk.Button(frame, text="Clear", command=self.clear_board)
        clear_button.pack(side=tk.LEFT, padx=5, pady=5)

    def get_board(self):
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                value = self.cells[i][j].get()
                if value.isdigit() and 1 <= int(value) <= 9:
                    row.append(int(value))
                else:
                    row.append(0)
            board.append(row)
        return board

    def set_board(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    self.cells[i][j].delete(0, tk.END)
                    self.cells[i][j].insert(0, str(board[i][j]))
                else:
                    self.cells[i][j].delete(0, tk.END)

    def solve_board(self):
        board = self.get_board()
        if solve(board):
            self.set_board(board)
        else:
            messagebox.showerror("Error", "No solution exists for this Sudoku puzzle.")

    def clear_board(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, tk.END)