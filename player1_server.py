# -*- coding: utf-8 -*-
"""
Created on Thu May 25 18:52:00 2023

@author: Right
"""

import socket
import random

# Generate a random number for Player 1
number = random.randint(1, 100)

# Create the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 8000))
server_socket.listen(1)

# Accept a client connection
conn, addr = server_socket.accept()

# Game loop
while True:
    # Receive the guess from Player 2
    guess = int(conn.recv(1024).decode())

    # Check if the guess is correct
    if guess == number:
        conn.send("Correct! Player 2 wins!".encode())
        break
    elif guess < number:
        conn.send("Too low. Guess again.".encode())
    else:
        conn.send("Too high. Guess again.".encode())

# Close the server socket
server_socket.close()
