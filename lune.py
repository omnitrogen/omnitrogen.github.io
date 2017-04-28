import turtle
import math

turtle.setworldcoordinates(-500000000,-500000000,500000000,500000000)

#soleil
ts = turtle.Turtle()
ts.shape('circle')
ts.color('yellow')
ts.speed(400)
ts.shapesize(2)

#lune
t1 = turtle.Turtle()  
t1.shape('circle')
t1.color('grey')
t1.speed(400)
t1.shapesize(3)

#terre
t2=turtle.Turtle()  
t2.shape('circle')
t2.color('blue')
t2.speed(400)
t2.shapesize(1)

#donnees
m= 7*10**22
G= 6.67*10**-11
M=6*10**24

#terre init
x=0        
y=400000000
vx=1000
vy=0
ax=0
ay=0
dt = 10000

#lune init
X= 0 
Y= int(y + 1000)
vX= vx + 500
vY=0
aX=0
aY=0
dT = 10000

#soleil data
#ts.pu()
#ts.goto(xx,yy)
#ts.pd()

for i in range (1000000):

   ts.goto(0,0)
   ax = -( G*M*x)/(x**2+y**2)**1.5
	ay = -( G*M*y)/(x**2+y**2)**1.5
	vx+=ax*dt
	vy+=ay*dt
   x+=vx*dt
   y+=vy*dt
	t2.goto(x,y)

	aX = -(G*M*X)/(X**2+Y**2)**1.5
   ay = -(G*M*Y)/(X**2+Y**2)**1.5
   vX+=aX*dt
   vY+=aY*dt
   X+=vX*dt
   Y+=vY*dt
   t1.goto(X,Y)

turtle.exitonclick()
