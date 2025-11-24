from customtkinter import *
import csv

from tkinter import messagebox, ttk
attempts_left = 3


def login_success():
    # create window after login main screen
    main = CTk(fg_color="#909590")
    main.geometry("1920x1080")
    main.title("Trail Talk")
    main.resizable(False, False)
    main.attributes ("-fullscreen", True)
    main.update()

    main_exit_button = CTkButton(main, text="X", font=CTkFont(size=20, weight="bold"), fg_color="#FF5C5C", command=main.destroy)
    main_exit_button.pack(side="top", anchor="ne", padx=10, pady=10)



# log in function to check username and password against CSV file
def login(username, password):
    global attempts_left # to modify the global variable
    with open('users.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader: # seach through each row
            if row['username'] == username and row['password'] == password: # if both are equal it will work
                login_success() # open main window 
                exit_app() # kils the log in welcom window
                return True # if this isnt here then messagebox will still show idk why 
            else:     
                attempts_left = attempts_left - 1 # needs to before the if statement or closes at -1
                messagebox.showerror("Login Failed", f"Invalid username or password. You have {attempts_left} attempts left.")
                if attempts_left <= 0:
                    app.destroy()  # close the app if no attempts left
                return False 

# signup function to add new username and password to CSV file

def signup(username, password):
    with open('users.csv', mode='a', newline='') as file: # append mode to add without deleting



#function to open top level window for login and signup
def open_login_signup():
    # make sure no other top level windows are open

    window_login = CTkToplevel(app, fg_color="#1E1E1E")
    window_login.geometry("650x400")
    window_login.title("Login/Signup")
    window_login.resizable(False, False)
    window_login.focus()
    window_login.attributes ("-topmost", True)   # keep window on top of main window Thanks stack overflow
    window_login.update() # update window to apply attributes

    # tabs for login and signup
    tabview = CTkTabview(window_login, fg_color="#474A48", segmented_button_fg_color="#537A5A", segmented_button_selected_color="#9AE19D", segmented_button_unselected_color="#537A5A")
    tabview.pack(pady=20, padx=20, fill="both", expand=True)
    login_tab = tabview.add("Login")
    signup_tab = tabview.add("Signup")
    # Top level window for login/signup

    #login
    # username: label then entry Password: label then entry then button
    # these haveto be placed in the function with the definition otherwise they wont show up
    username_login_label = CTkLabel(login_tab, text="Username:", font=CTkFont(size=20), text_color="#FFFFFF")
    username_login_label.pack(pady=10)
    username_login_entry = CTkEntry(login_tab, width=300, font=CTkFont(size=20))
    username_login_entry.pack(pady=10)
    password_login_label = CTkLabel(login_tab, text="Password:", font=CTkFont(size=20), text_color="#FFFFFF")
    password_login_label.pack(pady=10)
    password_login_entry = CTkEntry(login_tab, width=300, font=CTkFont(size=20))
    password_login_entry.pack(pady=10)
    login_button = CTkButton(login_tab, text="Log in", font=CTkFont(size=20), fg_color="#9AE19D", command=lambda: login(username_login_entry.get(), password_login_entry.get()))
    login_button.pack(pady=20)
    #attemps left label
    attempts_left_label = CTkLabel(login_tab, text="You have 3 total attempts", font=CTkFont(size=15), text_color="#FF0000")
    attempts_left_label.pack(pady=5)
    
    # signup
    # username: label then entry Password: label then entry then button
    
    username_signup_label = CTkLabel(signup_tab, text="Username:", font=CTkFont(size=20), text_color="#FFFFFF")
    username_signup_label.pack(pady=10)
    username_signup_entry = CTkEntry(signup_tab, width=300, font=CTkFont(size=20))
    username_signup_entry.pack(pady=10)
    password_signup_label = CTkLabel(signup_tab, text="Password:", font=CTkFont(size=20), text_color="#FFFFFF")
    password_signup_label.pack(pady=10)
    password_signup_entry = CTkEntry(signup_tab, width=300, font=CTkFont(size=20))
    password_signup_entry.pack(pady=10)
    signup_button = CTkButton(signup_tab, text="Sign up", font=CTkFont(size=20), fg_color="#9AE19D", command=lambda: signup(username_signup_entry.get(), password_signup_entry.get()))
    signup_button.pack(pady=20)
    
#function to exit kill welcome window and app
def exit_app():
    app.destroy()    
#def exit_main():
#    main.destroy()

#create the login window
app = CTk(fg_color="#909590")
app.geometry("1920x1080")
app.title("Trail Talk | Login required")
app.resizable(False, False)
app.attributes ("-fullscreen", True)
app.update()

# login window Title
# exit button top right
exit_button = CTkButton(app, text="X", font=CTkFont(size=20, weight="bold"), fg_color="#FF5C5C", command=app.destroy)
exit_button.pack(side="top", anchor="ne", padx=10, pady=10)

# title
app_Title = CTkLabel(app, text="Trail Talk", font=CTkFont(size=250, weight="bold"), text_color="#537A5A")
app_Title.pack(pady=50)

#solgan
app_slogan = CTkLabel(app, text='"Connecting hikers, One path at a time."', font=CTkFont(size=45, weight="bold"), text_color="#FFFFFF")
app_slogan.pack(pady=10)

# button
Open_login_window_button = CTkButton(app, text="Log in",font=CTkFont(size=20, weight="bold"),fg_color="#9AE19D", command=open_login_signup)
Open_login_window_button.pack(pady=90)





#run the application
app.mainloop()

# ---ignore---
"""
TO do list:
- Make sure only one login/signup window has one instance at a time
- stuck on appending to CSV file 
""" 