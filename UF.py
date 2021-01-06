class unionfind:
    def __init__(self,n):
        self.n = n
        self.par = [-1] * n
    def root(self,x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.root(self,self.par[x])
            return self.par[x]
    def same(self,x,y):
        return self.root(self,x) == self.root(self,y)
    def merge(self,x,y):
        x = self.root(self,x)
        y = self.root(self,y)
        if(x == y):
            return False
        if(self.par[x] > self.par[y]):
            x,y = y,x
        self.par[x] += self.par[y]
        self.par[y] = x
        return True
    def size(self,x):
        return -self.par[self.root(x)]
