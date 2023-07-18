from turtle import *
import math

def tree(n, l, pen):
    if n==0 or l<2 :
        return
    #endif
    pen.forward(l)
    pen.left(45)
    tree(n-1, l/2, pen)
    pen.right(90)
    tree(n-1, l/2, pen)
    pen.left(45)
    pen.backward(l)

#end 

def tree4(n, l, pen):
    if n==0 or l<2 :
        return
    #endif
    pen.forward(l)
    pen.left(90)
    tree4(n-1, l/2, pen)
    pen.right(60)
    tree4(n-1, l/2, pen)
    pen.right(60)
    tree4(n-1, l/2, pen)
    pen.right(60)
    tree4(n-1, l/2, pen)
    pen.left(90)
    pen.backward(l)

#end


def fern(n, l, pen):
    if n==0 or l<2 :
         return
    #endif
    pen.forward(0.3*l)
    pen.left(55)
    fern(n-1, l/2, pen)
    pen.right(55)
    pen.forward(0.7*l)
    pen.right(40)
    fern(n-1, l/2, pen)
    pen.left(40)
    pen.forward(l)
    pen.left(5)
    fern(n-1, 0.8*l, pen)
    pen.right(5)
    pen.backward(2*l)
    
#end

def koch(n, l, pen):
    #termination
    if n==0 or l<2 :
         pen.forward(l)
         return
    #endif
    koch(n-1,l/3, pen)
    pen.left(60)
    koch(n-1,l/3, pen)
    pen.right(120)
    koch(n-1,l/3, pen)
    pen.left(60)
    koch(n-1,l/3, pen)

#end

def flake(n, l, pen):
    for i in range(3):
        koch(n,l, pen)
        pen.right(120)
    #endfor

#end

def antiflake(n, l, pen):
    for i in range(3):
        koch(n,l, pen)
        pen.left(120)
    #endfor

#end

def sierpinski(n, l, pen):
    #termination
    if n==0 or l<2 :
        return
    #endif
    sierpinski(n-1,l, pen)
    pen.right(45)
    pen.forward(l)
    pen.right(45)
    sierpinski(n-1,l, pen)
    pen.left(90)
    pen.forward(l)
    pen.left(90)
    sierpinski(n-1,l, pen)
    pen.right(45)
    pen.forward(l)
    pen.right(45)
    sierpinski(n-1,l, pen)
#end


def s_carpet(n, l, pen):
    for i in range(4):
        sierpinski(n, l, pen)
        pen.right(45)
        pen.forward(l)
        pen.right(45)
    #endfor
#end

def s_gasket(n,l, pen):
    #termination
    if n==0 or l<2 :
        return
    #endif
    for i in range(3):
        s_gasket(n-1,l/2, pen)
        pen.forward(l)
        pen.left(120)
    #endfor
#end

def swiss_gasket(n, l, pen):
    #termination
    if n==0 or l<2 :
        return
    #endif
    for i in range(4):
        swiss_gasket(n-1,l/3, pen)
        pen.forward(l)
        pen.left(90)
    #endfor
#end

def pent(n, l, pen):
    #termination
    if n==0 or l<2 :
        return
    #endif
    for i in range(5):
        pent(n-1,0.382*l, pen)
        pen.forward(l)
        pen.left(72)
    #endfor
#end

    
def c_curve(n, l, pen):
    #termination
    if n==0 :
         pen.forward(l)
         return
    #endif
    c_curve(n-1,l, pen)
    pen.right(90)
    c_curve(n-1,l, pen)
    pen.left(90)
#end

def circles(n, l, pen):
    #termination
    if n==0 or l<2 :
        return
    #endif
    for i in range(6):
        pen.circle(l/3,180)
        pen.right(180)
        pen.circle(l/3)
        pen.left(180)
        pen.circle(l/3,180)
        pen.circle(l/3)
        pen.circle(l,19.8)
        pen.circle(0.057*l)
        pen.circle(l,10.2)
        pen.circle(0.118*l)
        pen.circle(l,10.2)
        pen.circle(0.057*l)
        pen.circle(l,19.8)
    #endfor
    for i in range(6):
        circles(n-1,l/3, pen)
        pen.circle(l,19.8)
        circles(n-1,0.057*l, pen)
        pen.circle(l,10.2)
        circles(n-1,0.118*l, pen)
        pen.circle(l,10.2)
        circles(n-1,0.057*l, pen)
        pen.circle(l,19.8)
    #endfor
    pen.circle(l/3,180)
    pen.right(180)
    circles(n-1,l/3, pen)
    pen.left(180)
    pen.circle(l/3,180)
    
#end


def diamond(n, l, pen):
    #termination
    if n==0 or l<2 :
        return
    #endif
    diamond(n-1, l/2, pen)
    pen.forward(l*0.288675)
    diamond(n-1, l/2, pen)
    pen.forward(l*0.288675)
    pen.right(60)
    pen.forward(l*0.57735)
    pen.right(120)
    diamond(n-1, l/2, pen)
    pen.forward(l*0.288675)
    diamond(n-1, l/2, pen)
    pen.forward(l*0.288675)
    pen.right(60)
    pen.forward(l*0.57735)
    pen.right(120)
#end


def pinwheel(n, l, pen):
    #termination
    if n==0 or l<2 :
        return
    #endif
    for i in range(4): 
        pen.left(30)        
        pen.forward(l)
        pen.right(60)
        pen.forward(l)
        pen.right(120)
        pen.forward(l)
        pen.right(60)
        pen.forward(l)
        pen.left(120)
    #end for
    pen.left(30)
    pinwheel(n-1, l*0.57735, pen)
    pen.left(150)
#end


def star(n, l, pen):
    #termination
    if n==0 or l<2 :
        return
    #endif
    for i in range(6): 
        pen.left(30)        
        pen.forward(l)
        pen.right(60)
        pen.forward(l)
        pen.right(120)
        pen.forward(l)
        pen.right(60)
        pen.forward(l)
        pen.left(150)
    #end for
    pen.left(30)
    star(n-1, l*0.57735, pen)
    pen.right(30)
#end

def diamond_cube(n, l, pen):
    #termination
    if n==0 or l<2 :
        return
    #endif
    pen.left(45)
    for i in range(3):
        diamond(n, l, pen)
        pen.right(30)
        pen.up()
        pen.forward(l)
        pen.down()
        pen.right(90)
    pen.right(45)
#end

def diamond_eye(n, l, pen):
    #termination
    if n==0 or l<2 :
        return
    #endif
    pen.left(30)
    diamond_eye(n-1,l*0.57735, pen)
    pen.forward(l/2)
    pen.right(60)
    diamond_eye(n-1,l*0.57735, pen)
    pen.forward(l/2)
    pen.right(120)
    diamond_eye(n-1,l*0.57735, pen)
    pen.forward(l/2)
    pen.right(60)
    diamond_eye(n-1,l*0.57735, pen)
    pen.forward(l/2)
    pen.right(150)

#end


       


    
    
    
