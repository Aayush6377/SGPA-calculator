import numpy as np, pandas as pd
import matplotlib.pyplot as plt
import random as rd

name=str(input("Enter your name:"))
n=int(input("Enter Number of Subjects:"))
data=pd.DataFrame(columns=["Subject","Credit","Internals","Externals","Grade","Grade point"],index=np.arange(0,n))

percentage=[]
perlist=[95,85,75,65,55,45,40,0]
gra={0:["O",10],1:["A+",9],2:["A",8],3:["B+",7],4:["B",6],5:["C",5],6:["P",4],7:["F",0]}
print("Note: Internal and External marks should be in the form a/b where a is marks obtained out of b")
print("If Student is absent than type Ab/b where b is MM of paper")
for i in range(n):
    print("Enter",i+1,"Subject name:",end="")
    data.loc[i,"Subject"]=str(input())
    print("Enter ",data.loc[i,"Subject"],"credit:",end="")
    data.loc[i,"Credit"]=int(input())
    data.loc[i,"Internals"]=str(input("Enter internal marks:"))
    data.loc[i,"Externals"]=str(input("Enter external marks:"))
    
    if data.loc[i,"Internals"][0:data.loc[i,"Internals"].index('/')].upper()=="AB":
        data.loc[i,"Internals"]="0" + data.loc[i,"Internals"][data.loc[i,"Internals"].index('/'):]
    if data.loc[i,"Externals"][0:data.loc[i,"Externals"].index('/')].upper()=="AB":
        data.loc[i,"Externals"]="0" + data.loc[i,"Externals"][data.loc[i,"Externals"].index('/'):]

    
    markin=int(data.loc[i,"Internals"][0:data.loc[i,"Internals"].index('/')])
    markex=int(data.loc[i,"Externals"][0:data.loc[i,"Externals"].index('/')])
    total=int(data.loc[i,"Internals"][data.loc[i,"Internals"].index('/')+1:])+int(data.loc[i,"Externals"][data.loc[i,"Externals"].index('/')+1:])
    per=((markin+markex)/total)*100
    percentage.append(int(per))
    for j in perlist:
        if per>=j:
            data.loc[i,"Grade"]=gra[perlist.index(j)][0]
            data.loc[i,"Grade point"]=int(gra[perlist.index(j)][1])
            break
    print("\n",end="")
    
print(data)
num=0
for i in range(n):
    num+=data.loc[i,"Credit"]*data.loc[i,"Grade point"]
sgpa=num/(sum(data.loc[:,"Credit"]))
print("SGPA:",round(sgpa,2))

if sgpa>9:
    print("Congratulations",name.capitalize(),"you have got 9+ sgpa.")
elif sgpa>=7 and sgpa<=9:
    print(name.capitalize(),"your scholarship is save.")
elif sgpa<7 and sgpa>=4:
    print("Sorry your scholarship is gone but still you have passed.")
elif sgpa<4:
    print("You have failed, perform your best next time.")
    
data.loc[n,"Grade"]="SGPA"
data.loc[n,"Grade point"]=round(sgpa,2)
data.to_csv(name+"'s report card"+".csv",index=False)

co=["r","b","g","c","m","y","k","purple","orange","brown","pink","olive"]
plt.barh(data.loc[:n-1,"Subject"],percentage,color=rd.choice(co),height=0.5)
plt.xlabel("Performance")
plt.ylabel("Subjects")
plt.title(name+"'s report graph")
plt.show()
