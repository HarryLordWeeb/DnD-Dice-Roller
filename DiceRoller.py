import random
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
# ------------------------Tkinter window and icon.
root = Tk()
root.title('Dice Roller')
root.geometry('1600x1000')
root.resizable(False, False)
root.iconbitmap('./images/favicon.ico')
# ---------------------------------------Style
style = Style()
style.configure('W.TButton', font =
               ('calibri', 20, 'bold', 'underline'),
                foreground = 'Black')
#--------------------------------------------------Output fields 
HistoryOutput = Text(height=100,width=700)
HistoryOutput.place(x=180, y= 0)
HistoryOutput.configure(bg="gray", fg='white', font=('Calibri',20, 'bold'))
CurrentResultOutput = Text(padx=5,width=12,height=2)
CurrentResultOutput.place(x=0, y= 450)
CurrentResultOutput.configure(bg="gray", fg='white', font=('Calibri',20, 'bold'))
#---------------------------------------------------------------Arrays and ranges
texty = ["Name:","Proficiency bonus:","Number of rolls:","Need to roll over:","Bonus on every roll:"]
entry = []
CurrentResult = []
AllRolls = []
RollRange = [ (1,2) , (1,3) , (1,4) , (1,6) , (1,8) , (1,10) , (1,12) , (1,20) , (1,100) ]
# -------------------------------------------------------------------------------------------input placement
for i in range(5):
    s = 75
    Entryx = ttk.Entry(root, font=('Calibri',20, 'bold'),width=12)
    Entryx.place(x = 5, y = 550 + s * i)
    entry.append(Entryx)
    Lablex = ttk.Label(root,font = ('Calibri',14, 'bold'), text=texty[i])
    Lablex.place(x=5, y=520 + s * i)
#-----------------------------------------------------------------------Rolling function + logic for inputs
def Rolling(inddex):
    nameGet = entry[0].get()
    setName= str(nameGet)
    profGet = entry[1].get()
    if profGet == "":
        profGet = 0
    profSet = int(profGet)
    numGet = entry[2].get()
    if numGet == "":
        numGet = 1
    numSet = int(numGet)
    if numSet <= 0:
        numSet = 1
    rollOGet = entry[3].get()
    if rollOGet == "":
        rollOGet = 0
    rollOSet = int(rollOGet)
    bonusRGet = entry[4].get()
    if bonusRGet == "":
        bonusRGet = 0
    bonusRSet = int(bonusRGet)
    CurrentResult.clear()
    AllRolls.clear()
    AllRolls.append(f'Name: {setName}')
    s = 0
    for i in range(numSet):
        a ,b = RollRange[inddex]
        x = random.randint(a, b)
        if x + bonusRSet <= rollOSet:
            x = 0
            bonusRSet = 0
        AllRolls.append(f' {x + bonusRSet}')
        s += x + bonusRSet
        if b <=2:
            break
        i += 1
    CurrentResult.append(f'result:{s + profSet}')
    AllRolls.append(f'result: {s + profSet}')
    AllRolls.append(f'+ {profSet} ')
    HistoryOutput.insert('1.0', AllRolls)
    HistoryOutput.insert('1.0', '\n')
    CurrentResultOutput.delete('1.0', END)
    CurrentResultOutput.insert('1.0', CurrentResult)
#----------------------------------------------------------------Functions that call Rolling with different ranges(for buttons)
def d2():
    Rolling(0)
def d3():
    Rolling(1)
def d4():
    Rolling(2)
def d6():
    Rolling(3)
def d8():
    Rolling(4)
def d10():
    Rolling(5)
def d12():
    Rolling(6)
def d20():
    Rolling(7)
def d100():
    Rolling(8)
#---------------------------------------------------- Clean up roll Log + function arr
def CleanUp():
    HistoryOutput.delete('1.0',END)
funcs = [d2,d3,d4,d6,d8,d10,d12,d20,d100,CleanUp,"d2","d3","d4","d6","d8","d10","d12","d20","d100","Clean"]
#------------------------------------------------------------------Button set and labeling.
for i in range(10):
    y = 0
    btn = Button(root, text = f'{funcs[i+10]}', command = funcs[i], style='W.TButton')
    if i == 9:
        y = 500
    btn.place(x = 0, y = y + 50*i,width=180,height=50)
#---------------------------------Main loop for the window
root.mainloop()



