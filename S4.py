def xor(key):
    p=[]
    l = [key[i] for i in (0,1,2,3)]
    r = [key[i] for i in (4,5,6,7)]
    
    EP=(l[3],l[0],l[1],l[2],
        l[1],l[2],l[3],l[0])
    
    for i in range(8):
        #p.append(text[i] ^ EP[i])
        p.append(key[i] ^ EP[i])
    
    print('P: ',p)

    #l = [p[i] for i in (0,1,2,3)]
    #r = [p[i] for i in (4,5,6,7)]
    #first= p[:4]
    #last= p[-4:]
    l = [p[i] for i in (0,1,2,3)]
    r = [p[i] for i in (4,5,6,7)]

    S0=([1,0,3,2],
        [3,2,1,0],
        [0,2,1,3],
        [3,1,3,2])

    S1=([0,1,2,3],
        [2,0,1,3],
        [3,0,1,0],
        [2,1,0,3])

    print('Li: ', l)
    indx= int(''.join(map(str, (l[0],l[3]))), 2)
    indx1= int(''.join(map(str, (l[1],l[2]))), 2)
    print('S0, row: ', l[0],l[3], ' - ', indx)
    print('S0, col: ', l[1],l[2], ' - ', indx1)

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

    print('Combining S0 & S1: ',S0[indx][indx1], S1[indx2][indx3], '-', el_S0, el_S1)
    P4_list=list(map(int, str(el_S0)))
    P4_list.extend(list(map(int, str(el_S1))))
    print('P4_list: ', P4_list)
    P4=[P4_list[1],P4_list[3],P4_list[2],P4_list[0]]
    print('Fk = P4:',P4)

    
    xor_P4=[]
    for i in range(4):
        xor_P4.append(l[i] ^ P4[i])

    print('Combine new l and previous r: ', xor_P4,r)
    print('l-r and r-l: ', r,xor_P4)


def DES(text, key1, key2):
    IP=(text[1],text[5],text[2],text[0],
        text[3],text[7],text[4],text[6])

    #IP =(2,6,3,1,4,8,5,7)
    #IP_1=(4,1,3,5,7,2,8,6)


    
    
    #print('EP: ',EP)
    #EP=(4,1,2,3,2,3,4,1)

    #p = text ^ EP #key_xor
    xor(key1)
    '''for i in range(8):
        #p.append(text[i] ^ EP[i])
        p.append(key[i] ^ EP[i])'''

    

    xor(key2)


    IP_1=(text[3],text[0],text[2],text[4],
        text[6],text[1],text[7],text[5])
    print('IP_1', IP_1)

    return IP_1



key1 = (1,0,1,0,0,1,0,0)
key2 = (0,1,0,0,0,0,1,1)
#text = input("Enter text:")
text=(1,0,0,1,0,1,1,1)

cipher = DES(text, key1, key2)

 
D_key1=(key1[-1],key1[-2],key1[-3],key1[-4],key1[-5],key1[-6],key1[-7],key1[-8])
D_key2=(key2[-1],key2[-2],key2[-3],key2[-4],key2[-5],key2[-6],key2[-7],key2[-8])
decrypted=DES(text, D_key1, D_key2)

print("\n\nKey1: ", key1)
print("Key2: ", key2)
print("Text: ", text)
print("\nCipher: ", cipher)
print("Decrypted", decrypted)