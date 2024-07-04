import subprocess
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, font, Text, WORD
import threading
import os

root = tk.Tk()

# Create a custom font with a larger size
title_font = ("Helvetica", 24, "bold")
button_font = ("Helvetica", 12)
# Set window icon and title
root.iconbitmap(r"C:\Users\user\Desktop\FYP\logo.ico")
root.title("AYMAN KANSO ULFG3")
root.geometry("1200x800")
root.configure(bg="#f0f0f0")

style = ttk.Style()
style.configure("TButton", font=button_font, padding=10)
style.configure("TLabel", font=("Helvetica", 14), background="#f0f0f0")
style.configure("TFrame", background="#f0f0f0")

# Function to browse files and update entry field
def browse_file(entry):
    file_path = filedialog.askopenfilename(filetypes=[("All files", "*.*")])
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

# Function to create new windows with specified title and description
def create_new_window(title, description, command):
    new_window = tk.Toplevel(root)
    new_window.title(title)
    new_window.geometry("800x600")
    new_window.iconbitmap(r"C:\Users\user\Desktop\FYP\logo.ico")
    new_window.configure(bg="#f0f0f0")
    
    label = ttk.Label(new_window, text=title, font=("Helvetica", 16, "bold"))
    label.pack(pady=10)
    
    description_label = ttk.Label(new_window, text=description, justify="left", wraplength=700)
    description_label.pack(pady=10)
    
    command(new_window)

# Function to display output in a Text widget
def display_output(new_window, output):
    output_text = tk.Text(new_window, wrap=WORD, width=70, height=20)
    output_text.pack(pady=10)
    output_text.insert(tk.END, output)

# Example function to show how to integrate other functions
def example_function(new_window):
    label = ttk.Label(new_window, text="Example Function Content")
    label.pack()

# Define button commands for each functionality
def open_new_window1():
    description = ("This tool is a network credential sniffer implemented in Python using the Scapy library. "
                   "It aims to analyze network traffic captured in a PCAP file to identify and extract sensitive "
                   "information such as FTP usernames and passwords, SMTP usernames, and telnet usernames and passwords.")
    create_new_window("Network Sniffing", description, example_function)

def open_new_window2():
    description = ("This tool is designed to search through specified directories for files containing personally "
                   "identifiable information (PII) such as email addresses, phone numbers, and social security numbers (SSNs). "
                   "It supports searching through .docx files and any other text-based files specified by the user.")
    create_new_window("File & Directory Discovery", description, example_function)

# Add similar functions for other tools

# Main window layout with buttons
main_frame = ttk.Frame(root, padding="20")
main_frame.pack(expand=True)

buttons = [
    ("Network Sniffing", open_new_window1),
    ("File & Directory Discovery", open_new_window2),
    ("Remote Services", example_function),  # Replace example_function with the actual function
    ("Encrypt Channel", example_function),
    ("Protocol Tunneling", example_function),
    ("Non application layer protocol", example_function),
    ("Data Encryption/Decryption", example_function),
    ("Decoy content", example_function),
    ("Burn in", example_function),
    ("Network Monitoring", example_function),
    ("Behavioral Analysis", example_function),
    ("local email account", example_function),
    ("Modify Clipboard", example_function),
    ("User Discovery", example_function),
    ("DNS Exfiltration", example_function),
    ("Account Access Removal", example_function),
    ("Sys Activity Monitoring", example_function),
    ("Port Scanner", example_function),
    ("OS Detection", example_function),
    ("Network Device Discovery", example_function)
]

for index, (text, command) in enumerate(buttons):
    row = index // 3
    column = index % 3
    button = ttk.Button(main_frame, text=text, command=command)
    button.grid(row=row, column=column, padx=20, pady=20, sticky="nsew")

root.mainloop()
