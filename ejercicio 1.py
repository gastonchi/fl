a1=[1,2,3,4]
a2=[-1,0,1,-2]
a3=[-1,-2,0,3]
x=[]
ecuacion = 0
i=0

while i < len(a1):
    ecuacion = 3*a1[i]-2*a2[i]+4*a3[i]
    x.append(ecuacion)
    i=i+1
    
print (x)