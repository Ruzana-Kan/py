#Dsktop_notifier
import tkinter as tk
from tkinter import messagebox
from plyer import notification

class DesktopNotifierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Desktop Notifier App")
        self.root.geometry("300x200")

        self.label = tk.Label(root, text="Enter Notification Message:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=10)

        self.notify_button = tk.Button(root, text="Notify", command=self.notify)
        self.notify_button.pack(pady=20)

    def notify(self):
        message = self.entry.get()
 # Notification will disappear after 30 seconds
        if message:
            notification.notify(
                title="Notification",
                message=message,
                timeout= 30 
            )
        else:
            messagebox.showwarning("Empty Message", "Please enter a notification message.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DesktopNotifierApp(root)
    root.mainloop()

