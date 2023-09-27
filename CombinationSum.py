import re, copy
InputCandidateslist = input()

# transform list of the string to the list of numbers
ListRegex = re.compile(r'\d+')
StringCandidateslist = ListRegex.findall(InputCandidateslist)
Candidateslist = list(set(map(lambda st:int(st),StringCandidateslist)))
NumberofCandidates = len(Candidateslist)


Target = int(input())

Maxtimes = list(map(lambda num : Target//num ,Candidateslist))# list of maximum possible repetitions of each Candidates in linear combinations

#By considering Maxtime, we construct a list of total cases that some of them might be a part of the result
def AddList(i,k):
    for j in range(1,Maxtimes[i]+1):
        list1 = copy.deepcopy(list2[k])
        list1[i] = j
        list2.append(copy.deepcopy(list1))

list1 = []
list2 = []
for i in range(NumberofCandidates):
    list1.append(0)
list2.append(copy.deepcopy(list1))

for i in range(NumberofCandidates):
    for k in (range(len(list2))):
        AddList(i,k)


#construct the result list
mylist = []
for i in range(len(list2)):
    sum = 0
    for j in range(NumberofCandidates):
        sum = sum + list2[i][j]*Candidateslist[j]
    if sum == Target:
        mylist.append(list2[i])


#show the result in the desired format
list4 = []
for i in mylist:
    list3 = []
    for j in range(NumberofCandidates):
        for k in range(i[j]):
            list3.append(Candidateslist[j])
    if list3 != []:
        list4.append(list3)
print(list4)
