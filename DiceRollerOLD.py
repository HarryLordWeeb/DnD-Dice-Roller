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
#---------------------------------------------------------------Input fields
L1 = ttk.Label(root,font = ('Calibri',14, 'bold'), text="Name:")
L1.place(x=5,y=520)
PlayerNameInput = ttk.Entry(root, font=('Calibri',20, 'bold'),width=12)
PlayerNameInput.place(x=0,y=550)
L2 = ttk.Label(root,font = ('Calibri',14, 'bold'), text="Proficiency bonus:")
L2.place(x=5,y=600)
ProficiencyInput = ttk.Entry(root, font=('Calibri',20, 'bold'),width=12)
ProficiencyInput.place(x=0,y=625)
L3 = ttk.Label(root,font = ('Calibri',14, 'bold'), text="Number of rolls:")
L3.place(x=5,y=675)
NumberOfRollsInput = ttk.Entry(root, font=('Calibri',20, 'bold'),width=12)
NumberOfRollsInput.place(x=0,y=700)
L4 = ttk.Label(root,font = ('Calibri',14, 'bold'), text="Need to roll over:")
L4.place(x=5,y=750)
NeedToRollOverInput = ttk.Entry(root, font=('Calibri',20, 'bold'),width=12)
NeedToRollOverInput.place(x=0,y=775)
L5 = ttk.Label(root,font = ('Calibri',14, 'bold'), text="Bonus on every roll:")
L5.place(x=5,y=820)
BonusOnRollInput = ttk.Entry(root, font=('Calibri',20, 'bold'),width=12)
BonusOnRollInput.place(x=0,y=850)
#----------------------------------------------------------------Dice dictrionary, empty arrays and ranges.
Dice = {
    "d2": 0,
    "d3": 1,
    "d4": 2,
    "d6": 3,
    "d8": 4,
    "d10": 5,
    "d12": 6,
    "d20": 7,
    "d100":8
}
CurrentResult = []
AllRolls = []
RollRange = [ (1,2) , (1,3) , (1,4) , (1,6) , (1,8) , (1,10) , (1,12) , (1,20) , (1,100) ]
#-----------------------------------------------------------------------Rolling function + logic for inputs
def Rolling(inddex):
    nameGet = PlayerNameInput.get()
    setName= str(nameGet)
    profGet = ProficiencyInput.get()
    if profGet == "":
        profGet = 0
    profSet = int(profGet)
    numGet = NumberOfRollsInput.get()
    if numGet == "":
        numGet = 1
    numSet = int(numGet)
    if numSet <= 0:
        numSet = 1
    rollOGet = NeedToRollOverInput.get()
    if rollOGet == "":
        rollOGet = 0
    rollOSet = int(rollOGet)
    bonusRGet = BonusOnRollInput.get()
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
    Rolling(Dice['d2'])
def d3():
    Rolling(Dice['d3'])
def d4():
    Rolling(Dice['d4'])
def d6():
    Rolling(Dice['d6'])
def d8():
    Rolling(Dice['d8'])
def d10():
    Rolling(Dice['d10'])
def d12():
    Rolling(Dice['d12'])
def d20():
    Rolling(Dice['d20'])
def d100():
    Rolling(Dice['d100'])
#---------------------------------------------------- Clean up roll Log
def CleanUp():
    HistoryOutput.delete('1.0',END)
#------------------------------------------------------------------Button set and labeling.
d21 = Button(root, text = 'D2 ', command = d2, style='W.TButton') 
d21.place(x = 0,y = 0,width=180,height=50)
d31 = Button(root,text="D3 ", style='W.TButton', command=d3)
d31.place(x = 0, y = 50,width=180,height=50)
d41 = Button(root,text="D4 ", style='W.TButton', command=d4)
d41.place(x = 0,y = 100,width=180,height=50)
d61 = Button(root, text="D6 ", style='W.TButton', command=d6)
d61.place(x=0,y=150,height=50,width=180)
d81 = Button(root,text='D8 ', style='W.TButton', command=d8)
d81.place(x=0,y=200, height=50,width=180)
d101 = Button(root,text='D10 ', style='W.TButton', command=d10)
d101.place(x=0,y=250, height=50,width=180)
d121 = Button(root,text='D12 ', style='W.TButton', command=d12)
d121.place(x=0,y=300, height=50,width=180)
d201 = Button(root,text='D20 ', style='W.TButton', command=d20)
d201.place(x=0,y=350, height=50,width=180)
d1001 = Button(root,text='D100', style='W.TButton', command=d100)
d1001.place(x=0,y=400, height=50,width=180)
Cleaning = Button(root, text='clean', style='W.TButton', command= CleanUp)
Cleaning.place(x=0,y=950,height=50,width=180)
#---------------------------------Main loop for the window
root.mainloop()



