from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Error code 6969", message="Please fill in all fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Is this information correct?\n{email}\n{password}"
                                                  f"\nIs it okay to save?")
        if is_ok:
            messagebox.showinfo("Success", "Information has been saved")
            with open("password_data.txt", "a") as password_doc:
                password_doc.write(f"\n{website} | {email} | {password}")
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
# window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

# canvas
canvas = Canvas(width=200, height=200, bg="white",highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# labels

website_label = Label(text="Website")
website_label.config(bg="white")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username")
email_label.config(bg="white")
email_label.grid(column=0, row=2)
password_label = Label(text="Password")
password_label.config(bg="white")
password_label.grid(column=0, row=3)

# Entries

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "Joe.Schmoe@gmail.com")
password_entry = Entry(width=17)
password_entry.grid(column=1, row=3)



# Buttons

password_button = Button(text="Generate Password")
password_button.config(bg="white")
password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=30)
add_button.config(bg="white", command=save)
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()


