class Sonlu_Otomat:
    def __init__(self,Q,Sigma,delta,q0,F):
        self.Q=Q
        self.Sigma=Sigma
        self.delta=delta #transition function
        self.q0=q0
        self.F=F
    def calistir(self,metin):
        q=self.q0
        while metin!="":
            q=self.delta[(q,metin[0])]
            metin=metin[1:]
        return q in self.F
    

ornek=Sonlu_Otomat({0,1,2},{"a","b"},
                   {(0,"a"):0,(0,"b"):1,
                    (1,"a"):2,(1,"b"):1,
                    (2,"a"):2,(2,"b"):2},
                   0,
                   {0,1})

print(ornek.calistir("abbba"));
