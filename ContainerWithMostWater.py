Height = input('Heights (List) = ')
Hlist = []
Vol = []
for i in range(1,len(Height),2):
    Hlist.append(int(Height[i]))
for i in range(len(Hlist)-1):
    for j in range(i+1,len(Hlist)):
        Vol.append((j-i)*min(Hlist[i],Hlist[j]))
print(max(Vol))