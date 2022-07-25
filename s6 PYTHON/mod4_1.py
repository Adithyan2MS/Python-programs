class rational():
    def __init__(self,numer,denom):
        self.numer=numer
        self.denom=denom3
    def numerator(self):
        return self.numer
    def denominator(self):
        return self.denom
    def sum(self):
        return self.numer*self.denom

r=rational(3,4)
print(r.sum())
print(r.numerator())
    