import tkinter as tk
from tkinter import ttk


def reset():
    set_placeholder(username_entry, "Введите имя пользователя")
    set_placeholder(email_entry, "example@example.com")
    set_placeholder(password_entry, "********")
    set_placeholder(address_entry, "Введите адрес")
    set_placeholder(dob_entry, "ДД.ММ.ГГГГ")
    set_placeholder(age_entry, "18")
    gender.set('')
    terms.set(0)


def add_placeholder(entry, placeholder):
    entry.insert(0, placeholder)
    entry.bind("<FocusIn>", lambda e: on_focus_in(entry, placeholder))
    entry.bind("<FocusOut>", lambda e: on_focus_out(entry, placeholder))


def on_focus_in(entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, tk.END)
        entry.config(foreground='black')


def on_focus_out(entry, placeholder):
    if not entry.get():
        entry.insert(0, placeholder)
        entry.config(foreground='gray')


def set_placeholder(entry, placeholder):
    entry.delete(0, tk.END)
    entry.insert(0, placeholder)
    entry.config(foreground='gray')




root = tk.Tk()
root.title("Форма регистрации")
root.geometry("800x600")



style = ttk.Style()
style.configure("TFrame", borderwidth=1, relief="solid")



login_frame = ttk.Frame(root, padding=10)
login_frame.pack(pady=10, fill=tk.X)

login_label = ttk.Label(login_frame, text="User login info", font=("Arial", 12, "bold"))
login_label.grid(row=0, column=0, columnspan=2, sticky=tk.W)



username_label = ttk.Label(login_frame, text="Username:")
username_label.grid(row=1, column=0, pady=5, sticky=tk.W)
username_entry = ttk.Entry(login_frame, width=30, foreground='gray')
username_entry.grid(row=1, column=1, pady=5)
add_placeholder(username_entry, "Введите имя пользователя")



email_label = ttk.Label(login_frame, text="Email:")
email_label.grid(row=2, column=0, pady=5, sticky=tk.W)
email_entry = ttk.Entry(login_frame, width=30, foreground='gray')
email_entry.grid(row=2, column=1, pady=5)
add_placeholder(email_entry, "example@example.com")



password_label = ttk.Label(login_frame, text="Password:")
password_label.grid(row=3, column=0, pady=5, sticky=tk.W)
password_entry = ttk.Entry(login_frame, width=30, show="*", foreground='gray')
password_entry.grid(row=3, column=1, pady=5)
add_placeholder(password_entry, "********")



data_frame = ttk.Frame(root, padding=10)
data_frame.pack(pady=10, fill=tk.X)

data_label = ttk.Label(data_frame, text="Data diri", font=("Arial", 12, "bold"))
data_label.grid(row=0, column=0, columnspan=2, sticky=tk.W)



address_label = ttk.Label(data_frame, text="Alamat:")
address_label.grid(row=1, column=0, pady=5, sticky=tk.W)
address_entry = ttk.Entry(data_frame, width=30, foreground='gray')
address_entry.grid(row=1, column=1, pady=5)
add_placeholder(address_entry, "Введите адрес")



dob_label = ttk.Label(data_frame, text="Tanggal lahir:")
dob_label.grid(row=2, column=0, pady=5, sticky=tk.W)
dob_entry = ttk.Entry(data_frame, width=30, foreground='gray')
dob_entry.grid(row=2, column=1, pady=5)
add_placeholder(dob_entry, "ДД.ММ.ГГГГ")



age_label = ttk.Label(data_frame, text="Usia:")
age_label.grid(row=3, column=0, pady=5, sticky=tk.W)
age_entry = ttk.Entry(data_frame, width=30, foreground='gray')
age_entry.grid(row=3, column=1, pady=5)
add_placeholder(age_entry, "18")



gender_label = ttk.Label(data_frame, text="Jenis kelamin:")
gender_label.grid(row=4, column=0, pady=5, sticky=tk.W)
gender = tk.StringVar()
male_radio = ttk.Radiobutton(data_frame, text="Pria", variable=gender, value="Pria")
male_radio.grid(row=4, column=1, sticky=tk.W)
female_radio = ttk.Radiobutton(data_frame, text="Wanita", variable=gender, value="Wanita")
female_radio.grid(row=4, column=1, padx=80, sticky=tk.W)



buttons_frame = ttk.Frame(root, padding=10)
buttons_frame.pack(pady=10, fill=tk.X)

terms = tk.IntVar()
terms_check = ttk.Checkbutton(buttons_frame, text="Saya bersedia mengikuti aturan forum", variable=terms)
terms_check.grid(row=0, column=0, columnspan=2, sticky=tk.W)

reset_btn = ttk.Button(buttons_frame, text="Reset", command=reset)
reset_btn.grid(row=1, column=0, pady=10)

# Кнопка отправки теперь просто не делает ничего
submit_btn = ttk.Button(buttons_frame, text="Submit")
submit_btn.grid(row=1, column=1, pady=10)

root.mainloop()
