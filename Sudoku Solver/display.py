import tkinter as Tk

#Null declarations
entries = ''
askwin = ''

def writeToFile():
    file = open("displayprob.txt", "w")
    for i in range(9):
        for j in range(9):
            data = entries[i][j].get()
            if data:
                file.write(data)
            else:
                file.write(".")        
    file.close()
    askwin.destroy()

def askWindow():
    global entries, askwin
    askwin = Tk.Tk()
    askwin.geometry('500x400')
    askwin.title('Enter your Sudoku!')
    
    #Welcome text
    welcomeText = Tk.Label(askwin, text = "Welcome to my Sudoku Solver!\nPlease enter your sudoku:", font = ('Century Gothic',15)) 
    welcomeText.pack(anchor = 'center')   

    #Setting up board
    frame = Tk.Frame(askwin)
    frame.pack()
    
    entries = [] 
    for i in range(9):
        row_entries = []
        for j in range(9):
            e = Tk.Entry(frame, width=3, font=('Century Gothic', 14), justify='center')
            e.grid(row=i, column=j, padx=(3 if j % 3 == 0 else 1), pady=(3 if i % 3 == 0 else 1))
            row_entries.append(e)
        entries.append(row_entries)
    
    #Buttons
    solve_button = Tk.Button(askwin, text="Solve", font=('Century Gothic', 15), command=writeToFile)
    solve_button.pack(pady=10)

    askwin.mainloop() 


def solutionFoundWindow(data):
    swin = Tk.Tk()
    swin.geometry('500x400')
    swin.title('Enter your Sudoku!')
    
    #Welcome text
    welcomeText = Tk.Label(swin, text = "Welcome to my Sudoku Solver!\nPlease enter your sudoku:", font = ('Century Gothic',15)) 
    welcomeText.pack(anchor = 'center')   

    #Setting up board
    frame = Tk.Frame(swin)
    frame.pack()

    entries = [] 
    for i in range(9):
        row_entries = []
        for j in range(9):
            e = Tk.Label(frame, text=data[i][j], width=3, font=('Century Gothic', 14), justify='center')
            e.grid(row=i, column=j, padx=(3 if j % 3 == 0 else 1), pady=(3 if i % 3 == 0 else 1))
            row_entries.append(e)
        entries.append(row_entries)
    
    #Buttons
    exit_button = Tk.Button(swin, text="Exit", font=('Century Gothic', 15), command=swin.destroy)
    exit_button.pack(pady=10)

    swin.mainloop() 

def solutionNotWindow():
    snwin = Tk.Tk()
    snwin.geometry('500x400')
    snwin.title('Bad news :(')
    
    #Welcome text
    welcomeText = Tk.Label(snwin, text = "No Solution Found :(", font = ('Century Gothic',15)) 
    welcomeText.pack(anchor = 'center', pady = 235)   
    
    #Buttons
    exit_button = Tk.Button(snwin, text="Exit", font=('Century Gothic', 15), command=snwin.destroy)
    exit_button.pack(pady=10)

    snwin.mainloop() 

