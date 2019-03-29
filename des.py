
#1-indexed
PC_1 = [[57,49,41,33,25,17,9],[1,58,50,42,34,26,18], [10,2,59,51,43,35,27], [19,11,3,60,52,44,36], [63,55,47,39,31,23,15], [7,62,54,46,38,30,22], [14,6,61,53,45,37,29], [21,13,5,28,20,12,4]]
IP = [58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]
iterBlocks = [[1,1],[2,1],[3,2],[4,2],[5,2],[6,2],[7,2],[8,2],[9,1],[10,2],[11,2],[12,2],[13,2],[14,2],[15,2],[16,1]]
PC_2 = [14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]
s_box= []
s_box.append([[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]])
s_box.append([[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]])
s_box.append([[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]])
s_box.append([[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]])
s_box.append([[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]])
s_box.append([[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]])
s_box.append([[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]])
s_box.append([[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]])


#0-indexed
E = [31,  0,  1,  2,  3,  4,  3,  4,  5,  6,  7,  8,  7,  8,  9, 10, 11, 12, 11, 12, 13, 14, 15, 16, 15, 16, 17, 18, 19, 20, 19, 20, 21, 22, 23, 24, 23, 24, 25, 26, 27, 28, 27, 28, 29, 30, 31,  0]
P = [15,  6, 19, 20, 28, 11, 27, 16,  0, 14, 22, 25,  4, 17, 30,  9,  1,7, 23, 13, 31, 26,  2,  8, 18, 12, 29,  5, 21, 10,  3, 24]
IP_INV=[39,  7, 47, 15, 55, 23, 63, 31, 38,  6, 46, 14, 54, 22, 62, 30, 37,5, 45, 13, 53, 21, 61, 29, 36,  4, 44, 12, 52, 20, 60, 28, 35,  3, 43, 11, 51, 19, 59, 27,34,  2, 42, 10, 50, 18, 58, 26, 33,  1, 41,9, 49, 17, 57, 25, 32,  0, 40,  8, 48, 16, 56, 24]

allKeys = []





def encode(M, K):
    subKeys(K)
    print('Cipher Text is:', encodeData(M))
    allKeys.clear()


def subKeys(K): #Generate all the keys (K1-K16)
    tmp = []

    #Generate permuted 56 bit key using PC-1
    for i in range(len(PC_1)):
        for j in range(len(PC_1[i])):
            tmp.append(K[PC_1[i][j] - 1])
    
    C = [] #To hold C1-C16
    D = [] #To hold D1-D16
    
    tmpC = tmp[:len(tmp)//2] #C0
    tmpD = tmp[len(tmp)//2:] #D0
    
    C.append(tmpC)
    D.append(tmpD)
    
    allCD = [] #To hold CnDn

    #Left shifting according to Iteration Blocks
    for i in range(len(iterBlocks)):
        lShift = iterBlocks[i][1]
        tmpC = C[iterBlocks[i][0]-1][lShift:]
        tmpC += C[iterBlocks[i][0]-1][0:lShift]
        C.append(tmpC)
        tmpD = D[iterBlocks[i][0]-1][lShift:]
        tmpD += D[iterBlocks[i][0]-1][0:lShift]
        D.append(tmpD)
    
    #Combine all Cs and Ds
    for i in range(len(C)):
        allCD.append(C[i]+D[i])
    
    #Permute to 48 bit block size using PC-2
    for i in range(1,len(allCD)):
        tmpKey = []
        for j in PC_2:
            tmpKey.append(allCD[i][j-1]) #PC-2 is 1-indexed, hence -1
        allKeys.append(tmpKey)
    
    
def encodeData(M):
    newM = []

    #Apply initial permutation
    for j in IP:
        newM.append(M[j-1])
    
    L0 = newM[:len(newM)//2] #L0
    R0 = newM[len(newM)//2:] #R0
    it = 1
    while(it<=16): #16 Rounds
        L1 = R0[:]
        f = calcF(L1,allKeys[it-1])
        R1 = []
        for x in range(len(f)):
            R1.append(int(L0[x]) ^ int(f[x]))
        L0 = L1[:]
        R0 = R1[:]
        it+=1
    
    M = R0+L0 #Reverse L16R16
    encM = []
    #Apply IP inverse permutation
    for y in IP_INV:
        encM.append(M[y])
    #Convert cipher text to hex
    hexVal = "".join(map(str, encM))
    hexVal = hex(int(hexVal, 2))
    return hexVal[2:].upper()
    
def calcF(R0, K1):
    eR = []
    for j in E:
        eR.append(R0[j])
    res = []
    for j in range(len(eR)):
        res.append(int(eR[j])^int(K1[j]))
    finalRes = []
    for i in range(8):
        B = res[i*6:(i+1)*6]
        row = int(str(B[0]) + str(B[-1]),2)
        col = int(str(B[1]) + str(B[2]) + str(B[3]) + str(B[4]),2)
        val = s_box[i][row][col]
        val = f'{val:04b}'
        finalRes.append(list(val))
    finalRes = [item for sublist in finalRes for item in sublist]
    res = []
    for j in P:
        res.append(finalRes[j])
    return res

if __name__ == '__main__':
    #input is a hex
    #M = input('Enter the message to encrypt in hex (16-bit): ')
    M = '0123456789ABCDEF'
    M = bin(int(M, 16))[2:]

    if len(M) < 64:
        M = '0'*(64-len(M)) + M
        

    
    #K = input('Enter the key to use in hex (16-bit): ')

    K = '133457799BBCDFF1'
    K = bin(int(K,16))[2:]
    if len(K) < 64:
        K = '0'*(64-len(K)) + K
    encode(M,K)



    
    
