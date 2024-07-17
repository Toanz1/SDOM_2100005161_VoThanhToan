import tkinter as tk
from tkinter import font

def main():
    root = tk.Tk()
    root.title("AtarBals Modern Antivirus")  # Set the window title
    root.geometry("800x500")  # Set the window size
    root.configure(bg='#C0C0C0')  # Set the background color to Silver

    title_font = font.Font(family="Arial", size=24, weight="bold")  # Font for the main title
    subtitle_font = font.Font(family="Arial", size=12)  # Font for subtitles
    button_font = font.Font(family="Arial", size=10, weight="bold")  # Font for buttons
    sidebar_font = font.Font(family="Arial", size=14)  # Font for the sidebar

    def open_success_tab(message):
        """Open success notification tab."""
        success_window = tk.Toplevel(root)
        success_window.title("Notification")
        success_window.geometry("300x200")
        success_window.configure(bg='#C0C0C0')

        success_label = tk.Label(success_window, text=message, font=subtitle_font, fg='#27AE60', bg='#C0C0C0')
        success_label.pack(pady=50)

    def update_status(status):
        """Update the status and handle success notifications."""
        status_label.config(text=status)
        if status == "Scan completed successfully...":
            status_label.config(fg='#27AE60')
            open_success_tab("Scan completed successfully!")
        elif status == "Quick scanning...":
            open_success_tab("Performing quick scan...")
        elif status == "Quarantining...":
            open_success_tab("Quarantining...")

    main_frame = tk.Frame(root, bg='#C0C0C0')
    main_frame.pack(fill='both', expand=True)

    sidebar_frame = tk.Frame(main_frame, bg='#2C3E50', width=200)
    sidebar_frame.pack(side='left', fill='y')

    sections = ["Status", "Update", "Settings", "Feedback", "Buy Premium", "Help"]
    for section in sections:
        label = tk.Label(sidebar_frame, text=section, bg='#2C3E50', fg='white', font=sidebar_font)
        label.pack(pady=10, anchor='w', padx=20)

    content_frame = tk.Frame(main_frame, bg='#C0C0C0')
    content_frame.pack(side='right', fill='both', expand=True, padx=20, pady=20)

    title_label = tk.Label(content_frame, text="Scan", bg='#C0C0C0', font=title_font, fg='#2C3E50')
    title_label.pack(pady=10)

    subtitle_label = tk.Label(content_frame, text="Premium will always be free. Just click the button.", bg='#C0C0C0', font=subtitle_font, fg='#2C3E50')
    subtitle_label.pack(pady=5)

    scan_now_button = tk.Button(sidebar_frame, text="Scan Now", bg='#27AE60', fg='white', font=button_font, command=lambda: update_status("Scan completed successfully..."))
    scan_now_button.pack(pady=20, anchor='w', padx=20)

    buttons = [
        ("Quick Scan", "Quick scanning..."),
        ("Web Protection", "Web protection requires Premium!"),
        ("Quarantine", "Quarantining..."),
        ("Full Scan", "Full scan requires Premium!"),
        ("Simple Update", "Simple update requires Premium!")
    ]

    for i, (button_text, status_text) in enumerate(buttons):
        button = tk.Button(content_frame, text=button_text, bg='#3498DB', fg='white', font=button_font, width=15, command=lambda st=status_text: update_status(st))
        button.pack(pady=5)
        if i % 2 == 0:
            button.pack(anchor='w')  # Left-align even-positioned buttons
        else:
            button.pack(anchor='e')  # Right-align odd-positioned buttons

    status_label = tk.Label(content_frame, text="Get Premium to Enable: {Web Protection}, {Full Scan}, {Simple Update}", bg='#C0C0C0', fg='#3498DB', font=subtitle_font)
    status_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
