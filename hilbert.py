import turtle as t

instructions = "+BF-AFA-FB+"

t.penup()
t.delay(0)
t.hideturtle() # hide turtle for more speed
t.goto(-350, -350)
t.pendown()
t.tracer(0, 0) # for more speed

def replace(instructions):
    x = ''
    for i in instructions:
        if i == "A":
            x += "+BF-AFA-FB+"
        elif i == "B":
            x += "-AF+BFB+FA-"
        else:
            x += i
    return x


for i in range(6):
    instructions = replace(instructions)
    print(len(instructions))


for i in instructions:
    if i == "+":
        t.left(90)
    elif i == "-":
        t.right(90)
    elif i == "F":
        t.forward(5.5)
    t.update() # update at the end for even more speed
t.mainloop()

