
########### VERSION 1 ###############################
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

########### VERSION 2 ###############################

a1=[1,2,3,4]
a2=[-1,0,1,-2]
a3=[-1,-2,0,3]
x1=[]

for x in range(0,len(a1)):
  ecuacion = 3*a1[x]-2*a2[x]+4*a3[x]
  x1.append(ecuacion)    

print(x1)