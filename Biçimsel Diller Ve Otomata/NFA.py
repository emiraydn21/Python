#cellular automaton

class NFA:
    def __init__(self,Q,Sigma,delta,S,F):
        self.Q=Q
        self.Sigma=Sigma
        self.delta=delta #transition function
        self.S=S
        self.F=F

    def deltayi_calistir(self, q,x):
        try:
            return self.delta[(q,x)]
        except KeyError:
            return set({})
     
    def calistir(self,w):
        P=self.S

        while w!="":
            Pyeni=set({})
            for q in P:
                Pyeni=Pyeni|self.deltayi_calistir(q,w[0])
            w=w[1:]
            P=Pyeni
        return (P&self.F)!=set({})
    




    

ornek=NFA({0,1,2},{"0","1"},
          {(0,"0"):{0},(0,"1"):{0,1},
           (1,"0"):{2},(1,"1"):{2}},
          {0},
          {2})

print(ornek.calistir("10010111"))


  
