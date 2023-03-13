x=int(input("Enter x coordinate: "))
y=int(input("Enter y coordinate: "))

if x>0 and y>0:
    print(f"Point P({x},{y}) is in the first quadrant of the coordinate system.")
    
elif x<0 and y>0:
    print(f"Point P({x},{y}) is in the second quadrant of the coordinate system.")
    
elif x<0 and y<0:
    print(f"Point P({x},{y}) is in the third quadrant of the coordinate system.")
    
elif x>0 and y<0:
    print(f"Point P({x},{y}) is in the fourth quadrant of the coordinate system.")
    
elif x>0 and y==0:
    print(f"Point P({x},{y}) is on the positive side of x-axis.")
    
elif x==0 and y>0:
    print(f"Point P({x},{y}) is on the positive side of y-axis.")
    
elif x<0 and y==0:
    print(f"Point P({x},{y}) is on the negative side of x-axis.")
    
elif x==0 and y<0:
    print(f"Point P({x},{y}) is on the negative side of y-axis.")
    
elif x==0 and y==0:
    print(f"Point P({x},{y}) is in the origin.")