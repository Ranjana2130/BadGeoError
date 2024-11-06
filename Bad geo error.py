import tkinter as tk
from tkinter import messagebox

def set_geometry():
    try:
        # Try setting an invalid geometry to trigger a Bad Geometry error
        root.geometry("-50x800")  # Invalid geometry, negative width
    except Exception as e:
        # Catch the error and display a message box with the error information
        messagebox.showerror("An error occurred","Please check your geometry dimension")
        
        
# Create the main Tkinter window
root = tk.Tk()
root.title("Bad Geometry Error Handling Example")

# Create a button to set the geometry
button = tk.Button(root, text="Set Invalid Geometry", command=set_geometry)
button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
