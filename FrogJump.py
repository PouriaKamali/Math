print('< Frog Jump Problem >')
Continue = 'Y'
while Continue in ['Y','y']:
    stonelist = [2]
    while 0 not in stonelist or 1 not in stonelist:
        print('NOTE: The list must has 0 and 1!')
        liststr = input('Enter stones\' index separated by space ')
        stonelist = liststr.split()
        myset = set()
        for k in range(len(stonelist)):
            stonelist[k] = int(stonelist[k])
        stonelist.sort()
        for item in stonelist:
            myset.add(item)
        stonelist = list(myset)
    print(stonelist)
    def eliminate(name):
        difference = []
        ddifference = []
        ind = []
        for i in range(len(stonelist)-1):
            difference.append(stonelist[i+1]-stonelist[i])
        for j in range(len(difference)-1):
            ddifference.append(abs(difference[j+1]-difference[j]))
        for k in range(len(ddifference)):
            if ddifference[k]>1:
                ind.append(k)
        if ind != []:
            del stonelist[min(ind)]
    for i in range(len(stonelist)):
        eliminate(stonelist)
    if 0 in stonelist and 1 in stonelist:
        print('The frog can cross the river in this way: ',stonelist)
    else:
        print('That\'s not possible for the frog to cross the river')
    Continue = ''
    while Continue not in ['Y','N','y','n']:
        Continue = input('Do you like to try again? (Y/N):')
