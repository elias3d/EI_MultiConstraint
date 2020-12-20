# Step 1: Select all objects to be recive the constraint and the target as the last one in the selection. 
# Step 2: Choose one of the constraints
import maya.cmds as cmds

def constraint_parent():
    selList = cmds.ls(selection=True)
    parent = selList[-1]
    for index in range(0,len(selList)-1):
        loc = selList[index]

        cmds.parentConstraint (parent, loc, mo = True)

def constraint_point():
    selList = cmds.ls(selection=True)
    parent = selList[-1]
    for index in range(0,len(selList)-1):
        loc = selList[index]

        cmds.pointConstraint (parent, loc, mo = True)

def constraint_Orient():
    selList = cmds.ls(selection=True)
    parent = selList[-1]
    for index in range(0,len(selList)-1):
        loc = selList[index]

        cmds.orientConstraint (parent, loc, mo = True)

def constraint_Scale():
    selList = cmds.ls(selection=True)
    parent = selList[-1]
    for index in range(0,len(selList)-1):
        loc = selList[index]

        cmds.scaleConstraint (parent, loc, mo = True)
    
def constraint_Aim():
    selList = cmds.ls(selection=True)
    parent = selList[-1]
    for index in range(0,len(selList)-1):
        loc = selList[index]

        cmds.aimConstraint (parent, loc, mo = True)
    
def constraint_PoleVector():
    selList = cmds.ls(selection=True)
    parent = selList[-1]
    for index in range(0,len(selList)-1):
        loc = selList[index]

        cmds.poleVectorConstraint (parent, loc, mo = True)
    
    #create UI
def showui():
    # Delete if window already exists
    if cmds.window("EI_MultiConstraint", exists=True):
        cmds.deleteUI("EI_MultiConstraint")
    my_win = cmds.window("EI_MultiConstraint", title="EI_MultiConstraint", widthHeight=(400, 200))    
    column_main = cmds.columnLayout()
    cmds.text(label="") 
    cmds.text(label="Step 1: Select all objects to be recive the constraint")
    cmds.text(label="             and the target as the last one in the selection.")
    cmds.text(label="") 
    cmds.text(label="Step 2: Choose one of the following constraints") 
    cmds.text(label="")   
    cmds.rowColumnLayout( nc=2, cw=[(1, 200), (2, 200)] )
    cmds.button("Parent Constraint", command=lambda *args: constraint_parent())
    cmds.button("Point Constraint", command=lambda *args: constraint_point())
    cmds.separator()
    cmds.separator()
    cmds.button("Orient Constraint", command=lambda *args: constraint_Orient())
    cmds.button("Scale Constraint", command=lambda *args: constraint_Scale())
    cmds.separator()
    cmds.separator()
    cmds.button("Aim Constraint", command=lambda *args: constraint_Aim())


    cmds.showWindow(my_win)
    
showui()    

    
