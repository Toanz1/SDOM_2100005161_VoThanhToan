import tkinter as tk
from tkinter import ttk, messagebox

# Create the main window
root = tk.Tk()
root.title("Data Entry Form")

# User Information Frame
frame_user_info = ttk.LabelFrame(root, text="User Information")
frame_user_info.grid(row=0, column=0, padx=10, pady=10)

# First Name
ttk.Label(frame_user_info, text="First Name").grid(row=0, column=0, padx=5, pady=5)
entry_first_name = ttk.Entry(frame_user_info)
entry_first_name.grid(row=0, column=1, padx=5, pady=5)

# Last Name
ttk.Label(frame_user_info, text="Last Name").grid(row=0, column=2, padx=5, pady=5)
entry_last_name = ttk.Entry(frame_user_info)
entry_last_name.grid(row=0, column=3, padx=5, pady=5)

# Title
ttk.Label(frame_user_info, text="Title").grid(row=0, column=4, padx=5, pady=5)
combo_title = ttk.Combobox(frame_user_info, values=["Mr.", "Ms.", "Dr.", "Prof."])
combo_title.grid(row=0, column=5, padx=5, pady=5)

# Age
ttk.Label(frame_user_info, text="Age").grid(row=1, column=0, padx=5, pady=5)
spinbox_age = tk.Spinbox(frame_user_info, from_=0, to=100)
spinbox_age.grid(row=1, column=1, padx=5, pady=5)

# Nationality
ttk.Label(frame_user_info, text="Nationality").grid(row=1, column=2, padx=5, pady=5)
entry_nationality = ttk.Entry(frame_user_info)
entry_nationality.grid(row=1, column=3, padx=5, pady=5)

# Registration Status Frame
frame_registration_status = ttk.LabelFrame(root, text="Registration Status")
frame_registration_status.grid(row=1, column=0, padx=10, pady=10)

# Currently Registered
check_currently_registered = ttk.Checkbutton(frame_registration_status, text="Currently Registered")
check_currently_registered.grid(row=0, column=0, padx=5, pady=5)

# Completed Courses
ttk.Label(frame_registration_status, text="# Completed Courses").grid(row=1, column=0, padx=5, pady=5)
spinbox_completed_courses = tk.Spinbox(frame_registration_status, from_=0, to=50)
spinbox_completed_courses.grid(row=1, column=1, padx=5, pady=5)

# Semesters
ttk.Label(frame_registration_status, text="# Semesters").grid(row=1, column=2, padx=5, pady=5)
spinbox_semesters = tk.Spinbox(frame_registration_status, from_=0, to=20)
spinbox_semesters.grid(row=1, column=3, padx=5, pady=5)

# Terms & Conditions Frame
frame_terms_conditions = ttk.LabelFrame(root, text="Terms & Conditions")
frame_terms_conditions.grid(row=2, column=0, padx=10, pady=10)

# Accept Terms
check_accept_terms = ttk.Checkbutton(frame_terms_conditions, text="I accept the terms and conditions.")
check_accept_terms.grid(row=0, column=0, padx=5, pady=5)

# Function to display the entered data
def show_data():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    title = combo_title.get()
    age = spinbox_age.get()
    nationality = entry_nationality.get()
    currently_registered = "Yes" if check_currently_registered.instate(['selected']) else "No"
    completed_courses = spinbox_completed_courses.get()
    semesters = spinbox_semesters.get()
    accept_terms = "Yes" if check_accept_terms.instate(['selected']) else "No"

    data = (
        f"First Name: {first_name}\n"
        f"Last Name: {last_name}\n"
        f"Title: {title}\n"
        f"Age: {age}\n"
        f"Nationality: {nationality}\n"
        f"Currently Registered: {currently_registered}\n"
        f"Completed Courses: {completed_courses}\n"
        f"Semesters: {semesters}\n"
        f"Accepted Terms: {accept_terms}"
    )

    messagebox.showinfo("Entered Data", data)

# Enter Data Button
button_enter_data = ttk.Button(root, text="Enter data", command=show_data)
button_enter_data.grid(row=3, column=0, padx=10, pady=10)

# Run the main loop
root.mainloop()
