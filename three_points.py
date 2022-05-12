def colinear(xa,ya,xb,yb,xc,yc):
    return (int(xb)-int(xa))*(int(yc)-int(ya)) == (int(yb)-int(ya))*(int(xc)-int(xa))

x1, y1 = input().split()
x2, y2 = input().split()
x3, y3 = input().split()
print(colinear(x1,y1,x2,y2,x3,y3))