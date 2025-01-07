import os
import zipfile
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

# Function to compress a directory
def compress_directory():
    directory = filedialog.askdirectory(title="Select the directory to compress")
    if directory:
        zip_file = filedialog.asksaveasfilename(defaultextension=".zip", filetypes=[("ZIP files", "*.zip")])
        if zip_file:
            with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zf:
                for root, dirs, files in os.walk(directory):
                    for file in files:
                        zf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), directory))
            messagebox.showinfo("Success", f"Directory '{directory}' compressed as '{zip_file}'")

# Function to compress multiple files
def compress_multiple_files():
    files = filedialog.askopenfilenames(
        title="Select files to compress",
        filetypes=[("All files", "*.*")]
    )
    if files:
        zip_file = filedialog.asksaveasfilename(defaultextension=".zip", filetypes=[("ZIP files", "*.zip")])
        if zip_file:
            progress_bar['maximum'] = len(files)
            with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zf:
                for i, file in enumerate(files, 1):
                    zf.write(file, os.path.basename(file))
                    progress_bar['value'] = i
                    root.update_idletasks()  # Actualiza la interfaz gráfica
            progress_bar['value'] = 0  # Restablece la barra de progreso
            messagebox.showinfo("Success", f"Files compressed as '{zip_file}'")

# Function to decompress a ZIP file
def decompress_zip():
    zip_file = filedialog.askopenfilename(title="Select the ZIP file to decompress", filetypes=[("ZIP files", "*.zip")])
    if zip_file:
        destination = filedialog.askdirectory(title="Select the destination directory")
        if destination:
            with zipfile.ZipFile(zip_file, 'r') as zf:
                zf.extractall(destination)
            messagebox.showinfo("Success", f"File '{zip_file}' decompressed to '{destination}'")

# Set up the graphical interface
root = tk.Tk()
root.title("ZIP Utility")

label = tk.Label(root, text="Select an option:", font=("Arial", 14))
label.pack(pady=20)

button_compress_dir = tk.Button(root, text="Compress a directory", command=compress_directory, width=30)
button_compress_dir.pack(pady=10)

button_compress_files = tk.Button(root, text="Compress multiple files", command=compress_multiple_files, width=30)
button_compress_files.pack(pady=10)

button_decompress = tk.Button(root, text="Decompress a ZIP file", command=decompress_zip, width=30)
button_decompress.pack(pady=10)

button_exit = tk.Button(root, text="Exit", command=root.quit, width=30)
button_exit.pack(pady=10)

# Add a progress bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(pady=10)

# Run the application
root.mainloop()
