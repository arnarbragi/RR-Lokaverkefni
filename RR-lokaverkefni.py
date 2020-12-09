import re
import math

class FallaRannsoknir:
    def __init__(self, fall):
        self.fall = fall

    def diffra(self):
        formerki = []
        for i in self.fall:
            if i == "+" or i == "-":
                formerki.append(i)
                
        lidir = re.split('[-+]',self.fall)
        if self.fall[0] == '-':
            lidir.remove('')
        else:
            formerki.insert(0,'+')

        diffrad = []
        tel = 0
        for i in lidir:
            lidur = re.split('[x]',i)
            if len(lidur) == 2:
                if lidur[0] != '' and lidur[1] != '':
                    if (int(lidur[1]) - 1) == 1:
                        temp = str(int(lidur[0])*2) + "x"
                    else:
                        temp = str(int(lidur[0])*int(lidur[1])) + "x" + str(int(lidur[1])-1)
                    diffrad.append(temp)
                elif lidur[0] == '' and lidur[1] != '':
                    if (int(lidur[1]) -1) == 1:
                        temp = '2x'
                    else:
                        temp = str(lidur[1]) + 'x' + str(int(lidur[1]) - 1)
                    diffrad.append(temp)
                elif lidur[0] != '' and lidur[1] == '':
                    diffrad.append(lidur[0])
                elif lidur[0] == '' and lidur[1] == '':
                    diffrad.append("1")
            elif len(lidur) == 1:
                formerki.pop(tel)
                         
            tel += 1
        strengur = ""
        tel2 = 0
        for y in diffrad:
            if formerki[tel2] == '+':
                if len(strengur) > 0:
                    strengur += '+' + str(y)
                else:
                    strengur = str(y)
            elif formerki[tel2] == '-':
                strengur += '-' + str(y)
            tel2 += 1
        return strengur

    def utgildi(self):
        main = self.diffra()
        formerki = []
        for i in main:
            if i == "+" or i == "-":
                formerki.append(i)
        lidir = re.split('[-+]',main)
        if main[0] == '-':
            lidir.remove('')
        else:
            formerki.insert(0,'+')

        lidur1 = re.split('[x]',lidir[0])
        lidur2 = re.split('[x]',lidir[1])
        if len(lidir) > 2:
            lidur3 = re.split('[x]',lidir[2])
        else:
            lidur3 = []

        if lidur1[0] != '' and lidur1[1] != '':
            if lidur1[1] == '2':
                if formerki[0] == "+":
                    a = int(lidur1[0])
                else:
                    a = -(int(lidur1[0]))
                if len(lidur2) > 1:
                    if formerki[1] == '+':
                        b = int(lidur2[0])
                    else:
                        b = -(int(lidur2[0]))
                else:
                    b = 0
                    if formerki[1] == '+':
                        c = int(lidur2[0])
                    else:
                        c = -(int(lidur2[0]))
                if len(lidur3) == 1:
                    c = int(lidur3[0])
                else:
                    pass
                d = (b**2) - (4*a*c)

                if d >= 0:
                    sol1 = (-b-math.sqrt(d))/(2*a)
                    sol2 = (-b+math.sqrt(d))/(2*a)
                    return sol1, sol2
                else:
                    print("Get ekki reiknað þetta")
                    return None
            else:
                print("Get ekki reiknað")
        elif lidur1[0] == '' and lidur1[1] != '':
            if lidur1[1] == '2':
                if formerki[0] == "+":
                    a = 1
                else:
                    a = -1
                if len(lidur2) > 1:
                    if formerki[1] == '+':
                        b = int(lidur2[0])
                    else:
                        b = -(int(lidur2[0]))
                else:
                    b = 0
                    if formerki[1] == '+':
                        c = int(lidur2[0])
                    else:
                        c = -(int(lidur2[0]))
                if len(lidur3) == 1:
                    c = int(lidur3[0])
                else:
                    pass
                d = (b**2) - (4*a*c)

                if d >= 0:
                    sol1 = (-b-math.sqrt(d))/(2*a)
                    sol2 = (-b+math.sqrt(d))/(2*a)
                    return sol1, sol2
                else:
                    print("Get ekki reiknað þetta")
                    return None
        else:
            print("Get ekki reiknað þetta")
            return None
                

    def uPunktar(self):
        main = self.fall
        half = self.utgildi()
        formerki = []
        for i in main:
            if i == "+" or i == "-":
                formerki.append(i)
        lidir = re.split('[-+]',main)
        if main[0] == '-':
            lidir.remove('')
        else:
            formerki.insert(0,'+')

        sol1 = []
        sol2 = []
        tel = 0
        for i in lidir:
            lidur = re.split('[x]',i)
            if len(lidur) == 2:
                if lidur[0] != '' and lidur[1] != '':
                    if formerki[tel] == '+':
                        a = int(lidur[0]) * (half[0] ** int(lidur[1]))
                        b = int(lidur[0]) * (half[1] ** int(lidur[1]))
                    else:
                        a = -(int(lidur[0])) * (half[0] ** int(lidur[1]))
                        b = -(int(lidur[0])) * (half[1] ** int(lidur[1]))
                    sol1.append(a)
                    sol2.append(b)
                elif lidur[0] == '' and lidur[1] != '':
                    if formerki[tel] == '+':
                        a = half[0] ** int(lidur[1])
                        b = half[1] ** int(lidur[1])
                    else:
                        a = -(half[0] ** int(lidur[1]))
                        b = -(half[1] ** int(lidur[1]))
                    sol1.append(a)
                    sol2.append(b)
                elif lidur[0] != '' and lidur[1] == '':
                    if formerki[tel] == '+':
                        a = int(lidur[0]) * half[0]
                        b = int(lidur[0]) * half[1]
                    else:
                        a = -(int(lidur[0])) * half[0]
                        b = -(int(lidur[0])) * half[1]
                    sol1.append(a)
                    sol2.append(b)
            else:
                sol1.append(int(lidur[0]))
                sol2.append(int(lidur[0]))
            tel += 1
        ret1 = 0
        ret2 = 0
        for y in range(len(sol1)):
            ret1 += sol1[y]
            ret2 += sol2[y]
        return (half[0], ret1), (half[1], ret2)

    def beygjuskil(self):
        temp = FallaRannsoknir(self.diffra())
        main = temp.diffra()
        formerki = []
        for i in main:
            if i == "+" or i == "-":
                formerki.append(i)
        lidir = re.split('[-+]',main)
        if main[0] == '-':
            lidir.remove('')
        else:
            formerki.insert(0,'+')
            
        if len(lidir) >= 2:
            return temp.utgildi()
        else:
            if 'x' in lidir[0]:
                return 0
            else:
                print("Engin beygjuskil")
        

    def bPunktur(self):
        temp = FallaRannsoknir(self.diffra())
        main = temp.diffra()
        half = self.beygjuskil()
        formerki = []
        for i in main:
            if i == "+" or i == "-":
                formerki.append(i)
        lidir = re.split('[-+]',main)
        if main[0] == '-':
            lidir.remove('')
        else:
            formerki.insert(0,'+')
            
        if len(lidir) >= 2:
            return temp.uPunktar()
        elif len(lidir) == 1:
            lidur = re.split('[x]',main)
            if len(lidur) == 2:
                if lidur[0] != '' and lidur[1] != '':
                    if formerki[0] == '+':
                        ret = int(lidur[0]) * (half ** int(lidur[1]))
                    else:
                        ret = -(int(lidur[0])) * (half ** int(lidur[1]))
                elif lidur[0] == '' and lidur[1] != '':
                    if formerki[0] == '+':
                        ret = half ** int(lidur[1])
                    else:
                        ret = -(half ** int(lidur[1]))
                elif lidur[0] != '' and lidur[1] == '':
                    if formerki[0] == '+':
                        ret = int(lidur[0]) * half
                    else:
                        ret = -(int(lidur[0])) * half
                return (half, ret)
        else:
            print("Get ekki reiknað")

        

test = FallaRannsoknir("x3-3x")
print(test.diffra())
print(test.utgildi())
print(test.uPunktar())
print(test.beygjuskil())
print(test.bPunktur())
