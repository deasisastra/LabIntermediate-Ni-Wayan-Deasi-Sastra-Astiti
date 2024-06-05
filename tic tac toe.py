# Import modul
import tkinter as tk
from tkinter import messagebox

# Definisi class "Tic Tac Toe"
class TicTacToe:
    # Inisialisasi (__init__ method):
    def __init__(self, size):
        # Atribut class
        self.size = size
        self.board = [" " for _ in range(size * size)]
        self.turn = "X"

        # Inisialisasi GUI (Graphical User Interface)
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.buttons = []

        # Membuat Tombol
        for i in range(size):
            row = []
            for j in range(size):
                button = tk.Button(self.window, text=" ", font=("Arial", 24), width=4, height=2,
                                   command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

# Metode on_button_click:
    def on_button_click(self, row, col):
        # Validasi Klik
        position = row * self.size + col
        if self.board[position] != " ":
            messagebox.showerror("Invalid move", "This position is already taken. Try again.")
            return

# Update papan dan UI
        self.board[position] = self.turn
        self.buttons[row][col].config(text=self.turn)

# Cek Pemenang
        winner = self.check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            self.reset_game()
            return

# Cek Seri
        if all(cell != " " for cell in self.board):
            messagebox.showinfo("Game Over", "The game is a tie!")
            self.reset_game()
            return

# Ganti Giliran
        self.turn = "O" if self.turn == "X" else "X"

# Metode check_winner:
    def check_winner(self):
    # Cek Baris dan Kolom:
        for i in range(self.size):
            if all(self.board[i * self.size + j] == self.turn for j in range(self.size)):
                return self.turn
            if all(self.board[j * self.size + i] == self.turn for j in range(self.size)):
                return self.turn

    # Cek Diagonal
        if all(self.board[i * (self.size + 1)] == self.turn for i in range(self.size)):
            return self.turn
        if all(self.board[(i + 1) * (self.size - 1)] == self.turn for i in range(self.size)):
            return self.turn

        # Tidak ada pemenenang
        return None

# Metode reset_game:
    def reset_game(self):
        # Reset Data dan UI:
        self.board = [" " for _ in range(self.size * self.size)]
        for row in self.buttons:
            for button in row:
                button.config(text=" ")

# Metode run:
# metode ini menjalankan aplikasi GUI
    def run(self):
        self.window.mainloop()


# Main Program
if __name__ == "__main__":
    size = int(input("Enter the size of the board (N for NxN): "))
    game = TicTacToe(size)
    game.run()
# Game tic tac toe akan muncul pada pop up window baru