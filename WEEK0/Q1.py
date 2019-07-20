import numpy as np

matrixA = []
fileA = open('matrixA.txt')
for i in fileA:
    row = [int(x) for x in i.split(',')]
    matrixA.append(row)

matrixB = []
fileB = open("matrixB.txt")
for i in fileB:
    row = [int(x) for x in i.split(",")]
    matrixB.append(row)

matrixA = np.array(matrixA)
matrixB = np.array(matrixB)

ans  = matrixA.dot(matrixB)
ans.sort(axis=1)

np.savetxt("Q1_ans.txt",ans,fmt="%d",delimiter="\r\n")
