# 2048 game

# Importing necessary modules
import tkinter as tk
import random
from tkinter import ttk
from tkinter import messagebox

# Creating GUI application with ttk and forest-dark theme
window = tk.Tk()
style = ttk.Style(window)
window.title("2048")
window.tk.call("source", "forest-dark.tcl")
style.theme_use("forest-dark")
style_cell = ttk.Style()

# Function to handle key press events


def on_key_press(event):
    if event.keysym == "Up":
        move_up()
    elif event.keysym == "Down":
        move_down()
    elif event.keysym == "Right":
        move_right()
    elif event.keysym == "Left":
        move_left()

# function to handle key prees 'Up'


def move_up():
    valid_numbers, board = find_numbers_index()
    for col in range(4):
        calculate_list = []
        calculate_list_index = []
        for row in range(4):
            if (row, col) in valid_numbers:
                calculate_list.append(int(board[row][col].get()))
                calculate_list_index.append((row, col))
        if calculate_list:
            if len(calculate_list) == 2:
                if calculate_list[0] == calculate_list[1]:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    sum_result = sum(calculate_list)
                    board[0][col].insert(0, sum_result)
                else:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    board[0][col].insert(0, calculate_list[0])
                    board[1][col].insert(0, calculate_list[1])
            elif len(calculate_list) == 3:
                if calculate_list[0] == calculate_list[1]:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    sum_result = sum(calculate_list[0:2])
                    board[0][col].insert(0, sum_result)
                    board[1][col].insert(0, calculate_list[2])
                elif calculate_list[1] == calculate_list[2]:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    sum_result = sum(calculate_list[1:3])
                    board[0][col].insert(0, calculate_list[0])
                    board[1][col].insert(0, sum_result)
                else:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    board[0][col].insert(0, calculate_list[0])
                    board[1][col].insert(0, calculate_list[1])
                    board[2][col].insert(0, calculate_list[2])

            elif len(calculate_list) == 4:
                if calculate_list[0] == calculate_list[1] and calculate_list[2] != calculate_list[3]:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    sum_result = sum(calculate_list[0:2])
                    board[0][col].insert(0, sum_result)
                    board[1][col].insert(0, calculate_list[2])
                    board[2][col].insert(0, calculate_list[3])
                elif calculate_list[0] == calculate_list[1] and calculate_list[2] == calculate_list[3]:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    sum_result = sum(calculate_list[0:2])
                    board[0][col].insert(0, sum_result)
                    sum_result = sum(calculate_list[2:4])
                    board[1][col].insert(0, sum_result)
                elif calculate_list[0] != calculate_list[1] and calculate_list[1] == calculate_list[2]:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    board[0][col].insert(0, calculate_list[0])
                    sum_result = sum(calculate_list[1:3])
                    board[1][col].insert(0, sum_result)
                    board[2][col].insert(0, calculate_list[3])
                elif calculate_list[0] != calculate_list[1] and calculate_list[2] == calculate_list[3]:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    board[0][col].insert(0, calculate_list[0])
                    board[1][col].insert(0, calculate_list[1])
                    sum_result = sum(calculate_list[2:4])
                    board[2][col].insert(0, sum_result)
            else:
                for index in calculate_list_index:
                    row, col = index
                    board[row][col].delete(0, tk.END)
                board[0][col].insert(0, calculate_list[0])

    new_number(board)
    check()

# function to handle key prees 'Down'


def move_down():
    valid_numbers, board = find_numbers_index()
    for col in range(4):
        calculate_list = []
        calculate_list_index = []
        for row in range(4):
            if (row, col) in valid_numbers:
                calculate_list.append(int(board[row][col].get()))
                calculate_list_index.append((row, col))
        if calculate_list:
            if len(calculate_list) == 2:
                if calculate_list[0] == calculate_list[1]:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    sum_result = sum(calculate_list)
                    board[3][col].insert(0, sum_result)
                else:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    board[2][col].insert(0, calculate_list[0])
                    board[3][col].insert(0, calculate_list[1])
            elif len(calculate_list) == 3:
                if calculate_list[1] == calculate_list[2]:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    board[2][col].insert(0, calculate_list[0])
                    sum_result = sum(calculate_list[1:3])
                    board[3][col].insert(0, sum_result)
                elif calculate_list[0] == calculate_list[1]:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    sum_result = sum(calculate_list[0:2])
                    board[2][col].insert(0, sum_result)
                    board[3][col].insert(0, calculate_list[2])
                else:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    board[1][col].insert(0, calculate_list[0])
                    board[2][col].insert(0, calculate_list[1])
                    board[3][col].insert(0, calculate_list[2])

            elif len(calculate_list) == 4:
                if calculate_list[0] != calculate_list[1] and calculate_list[2] == calculate_list[3]:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    board[1][col].insert(0, calculate_list[0])
                    board[2][col].insert(0, calculate_list[1])
                    sum_result = sum(calculate_list[2:4])
                    board[3][col].insert(0, sum_result)
                elif calculate_list[0] == calculate_list[1] and calculate_list[2] == calculate_list[3]:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    sum_result = sum(calculate_list[0:2])
                    board[2][col].insert(0, sum_result)
                    sum_result = sum(calculate_list[2:4])
                    board[3][col].insert(0, sum_result)
                elif calculate_list[3] != calculate_list[2] and calculate_list[2] == calculate_list[1]:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    board[1][col].insert(0, calculate_list[0])
                    sum_result = sum(calculate_list[1:3])
                    board[2][col].insert(0, sum_result)
                    board[3][col].insert(0, calculate_list[3])

                elif calculate_list[3] != calculate_list[2] and calculate_list[1] == calculate_list[0]:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    sum_result = sum(calculate_list[0:2])
                    board[1][col].insert(0, sum_result)
                    board[2][col].insert(0, calculate_list[2])
                    board[3][col].insert(0, calculate_list[3])
            else:
                for index in calculate_list_index:
                    row, col = index
                    board[row][col].delete(0, tk.END)
                board[3][col].insert(0, calculate_list[0])

    new_number(board)
    check()

# function to handle key prees 'Right'


def move_right():
    valid_numbers, board = find_numbers_index()
    for row in range(4):
        calculate_list = []
        calculate_list_index = []
        for col in range(4):
            if (row, col) in valid_numbers:
                calculate_list.append(int(board[row][col].get()))
                calculate_list_index.append((row, col))
        if calculate_list:
            if len(calculate_list) == 2:
                if calculate_list[0] == calculate_list[1]:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    sum_result = sum(calculate_list)
                    board[row][3].insert(0, sum_result)
                else:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    board[row][2].insert(0, calculate_list[0])
                    board[row][3].insert(0, calculate_list[1])
            elif len(calculate_list) == 3:
                if calculate_list[1] == calculate_list[2]:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    board[row][2].insert(0, calculate_list[0])
                    sum_result = sum(calculate_list[1:3])
                    board[row][3].insert(0, sum_result)
                elif calculate_list[0] == calculate_list[1]:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    sum_result = sum(calculate_list[0:2])
                    board[row][2].insert(0, sum_result)
                    board[row][3].insert(0, calculate_list[2])
                else:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    board[row][1].insert(0, calculate_list[0])
                    board[row][2].insert(0, calculate_list[1])
                    board[row][3].insert(0, calculate_list[2])

            elif len(calculate_list) == 4:
                if calculate_list[0] != calculate_list[1] and calculate_list[2] == calculate_list[3]:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    board[row][1].insert(0, calculate_list[0])
                    board[row][2].insert(0, calculate_list[1])
                    sum_result = sum(calculate_list[2:4])
                    board[row][3].insert(0, sum_result)
                elif calculate_list[0] == calculate_list[1] and calculate_list[2] == calculate_list[3]:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    sum_result = sum(calculate_list[0:2])
                    board[row][2].insert(0, sum_result)
                    sum_result = sum(calculate_list[2:4])
                    board[row][3].insert(0, sum_result)
                elif calculate_list[3] != calculate_list[2] and calculate_list[2] == calculate_list[1]:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    board[row][1].insert(0, calculate_list[0])
                    sum_result = sum(calculate_list[1:3])
                    board[row][2].insert(0, sum_result)
                    board[row][3].insert(0, calculate_list[3])

                elif calculate_list[3] != calculate_list[2] and calculate_list[1] == calculate_list[0]:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    sum_result = sum(calculate_list[0:2])
                    board[row][1].insert(0, sum_result)
                    board[row][2].insert(0, calculate_list[2])
                    board[row][3].insert(0, calculate_list[3])
            else:
                for index in calculate_list_index:
                    row, col = index
                    board[row][col].delete(0, tk.END)
                board[row][3].insert(0, calculate_list[0])

    new_number(board)
    check()

# function to handle key prees 'Left'


def move_left():
    valid_numbers, board = find_numbers_index()
    for row in range(4):
        calculate_list = []
        calculate_list_index = []
        for col in range(4):
            if (row, col) in valid_numbers:
                calculate_list.append(int(board[row][col].get()))
                calculate_list_index.append((row, col))
        if calculate_list:
            if len(calculate_list) == 2:
                if calculate_list[0] == calculate_list[1]:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    sum_result = sum(calculate_list)
                    board[row][0].insert(0, sum_result)
                else:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    board[row][0].insert(0, calculate_list[0])
                    board[row][1].insert(0, calculate_list[1])
            elif len(calculate_list) == 3:
                if calculate_list[1] == calculate_list[2]:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    board[row][0].insert(0, calculate_list[0])
                    sum_result = sum(calculate_list[1:3])
                    board[row][1].insert(0, sum_result)
                elif calculate_list[0] == calculate_list[1]:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    sum_result = sum(calculate_list[0:2])
                    board[row][0].insert(0, sum_result)
                    board[row][1].insert(0, calculate_list[2])
                else:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    board[row][0].insert(0, calculate_list[0])
                    board[row][1].insert(0, calculate_list[1])
                    board[row][2].insert(0, calculate_list[2])

            elif len(calculate_list) == 4:
                if calculate_list[0] != calculate_list[1] and calculate_list[2] == calculate_list[3]:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    board[row][0].insert(0, calculate_list[0])
                    board[row][1].insert(0, calculate_list[1])
                    sum_result = sum(calculate_list[2:4])
                    board[row][2].insert(0, sum_result)
                elif calculate_list[0] == calculate_list[1] and calculate_list[2] == calculate_list[3]:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    sum_result = sum(calculate_list[0:2])
                    board[row][0].insert(0, sum_result)
                    sum_result = sum(calculate_list[2:4])
                    board[row][1].insert(0, sum_result)
                elif calculate_list[3] != calculate_list[2] and calculate_list[2] == calculate_list[1]:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    board[row][0].insert(0, calculate_list[0])
                    sum_result = sum(calculate_list[1:3])
                    board[row][1].insert(0, sum_result)
                    board[row][2].insert(0, calculate_list[3])

                elif calculate_list[3] != calculate_list[2] and calculate_list[1] == calculate_list[0]:
                    for index in calculate_list_index:
                        row, col = index
                        board[row][col].delete(0, tk.END)
                    sum_result = sum(calculate_list[0:2])
                    board[row][0].insert(0, sum_result)
                    board[row][1].insert(0, calculate_list[2])
                    board[row][2].insert(0, calculate_list[3])
            else:
                for index in calculate_list_index:
                    row, col = index
                    board[row][col].delete(0, tk.END)
                board[row][0].insert(0, calculate_list[0])
    new_number(board)
    check()


# Function to search and save all cells that contain number
def find_numbers_index():
    valid_numbers = []
    for row in range(4):
        for col in range(4):
            number_text = board[row][col].get()
            if number_text.isdigit():
                valid_numbers.append((row, col))
    return valid_numbers, board

# Function to make new game(make all the cells empty and put into random cell number 2)


def new_game():
    global limit
    limit = 0
    for entries in board:
        for entry in entries:
            entry.delete(0, tk.END)  # Clear the Entry widget
    random_row = random.randint(0, 3)
    random_col = random.randint(0, 3)
    random_cell = board[random_row][random_col]
    random_cell.insert(0, 2)

# Function to add number to a random valid cell after key press


def new_number(board):
    global limit
    limit += 1
    if limit <= 10:
        random_number = 2
    elif limit <= 20:
        random_number = 4
    elif limit <= 30:
        random_number = 8
    elif limit <= 50:
        random_number = 16
    elif limit <= 100:
        random_number = 32
    else:
        random_number = 64
    valid_entry = []
    for row in range(4):
        for col in range(4):
            x = board[row][col]
            if x.get().strip() == "":
                valid_entry.append(board[row][col])
    if valid_entry:
        random_cell = random.choice(valid_entry)
        random_cell.insert(0, random_number)

# Function to check if any move in the board is possible


def check():
    for entries in board:
        last_entry = 1
        for entry in entries:
            if last_entry == entry.get() or entry.get().strip() == '':
                return True
            last_entry = entry.get()
    for col in range(4):
        last_entry = 1
        for row in range(4):
            if last_entry == board[row][col].get():
                return True
            last_entry = board[row][col].get()
    messagebox.showinfo("Game Over", "You lose...")


# Create GUI application(Cells,Labels,Button)
frame = ttk.Frame(window)
frame.grid(row=0, column=0)

buttons_label = ttk.LabelFrame(frame, text='Buttons')
buttons_label.grid(row=0, column=0)

button_new = ttk.Button(buttons_label, text='New Game',
                        command=new_game)  # corrected placement
button_new.grid(row=0, column=0)  # corrected placement

cells_label = ttk.LabelFrame(frame, text='Cells')
cells_label.grid(row=1, column=0)

cell_a_1 = ttk.Entry(cells_label, width=5, justify='center')
cell_a_1.grid(row=0, column=0)

cell_a_2 = ttk.Entry(cells_label, width=5, justify='center')
cell_a_2.grid(row=1, column=0)

cell_a_3 = ttk.Entry(cells_label, width=5, justify='center')
cell_a_3.grid(row=2, column=0)

cell_a_4 = ttk.Entry(cells_label, width=5, justify='center')
cell_a_4.grid(row=3, column=0)

cell_b_1 = ttk.Entry(cells_label, width=5, justify='center')
cell_b_1.grid(row=0, column=1)

cell_b_2 = ttk.Entry(cells_label, width=5, justify='center')
cell_b_2.grid(row=1, column=1)

cell_b_3 = ttk.Entry(cells_label, width=5, justify='center')
cell_b_3.grid(row=2, column=1)

cell_b_4 = ttk.Entry(cells_label, width=5, justify='center')
cell_b_4.grid(row=3, column=1)

cell_c_1 = ttk.Entry(cells_label, width=5, justify='center')
cell_c_1.grid(row=0, column=2)

cell_c_2 = ttk.Entry(cells_label, width=5, justify='center')
cell_c_2.grid(row=1, column=2)

cell_c_3 = ttk.Entry(cells_label, width=5, justify='center')
cell_c_3.grid(row=2, column=2)

cell_c_4 = ttk.Entry(cells_label, width=5, justify='center')
cell_c_4.grid(row=3, column=2)

cell_d_1 = ttk.Entry(cells_label, width=5, justify='center')
cell_d_1.grid(row=0, column=3)

cell_d_2 = ttk.Entry(cells_label, width=5, justify='center')
cell_d_2.grid(row=1, column=3)

cell_d_3 = ttk.Entry(cells_label, width=5, justify='center')
cell_d_3.grid(row=2, column=3)

cell_d_4 = ttk.Entry(cells_label, width=5, justify='center')
cell_d_4.grid(row=3, column=3)
# Create a 2D list called "board" containing references to all the entry widgets representing the cells
# This list will be used to manage the game state and perform operations on the cells
board = [[cell_a_1, cell_b_1, cell_c_1, cell_d_1],
         [cell_a_2, cell_b_2, cell_c_2, cell_d_2],
         [cell_a_3, cell_b_3, cell_c_3, cell_d_3],
         [cell_a_4, cell_b_4, cell_c_4, cell_d_4]]

# Bind the arrow keys ("<Up>", "<Down>", "<Right>", "<Left>") to the on_key_press function
# This function will handle key presses and perform appropriate actions in the game
window.bind("<Up>", on_key_press)
window.bind("<Down>", on_key_press)
window.bind("<Right>", on_key_press)
window.bind("<Left>", on_key_press)

# Start the Tkinter event loop to handle user inputs and interactions with the GUI
window.mainloop()
