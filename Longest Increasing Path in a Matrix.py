import numpy as np
import pandas as pd

yn = 'y'
print('When the rows are finished, press "Enter".\nCaution: Note that every row must has the same length of other rows!')
while yn.lower()== 'y':
    Rows = ''
    while Rows == '':
        Rows = input('Enter first row of the matrix (elements be separated by space): ')

#Creating Matrix as an array
    MatArr = []
    while Rows != '':
        Lists = Rows.split()
        for k in range(len(Lists)):
            Lists[k] = int(Lists[k])
        MatArr.append(Lists)
        Rows = input('Enter next row of the matrix (elements be separated by space): ')
        if len(list(map(lambda x: int(x),Rows.split()))) != len(Lists):
            break
    Mtrx = np.array(MatArr)
    m = Mtrx.shape[0]
    n = Mtrx.shape[1]
    print('The matrix is:\n',Mtrx)

#Creating a dictionary to map indexes around a given position to that position
    dictall = {}
    for i in range(m):
        for j in range(n):
            d = []
            for k in [(i-1,j),(i,j+1),(i+1,j),(i,j-1)]:
                if k[0]>=0 and k[1]>=0 and k[0]<m and k[1]<n:
                    d.append(k)
            dictall[(i,j)] = d

#Creating a dictionary to map indexes around a given position with greater amount to that position
    dictg = {}
    for i in range(m):
        for j in range(n):
            listg = []
            for k in range(len(dictall[(i,j)])):
                if MatArr[dictall[(i,j)][k][0]][dictall[(i,j)][k][1]]>MatArr[i][j]:
                    listg.append(dictall[(i,j)][k])
            dictg[(i,j)] = listg

#Creating a list of all increasing paths as lists of position indexes
    Startpath = []
    for i in range(m):
        for j in range(n):
            if dictg[(i,j)] != []:
                Startpath.append([(i,j)])
    Pathl = Startpath.copy()
    for k in range(m*n-1):
        Startpath = Pathl
        for i in range(len(Startpath)):
            if dictg[Startpath[i][-1]] != []:
                for j in range(len(dictg[Startpath[i][-1]])):
                    Pathl.append(Startpath[i]+[dictg[Startpath[i][-1]][j]])
    Lenlist = list(map(lambda x:len(x),Pathl))

#Choosing one of the increasing paths with longest length, as a list of position indexes
    if m != 1 or n != 1:
        Pos = list(filter(lambda x: len(x)==max(Lenlist),Pathl))[0]
    else:
        Pos = [(0,0)]

#Creating the corresponding longest paths with matrix numbers
    Longest = list(map(lambda x:Mtrx[x[0],x[1]],Pos))
    print('The longest increasing path is: ',Longest)
    yn = ''
    while yn not in ['Y','y','N','n']:
        yn = input('Do want to start again? (y/n): ')
    




