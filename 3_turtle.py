# draw any polygon in turtle
  
import turtle
  
# creating turtle pen
turtle.shape('turtle')
  
# taking input for the no of the sides of the polygon
#n = int(input("Enter the no of the sides of the polygon : "))
  
# taking input for the length of the sides of the polygon
#l = int(input("Enter the length of the sides of the polygon : "))
l=20
for n in range (3,10):
  
    for _ in range(n):
        turtle.forward(l+2*n)
        turtle.right(360 / n)
    n+=1