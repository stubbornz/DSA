# importing libraries
from tkinter import *
from extras import User

def rating():
    user = User()
    # frame
    FRAME = Frame(root, bg=BACKGROUND_COLOR, relief=SUNKEN, borderwidth=5)
    FRAME.grid(row=0, column=0, padx=169, pady=20)

    # details
    frame = Frame(FRAME, bg=FRAME_COLOR, relief=SUNKEN, borderwidth=2)
    frame.grid(row=0, column=0, pady=15, padx=1)
    Label(frame, text="Name -->", font=FONTS, bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR, padx=12).grid(row=0, column=0)
    Label(frame, text="Rating", font=FONTS, bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR, padx=12).grid(row=0, column=1)

    # user details
    # Hritik
    frame = Frame(FRAME, bg=FRAME_COLOR, relief=SUNKEN, borderwidth=2)
    frame.grid(row=1, column=0, pady=15, padx=1)
    Label(frame, text=" Hritik -->", font=FONTS, fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR).grid(row=1, column=0)
    Label(frame, text=user.hritik, font=FONTS, fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR).grid(row=1, column=1)

    # Chid
    frame = Frame(FRAME, bg=FRAME_COLOR, relief=SUNKEN, borderwidth=2)
    frame.grid(row=2, column=0, pady=15, padx=1)
    Label(frame, text=" chid -->", font=FONTS, fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR).grid(row=2, column=0)
    Label(frame, text=user.chid, font=FONTS, fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR).grid(row=2, column=1)

    # Tanu
    frame = Frame(FRAME, bg=FRAME_COLOR, relief=SUNKEN, borderwidth=2)
    frame.grid(row=3, column=0, pady=15, padx=1)
    Label(frame, text=" tanu -->", font=FONTS, fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR).grid(row=3, column=0)
    Label(frame, text=user.chid, font=FONTS, fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR).grid(row=3, column=1)

    # Jp
    frame = Frame(FRAME, bg=FRAME_COLOR, relief=SUNKEN, borderwidth=2)
    frame.grid(row=4, column=0, pady=15, padx=1)
    Label(frame, text=" Jp -->", font=FONTS, fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR).grid(row=4, column=0)
    Label(frame, text=user.jp, font=FONTS, fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR).grid(row=4, column=1)

    # # Nikita
    # frame = Frame(FRAME, bg=FRAME_COLOR, relief=SUNKEN, borderwidth=2)
    # frame.grid(row=5, column=0, pady=15, padx=1)
    # Label(frame, text=" Nikita -->", font=FONTS, fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR).grid(row=5, column=0)
    # Label(frame, text=user.nikita, font=FONTS, fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR).grid(row=5, column=1)
    # # Hritik
    # frame = Frame(FRAME, bg=FRAME_COLOR, relief=SUNKEN, borderwidth=2)
    # frame.grid(row=6, column=0, pady=15, padx=1)
    # Label(frame, text=" Hritik -->", font=FONTS, fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR).grid(row=6, column=0)
    # Label(frame, text=" 000000 ", font=FONTS, fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR).grid(row=6, column=1)


# authenticating user
def authenticateUser(username, password, frame):
    username = username.get()
    password = password.get()
    if(username == ""):
        if(password == ""):
            frame.grid_forget()
            rating()


# codes start here
if __name__ == '__main__':
    # variables
    global BACKGROUND_COLOR
    global FOREGROUND_COLOR
    BACKGROUND_COLOR = '#2F4F4F'
    FOREGROUND_COLOR = '#FFE4E1'
    FRAME_COLOR = '#A9A9A9'
    FONTS = 'Times 25 bold'
    authentication = False

    # initializing tkinter root
    root = Tk()

    # creating tkinter window
    root.geometry("800x500")
    root.title("Work Flow")
    root.config(bg=BACKGROUND_COLOR)

    # frame
    FRAME = Frame(root, bg=BACKGROUND_COLOR, relief=SUNKEN, borderwidth=5)
    FRAME.grid(row=0, column=0, padx=169, pady=60)

    # Work Flow
    Label(FRAME, text="WorkFlow", bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR, font='Times 35 bold', pady=12, padx=5).grid()

    # username entry
    frame = Frame(FRAME, bg=FRAME_COLOR, relief=SUNKEN, borderwidth=5)
    frame.grid(row=1, column=0, padx=15, pady=15)
    Label(frame, text="Username : ", bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR, font=FONTS).grid(row=1, column=0)
    username = Entry(frame, bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR, font=FONTS)
    username.grid(row=1, column=1)

    # password entry
    frame = Frame(FRAME, bg=FRAME_COLOR, relief=SUNKEN, borderwidth=5)
    frame.grid(row=2, column=0, padx=15, pady=15)
    Label(frame, text="Password : ", bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR, font=FONTS).grid(row=2, column=0)
    password = Entry(frame, bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR, font=FONTS)
    password.grid(row=2, column=1)

    # Login button
    frame = Frame(FRAME, bg=FRAME_COLOR, relief=SUNKEN, borderwidth=5)
    frame.grid(row=3, column=0, padx=15, pady=10)
    login = Button(frame, text="LogIn", bg=FOREGROUND_COLOR, fg=BACKGROUND_COLOR, font=FONTS, padx=11, command=lambda: authenticateUser(username, password, FRAME))
    login.grid(row=3, column=1)



    # looping tkinter window
    root.mainloop()
