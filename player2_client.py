# -*- coding: utf-8 -*-
"""
Created on Thu May 25 19:18:21 2023

@author: Right
"""
import tkinter as tk
import socket
import tkinter.messagebox as messagebox

# Create the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 8000))

# Create the GUI window
window = tk.Tk()
window.title("Guess the Number")

# Variables
player_turn = tk.StringVar()
guess_text = tk.StringVar()
result_text = tk.StringVar()

# Function to process the guess
def process_guess():
    guess = int(guess_text.get())
    client_socket.send(str(guess).encode())

    # Receive the result from Player 1
    result = client_socket.recv(1024).decode()
    result_text.set(result)
    messagebox.showinfo("Result", result)

    # Check if the guess is correct
    if "wins" in result:
        window.quit()

# GUI Elements
turn_label = tk.Label(window, textvariable=player_turn)
turn_label.pack(pady=10)

guess_label = tk.Label(window, text="Enter your guess:")
guess_label.pack()

guess_entry = tk.Entry(window, textvariable=guess_text)
guess_entry.pack()

result_label = tk.Label(window, textvariable=result_text)
result_label.pack(pady=10)

submit_button = tk.Button(window, text="Submit", command=process_guess)
submit_button.pack(pady=10)

# Start the GUI event loop
window.mainloop()

# Close the client socket
client_socket.close()
