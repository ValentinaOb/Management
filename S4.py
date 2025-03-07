def key_gen(key):
    P10=(key[2],key[4],key[1],key[6],key[3],
         key[9],key[0],key[8],key[7],key[5])
    
    key1 = [P10[i] for i in (0,1,2,3,4)]
    key2 = [P10[i] for i in (5,6,7,8,9)]
    print('Key1: ',key1)
    print('Key2: ',key2)

    new_key1=[]
    new_key2=[]

    if len(key1) > 1:
        new_key1.extend(key1[1:] + [key1[0]])
    if len(key2) > 1:
        new_key2.extend(key2[1:] + [key2[0]])
        
    print('N_Key1: ',new_key1)
    print('N_Key2: ',new_key2)

    new_key = new_key1+new_key2

    P8=(new_key[5],new_key[2],new_key[6],new_key[3],
        new_key[7],new_key[4],new_key[9],new_key[8])
    
    k1=P8

    #2st

    new_key1.clear()
    new_key2.clear()
    if len(key1) > 1:
        new_key1.extend(key1[2:] + key1[:2])
    if len(key2) > 1:
        new_key2.extend(key2[2:] + key2[:2])

    print('2 N_Key1: ',new_key1)
    print('2 N_Key2: ',new_key2)

    new_key = new_key1+new_key2

    P8=(new_key[5],new_key[2],new_key[6],new_key[3],
        new_key[7],new_key[4],new_key[9],new_key[8])
    
    k2=P8
    print('K1: ',k1)
    print('K2: ',k2)
    print('\n\n')

    return k1, k2
        


def xor(key, l,r):

    EP=(r[3],r[0],r[1],r[2],
        r[1],r[2],r[3],r[0])

    p=[]
    for i in range(8):
        p.append(key[i] ^ EP[i])
    
    #print('P: ',p)
    
    indx= int(''.join(map(str, (p[0],p[3]))), 2)
    indx1= int(''.join(map(str, (p[1],p[2]))), 2)
    print('S0, row: ', p[0],p[3], ' - ', indx)
    print('S0, col: ', p[1],p[2], ' - ', indx1)

    indx2= int(''.join(map(str, (r[0],r[3]))), 2)
    indx3= int(''.join(map(str, (r[1],r[2]))), 2)
    print('\nS1, row: ', r[0],r[3], ' - ', indx2)
    print('S1, col: ', r[1],r[2], ' - ', indx3)

    el_S0=format(S0[indx][indx1], 'b')
    el_S1=format(S1[indx2][indx3], 'b')

    if el_S0=='1':
        el_S0='01'
    elif el_S0=='0':
        el_S0='00'
    if el_S1=='1':
        el_S1='01'
    elif el_S1=='0':
        el_S1='00'

    #print('Combining S0 & S1: ',S0[indx][indx1], S1[indx2][indx3], '-', el_S0, el_S1)
    P4_list=list(map(int, str(el_S0)))
    P4_list.extend(list(map(int, str(el_S1))))

    #print('P4_list: ', P4_list)
    P4=[P4_list[1],P4_list[3],P4_list[2],P4_list[0]]
    print('Fk = P4:',P4)


    new_l=[]
    for i in range(4):
        #p.append(text[i] ^ EP[i])
        new_l.append(l[i] ^ P4[i])    

    print('new_l: ',new_l, '    r: ',r)

    return new_l,r




def DES_E(text, key1, key2):
    IP=(text[1],text[5],text[2],text[0],
        text[3],text[7],text[4],text[6])
    
    l = [IP[i] for i in (0,1,2,3)]
    r = [IP[i] for i in (4,5,6,7)]

    l1,r1=xor(key1,l,r)

    new_l,new_r=xor(key2,r1,l1) # L-r1, R-l1 (SW)

    l_r=new_l+ new_r
    print('L_R: ',l_r)
    
    IP_1=(l_r[3],l_r[0],l_r[2],l_r[4],
        l_r[6],l_r[1],l_r[7],l_r[5])
    print('Cipher: ', IP_1)

    return IP_1


def DES_D(text, key1, key2):
    #   Decrypted
    IP=(text[1],text[5],text[2],text[0],
        text[3],text[7],text[4],text[6])
    
    l = [IP[i] for i in (0,1,2,3)]
    r = [IP[i] for i in (4,5,6,7)]

    l1,r1=xor(key1,l,r)

    new_l,new_r=xor(key2,r1,l1) # L-r1, R-l1 (SW)

    l_r=new_l + new_r
    print('\nL_R: ',l_r)
    
    IP_1=(l_r[3],l_r[0],l_r[2],l_r[4],
        l_r[6],l_r[1],l_r[7],l_r[5])
    print('Decrypted: ', IP_1)

    return IP_1




S0=([1,0,3,2],
        [3,2,1,0],
        [0,2,1,3],
        [3,1,3,2])

S1=([0,1,2,3],
        [2,0,1,3],
        [3,0,1,0],
        [2,1,0,3])


#text=(1,0,0,1,0,1,1,1)
#key = (1,0,1,0,0,1,0,0,1,1)


correct=False
while not correct:
    key = tuple(map(int, input("Enter key (10): ").split()))
    if len(key)!=10:
        print('Length not 10')
    elif not all(num in (0, 1) for num in key):
        print('Only 0 / 1')
    else:
        correct=True

correct=False

while not correct:
    text = tuple(map(int, input("Enter elements separated by spaces (8): ").split()))
    if len(text)!=8:
        print('Length not 8')
    elif not all(num in (0, 1) for num in text):
        print('Only 0 / 1')
    else:
        correct=True
    

key1, key2 = key_gen(key)

cipher = DES_E(text, key1, key2)
print('\n\n')

text1 = cipher    #text=IP_1
decrypted = DES_D(text1, key2, key1)

print("\n\nKey1: ", key1)
print("Key2: ", key2)
print("Text: ", text)

print("\nCipher: ", cipher)
print("Decrypted", decrypted)