# from tkinter import Tk

on = True

while on:
    input_text = ""

    text = ""
    while input_text != "q":
        input_text = input("Please put in text to remove multi spaces: ")
        if input_text.lower().strip() == "quit software":
            on = False
            break

        if input_text.strip().lower() == "q":
            break
        text += input_text.replace("\n", "")
        text += " "

    print("\n")

    previous = ""
    current = text
    while previous != current:
        previous = current
        current = current.replace("  "," ")
    
    # r = Tk()
    # r.withdraw()
    # r.clipboard_clear()
    # r.clipboard_append(current.strip())
    # r.update() # now it stays on the clipboard after the window is closed
    # r.destroy()
    print(current.strip())
    print("\n")