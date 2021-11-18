"""
by : Luvidi (2021)
f=front b=back u=up d=down r=right l=left
w=white y=yellow b=blue g=green o=orange r=red

---------
| 0 | 1 |
| 3 | 2 |
---------
"""
class rubik :
    def __init__(self,cube) :
        self.color=cube
        self.moveoption=["f","f'","b","b'","u","u'","d","d'","r","r'","l","l'"]
    def f(self,accent=False) :
        if accent :
            self.color['f'][3],self.color['f'][0],self.color['f'][1],self.color['f'][2]=self.color['f'][0],self.color['f'][1],self.color['f'][2],self.color['f'][3]
            self.color['l'][2],self.color['l'][1],self.color['u'][3],self.color['u'][2],self.color['r'][0],self.color['r'][3],self.color['d'][1],self.color['d'][0]=self.color['u'][3],self.color['u'][2],self.color['r'][0],self.color['r'][3],self.color['d'][1],self.color['d'][0],self.color['l'][2],self.color['l'][1]
            return
        self.color['f'][0],self.color['f'][1],self.color['f'][2],self.color['f'][3]=self.color['f'][3],self.color['f'][0],self.color['f'][1],self.color['f'][2]
        self.color['u'][3],self.color['u'][2],self.color['r'][0],self.color['r'][3],self.color['d'][1],self.color['d'][0],self.color['l'][2],self.color['l'][1]=self.color['l'][2],self.color['l'][1],self.color['u'][3],self.color['u'][2],self.color['r'][0],self.color['r'][3],self.color['d'][1],self.color['d'][0]
    
    def b(self,accent=False) :
        if accent :
            self.color['b'][3],self.color['b'][0],self.color['b'][1],self.color['b'][2]=self.color['b'][0],self.color['b'][1],self.color['b'][2],self.color['b'][3]
            self.color['r'][2],self.color['r'][1],self.color['u'][1],self.color['u'][0],self.color['l'][0],self.color['l'][3],self.color['d'][3],self.color['d'][2]=self.color['u'][1],self.color['u'][0],self.color['l'][0],self.color['l'][3],self.color['d'][3],self.color['d'][2],self.color['r'][2],self.color['r'][1]
            return
        self.color['b'][0],self.color['b'][1],self.color['b'][2],self.color['b'][3]=self.color['b'][3],self.color['b'][0],self.color['b'][1],self.color['b'][2]
        self.color['u'][1],self.color['u'][0],self.color['l'][0],self.color['l'][3],self.color['d'][3],self.color['d'][2],self.color['r'][2],self.color['r'][1]=self.color['r'][2],self.color['r'][1],self.color['u'][1],self.color['u'][0],self.color['l'][0],self.color['l'][3],self.color['d'][3],self.color['d'][2]
    
    def u(self,accent=False) :
        if accent :
            self.color['u'][3],self.color['u'][0],self.color['u'][1],self.color['u'][2]=self.color['u'][0],self.color['u'][1],self.color['u'][2],self.color['u'][3]
            self.color['r'][1],self.color['r'][0],self.color['f'][1],self.color['f'][0],self.color['l'][1],self.color['l'][0],self.color['b'][1],self.color['b'][0]=self.color['f'][1],self.color['f'][0],self.color['l'][1],self.color['l'][0],self.color['b'][1],self.color['b'][0],self.color['r'][1],self.color['r'][0]
            return
        self.color['u'][0],self.color['u'][1],self.color['u'][2],self.color['u'][3]=self.color['u'][3],self.color['u'][0],self.color['u'][1],self.color['u'][2]
        self.color['f'][1],self.color['f'][0],self.color['l'][1],self.color['l'][0],self.color['b'][1],self.color['b'][0],self.color['r'][1],self.color['r'][0]=self.color['r'][1],self.color['r'][0],self.color['f'][1],self.color['f'][0],self.color['l'][1],self.color['l'][0],self.color['b'][1],self.color['b'][0]
    
    def d(self,accent=False) :
        if accent :
            self.color['d'][3],self.color['d'][0],self.color['d'][1],self.color['d'][2]=self.color['d'][0],self.color['d'][1],self.color['d'][2],self.color['d'][3]
            self.color['l'][3],self.color['l'][2],self.color['f'][3],self.color['f'][2],self.color['r'][3],self.color['r'][2],self.color['b'][3],self.color['b'][2]=self.color['f'][3],self.color['f'][2],self.color['r'][3],self.color['r'][2],self.color['b'][3],self.color['b'][2],self.color['l'][3],self.color['l'][2]
            return
        self.color['d'][0],self.color['d'][1],self.color['d'][2],self.color['d'][3]=self.color['d'][3],self.color['d'][0],self.color['d'][1],self.color['d'][2]
        self.color['f'][3],self.color['f'][2],self.color['r'][3],self.color['r'][2],self.color['b'][3],self.color['b'][2],self.color['l'][3],self.color['l'][2]=self.color['l'][3],self.color['l'][2],self.color['f'][3],self.color['f'][2],self.color['r'][3],self.color['r'][2],self.color['b'][3],self.color['b'][2]
    
    def r(self,accent=False) :
        if accent :
            self.color['r'][3],self.color['r'][0],self.color['r'][1],self.color['r'][2]=self.color['r'][0],self.color['r'][1],self.color['r'][2],self.color['r'][3]
            self.color['d'][2],self.color['d'][1],self.color['f'][2],self.color['f'][1],self.color['u'][2],self.color['u'][1],self.color['b'][0],self.color['b'][3]=self.color['f'][2],self.color['f'][1],self.color['u'][2],self.color['u'][1],self.color['b'][0],self.color['b'][3],self.color['d'][2],self.color['d'][1]
            return
        
        self.color['r'][0],self.color['r'][1],self.color['r'][2],self.color['r'][3]=self.color['r'][3],self.color['r'][0],self.color['r'][1],self.color['r'][2]
        self.color['f'][2],self.color['f'][1],self.color['u'][2],self.color['u'][1],self.color['b'][0],self.color['b'][3],self.color['d'][2],self.color['d'][1]=self.color['d'][2],self.color['d'][1],self.color['f'][2],self.color['f'][1],self.color['u'][2],self.color['u'][1],self.color['b'][0],self.color['b'][3]
        
    def r(self,accent=False) :
        if accent :
            self.color['r'][3],self.color['r'][0],self.color['r'][1],self.color['r'][2]=self.color['r'][0],self.color['r'][1],self.color['r'][2],self.color['r'][3]
            self.color['d'][2],self.color['d'][1],self.color['f'][2],self.color['f'][1],self.color['u'][2],self.color['u'][1],self.color['b'][0],self.color['b'][3]=self.color['f'][2],self.color['f'][1],self.color['u'][2],self.color['u'][1],self.color['b'][0],self.color['b'][3],self.color['d'][2],self.color['d'][1]
            return
        
        self.color['r'][0],self.color['r'][1],self.color['r'][2],self.color['r'][3]=self.color['r'][3],self.color['r'][0],self.color['r'][1],self.color['r'][2]
        self.color['f'][2],self.color['f'][1],self.color['u'][2],self.color['u'][1],self.color['b'][0],self.color['b'][3],self.color['d'][2],self.color['d'][1]=self.color['d'][2],self.color['d'][1],self.color['f'][2],self.color['f'][1],self.color['u'][2],self.color['u'][1],self.color['b'][0],self.color['b'][3]    
    
    def l(self,accent=False) :
        if accent :
            self.color['r'][3],self.color['r'][0],self.color['r'][1],self.color['r'][2]=self.color['r'][0],self.color['r'][1],self.color['r'][2],self.color['r'][3]
            self.color['d'][2],self.color['d'][1],self.color['f'][2],self.color['f'][1],self.color['u'][2],self.color['u'][1],self.color['b'][0],self.color['b'][3]=self.color['f'][2],self.color['f'][1],self.color['u'][2],self.color['u'][1],self.color['b'][0],self.color['b'][3],self.color['d'][2],self.color['d'][1]
            return
        
        self.color['l'][0],self.color['l'][1],self.color['l'][2],self.color['l'][3]=self.color['l'][3],self.color['l'][0],self.color['l'][1],self.color['l'][2]
        self.color['f'][0],self.color['f'][3],self.color['d'][0],self.color['d'][3],self.color['b'][2],self.color['b'][1],self.color['u'][0],self.color['u'][3]=self.color['u'][0],self.color['u'][3],self.color['f'][0],self.color['f'][3],self.color['d'][0],self.color['d'][3],self.color['b'][2],self.color['b'][1]
        
    def issolved(self) :
        return sum([len(set(self.color[i])) for i in ['f','b','u','d','r','l']])==6
    
    def solve(self) :
        if self.issolved() :
            return
        self.original=str(self.color)
        self.list1={}
        self.list2={}
        self.list={}
        for i in ['f','b','u','d','r','l'] :
            for j in [False,True] :
                exec(f"self.{i}(accent=j)")
                if self.issolved() :
                    return
                self.list1[f"{i}'" if j else f"{i}"]=(str(self.color))
                self.list[f"{i}'" if j else f"{i}"]=(str(self.color))
                self.color=eval(self.original)
                
        for i in self.list1 :
            self.color=eval(self.list1[i])
            if self.issolved() :
                return i
        while True :
            self.list2={}
            for i in self.list1 :
                for j in ['f','b','u','d','r','l'] :
                    for k in [False,True] :
                        self.color=eval(self.list1[i])
                        exec(f"self.{j}(accent=k)")
                        
                        self.move=i+' '+((j+"'") if k else j)
                        if self.move not in self.list.values() :
                            self.list2[self.move]=str(self.color)
                            self.list[self.move]=str(self.color)
                        self.color=eval(self.original)
            
            for i in self.list2 :
                self.color=eval(self.list2[i])
                if self.issolved() :
                    return i
                
            self.list1={}
            for i in self.list2 :
                for j in ['f','b','u','d','r','l'] :
                    for k in [False,True] :
                        self.color=eval(self.list2[i])
                        exec(f"self.{j}(accent=k)")
                        self.move=i+' '+((j+"'") if k else j)
                        if self.move not in self.list.values() :
                            self.list1[self.move]=str(self.color)
                            self.list[self.move]=str(self.color)
                        self.color=eval(self.original)
                        
            for i in self.list1 :
                self.color=eval(self.list1[i])
                if self.issolved() :
                    return i

if __name__=='__main__' :
    r=rubik({'f':['r','r','o','y'],
            'b':['y','o','w','r'],
            'u':['g','r','b','b'],
            'd':['b','w','g','o'],
            'r':['y','g','w','b'],
            'l':['y','w','o','g']})
    print(r.solve())
