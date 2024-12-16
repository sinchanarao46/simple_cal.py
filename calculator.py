import tkinter as tk

# Define the calculator application class
class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Calculator")
        self.root.geometry("300x400")
        
        # Entry widget for displaying input and result
        self.display = tk.Entry(root, font=("Arial", 18), borderwidth=5, justify="left")
        self.display.grid(row=0, column=0, columnspan=100, ipadx=8, ipady=10)

        # Buttons
        buttons = [
            "AC", "DEL", "/", "*",
            "7", "8", "9", "-",
            "4", "5", "6", "+",
            "1", "2", "3", "=",
            "0", ".", "(", ")"
        ]

        # Adding buttons to the grid
        row = 1
        col = 0
        for button in buttons:
            if button == "AC":
                action = lambda: self.clear()
            elif button == "DEL":
                action = lambda: self.delete()
            elif button == "=":
                action = lambda: self.calculate()
            else:
                action = lambda char=button: self.append_to_display(char)

            tk.Button(
                root, text=button, width=6, height=2, font=("Arial", 15),
                command=action, bg="#f0f0f0"
            ).grid(row=row, column=col, sticky="nsew")

            col += 1
            if col > 3:
                col = 0
                row += 1

    def append_to_display(self, char):
        """Append a character to the display."""
        self.display.insert(tk.END, char)

    def clear(self):
        """Clear the display."""
        self.display.delete(0, tk.END)

    def delete(self):
        """Delete the last character."""
        current = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(0, current[:-1])

    def calculate(self):
        """Evaluate the expression in the display."""
        try:
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

# Create the Tkinter root window
root = tk.Tk()
calc_app = CalculatorApp(root)

# Start the main event loop
root.mainloop()
