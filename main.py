from customtkinter import *




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
    tabview.add("Login")
    tabview.add("Signup")

#create the main window
app = CTk(fg_color="#909590")
app.geometry("1920x1080")
app.title("Trail Talk")
app.resizable(False, False)

# main window Title

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

""" 