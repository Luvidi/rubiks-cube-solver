"""
by : Luvidi (2021)
f=front b=back u=up d=down r=right l=left
w=white y=yellow b=blue g=green o=orange r=red

---------
| 0 | 1 |
| 3 | 2 |
---------
"""

def replace(string,index,new) :
    return string[:index]+new+string[index+1:]

class Rubik :
    def __init__(self,color) :
        self.color=color
        
    def F(self) :
        temp=self.color[3]
        self.color=replace(self.color,3,self.color[2])
        self.color=replace(self.color,2,self.color[1])
        self.color=replace(self.color,1,self.color[0])
        self.color=replace(self.color,0,temp)

        temp=self.color[11]
        self.color=replace(self.color,11,self.color[22])
        self.color=replace(self.color,22,self.color[13])
        self.color=replace(self.color,13,self.color[16])
        self.color=replace(self.color,16,temp)

        temp=self.color[21]
        self.color=replace(self.color,21,self.color[12])
        self.color=replace(self.color,12,self.color[19])
        self.color=replace(self.color,19,self.color[10])
        self.color=replace(self.color,10,temp)

    def R(self) :
        temp=self.color[19]
        self.color=replace(self.color,19,self.color[18])
        self.color=replace(self.color,18,self.color[17])
        self.color=replace(self.color,17,self.color[16])
        self.color=replace(self.color,16,temp)

        temp=self.color[2]
        self.color=replace(self.color,2,self.color[14])
        self.color=replace(self.color,14,self.color[4])
        self.color=replace(self.color,4,self.color[10])
        self.color=replace(self.color,10,temp)

        temp=self.color[1]
        self.color=replace(self.color,1,self.color[13])
        self.color=replace(self.color,13,self.color[7])
        self.color=replace(self.color,7,self.color[9])
        self.color=replace(self.color,9,temp)

    def U(self) :
        temp=self.color[11]
        self.color=replace(self.color,11,self.color[10])
        self.color=replace(self.color,10,self.color[9])
        self.color=replace(self.color,9,self.color[8])
        self.color=replace(self.color,8,temp)

        temp=self.color[1]
        self.color=replace(self.color,1,self.color[17])
        self.color=replace(self.color,17,self.color[5])
        self.color=replace(self.color,5,self.color[21])
        self.color=replace(self.color,21,temp)

        temp=self.color[0]
        self.color=replace(self.color,0,self.color[16])
        self.color=replace(self.color,16,self.color[4])
        self.color=replace(self.color,4,self.color[20])
        self.color=replace(self.color,20,temp)
    
    def solved(self) :
        for i in range(6) :
            first=self.color[i*4]
            for j in range(4) :
                if self.color[i*4+j]!=first :
                    return False
        return True
    
    def solve(self) : 
        s=self.getMoves()
        s2=""
        col=s[0]
        cnt=0
        for i in range(len(s)) :
            if s[i]==col :
                cnt+=1
            else :
                if cnt==1 :
                    s2+=col+" "
                elif cnt==2 :
                    s2+=col+"2 "
                elif cnt==3 :
                    s2+=col+"' "
                col=s[i]
                cnt=1
        if cnt==1 :
            s2+=col+" "
        elif cnt==2 :
            s2+=col+"2 "
        elif cnt==3 :
            s2+=col+"' "
        return s2
        
        
    def getMoves(self) :
        if self.solved() :
            return ""
        
        original=self.color
        moves1, moves2, list1, list2 = [], [], [], []
        
        for moveIdx in range(3) :
            self.color=original
            move=["F","U","R"][moveIdx]
            exec("self."+move+"()")
            if self.solved() :
                print(self.color)
                return move
            list1.append(self.color)
            moves1.append(move)
        
        while True :
            moves2, list2 = [], []
            for cnt in range(len(moves1)) :
                for moveIdx in range(3) :
                    self.color=list1[cnt]
                    move=["F","U","R"][moveIdx]
                    exec("self."+move+"()")
                    if self.solved() :
                        return moves1[cnt]+move
                    list2.append(self.color)
                    moves2.append(moves1[cnt]+move)
            list1, moves1 = list2.copy(), moves2.copy()
            
        
        
if __name__=='__main__' :
    # f b u d r l
    color="obbygyrgrwowowrwyoyrbbgg" # R F2 R2 F U2 R F2 
    r=Rubik(color) 
    print(r.solve())
