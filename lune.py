import turtle
import math

turtle.setworldcoordinates(-500000000,-500000000,500000000,500000000)


# création de la Lune

t1=turtle.Turtle()  
t1.shape('circle')
t1.color('grey')
t1.speed(400)
t1.shapesize(1)

# création de la Terre

t2=turtle.Turtle()  
t2.shape('circle')
t2.color('blue')
t2.speed(400)
t2.shapesize(3)

# création de la fusée

t3=turtle.Turtle()
t3.color('red')
t3.speed(400)

# données de la fusée
   
F=9000000 # norme du vecteur vitesse constant
xx=0
yy=0
Vx=0
Vy=F

# donnés astronomiques

m= 7*10**22
G= 6.67*10**-11
M=6*10**24


# initialisation des données de la lune

x=0        
y=450000000
vx=1000
vy=0
ax=0
ay=0
dt = 10000

t1.pu()
t1.goto(x,y)
t1.pd()


    


for i in range (1000000):

    ax = -( G*M*x)/(x**2+y**2)**1.5
    ay = -( G*M*y)/(x**2+y**2)**1.5
    vx=ax*dt+vx
    vy=ay*dt+vy
    x=vx*dt+x
    y=vy*dt+y
    t1.goto(x,y)

    r=math.sqrt((xx-x)**2+(yy-y)**2)
    Vx=-F*(xx-x)/r
    Vy=-F*(yy-y)/r
    xx=Vx+xx
    yy=Vy+yy
    t3.goto(xx,yy)








turtle.exitonclick()
