import turtle
arrData = []

turtle.bgcolor("gray80")
turtle.tracer(0, 0)
t = turtle.Turtle()
t.hideturtle()
step = 4

def writeDot(obj, rad, color):
    obj.pendown()
    obj.dot(rad, color)
    obj.penup()

def modify(ln):
    mod_string = ""
    badChars = ['"', ','] 
    ln = ln.strip() 
    for c in ln:
        if c not in badChars:
            mod_string = mod_string + c
    return mod_string 

fh = open("boris_natasha_mod.xpm", "r") 
color_data = fh.readline()
color_data = (modify(color_data))
[cols, rows, colors] = color_data.split()
rows = int(rows)
cols = int(cols)
colors = int(colors)
colorData = {}

for i in range(colors):
    cLine = fh.readline()
    cLine = modify(cLine)
    [sym, c, color] = cLine.split()
    colorData[sym] = color 
  
for i in range(rows):
    gLine = fh.readline()
    gLine = modify(gLine)
    arrData.append(gLine) 
 
for i in range(len(arrData)):
    print(arrData[i])
    
print(colorData)
print(cols, rows, colors)

t.penup() 
t.forward(int((cols/2)*(-1))*step)
t.left(90)
t.forward(int(rows/2)*step)
t.right(90)

for i in range(len(arrData)):
    line = arrData[i]
    for j in range(len(line)):
        if (line[j] == " "):
            writeDot(t, step, "black")
            t.forward(step)
        else:
            writeDot(t, step, colorData[line[j]])
            t.forward(step)
    t.forward(int((cols)*(-1))*step)
    t.right(90)
    t.forward(step)
    t.left(90)
    
turtle.update() 
