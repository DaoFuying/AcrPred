# encoding: utf-8
#八个理化性质分成3类，维度168
from __future__ import division
import numpy as np
import math
pp = [
               [['R','K','E','D','Q','N'],['G','A','S','T','P','H','Y'],['C','L','V','I','M','F','W']],
               [['G','A','S','T','P','D','C'],['N','V','E','Q','I','L'],['M','H','K','F','R','Y','W']],
               [['L','I','F','W','C','M','V','Y'],['P','A','T','G','S'],['H','Q','R','K','N','E','D']],
               [['G','A','S','D','T'],['C','P','N','V','E','Q','I','L'],['K','M','H','F','R','Y','W']],
               [['K','R'],['A','N','C','Q','G','H','I','L','M','F','P','S','T','W','Y','V'],['D','E']],
               [['E','A','L','M','Q','K','R','H'],['V','I','Y','C','W','F','T'],['G','N','P','S','D']],
               [['A','L','F','C','G','I','V','W'],['P','K','Q','E','N','D'],['M','R','S','T','H','Y']],
               [['G','Q','D','N','A','H','R'],['K','T','S','E','C'],['I','L','M','F','P','W','Y','V']]
               
     ]
amino_acid = 'ARDCQEHIGNLKMFPSTWYV'
def aac(seq):
    aac_dict = dict(zip(amino_acid,[0]*20))
    for aa in seq:
        aac_dict[aa] += 1
    aac_list = []
    length = len(seq)
    for aa in amino_acid:
        aac_list.append(aac_dict[aa]/length)
    return aac_list

def feature188d(seq_list):

    num = 0
    ctd_list = []
    for i in range(len(seq_list)):
        sq = seq_list[i]
        n1 = np.zeros((8,3)) # 8x3 下标1理化性质，下标2类别
        n2 = np.zeros((8,3)) # 8x3 下标1理化性质，下标2中0代表12,1代表13，2代表23
        n3 = []
        c = np.zeros((8,3))
        t = np.zeros((8,3))
        d = np.zeros((8,3,5))
        ctd = []
        for j in range(8):
            n3_1 = []
            n3_2 = []
            n3_3 = []
            for k in range(len(sq)):
               
                if sq[k] in pp[j][0]:
                    n1[j][0]+=1
                    n3_1.append(k+1)
                    if (k+1)<len(sq):
                        if sq[k+1] in pp[j][1]:
                            n2[j][0]+=1
                        elif sq[k+1] in pp[j][2]:
                            n2[j][1]+=1    
                    
                elif sq[k] in pp[j][1]:
                    n1[j][1]+=1
                    n3_2.append(k+1)
                    if (k+1)<len(sq):
                        if sq[k+1] in pp[j][0]:
                            n2[j][0]+=1
                        elif sq[k+1] in pp[j][2]:
                            n2[j][2]+=1 
                elif sq[k] in pp[j][2]:
                    n1[j][2]+=1
                    n3_3.append(k+1)
                    if (k+1)<len(sq):
                        if sq[k+1] in pp[j][0]:
                            n2[j][1]+=1
                        elif sq[k+1] in pp[j][1]:
                            n2[j][2]+=1
            n3.append(n3_1)
            n3.append(n3_2)
            n3.append(n3_3)
        c = n1/len(sq)            
        t = n2/(len(sq)-1)
        for i in range(0,8):
            for j in range(0,3):
                if n1[i][j]>0:
                    d[i][j][0] = n3[3*i+j][0]/len(sq)
                if n1[i][j]>=4:   
                    d[i][j][1] = n3[3*i+j][int(0.25*n1[i][j])-1]/len(sq)
                if n1[i][j]>=2:
                    d[i][j][2] = n3[3*i+j][int(0.5*n1[i][j])-1]/len(sq)
                if n1[i][j]>=2:
                    d[i][j][3] = n3[3*i+j][int(0.75*n1[i][j])-1]/len(sq)
                if n1[i][j]>0:
                    d[i][j][4] = n3[3*i+j][int(n1[i][j])-1]/len(sq)
        for i in range(0,8):
            for j in range(0,3):
                ctd.append(c[i][j])
        for i in range(0,8):
            for j in range(0,3):
                ctd.append(t[i][j])
        for i in range(0,8):
            for j in range(0,3):
                for k in range(0,5):
                    ctd.append(d[i][j][k])
        #aac_list = aac(sq)
        #for value in aac_list:
        #    ctd.append(value)
        ctd_list.append(ctd)
        num+=1

    #print num
    return ctd_list
