
class amsterdam:
    def __init__(self,M,N,R):
        self.pi = 3.14159265359
        if M>=1 and M<=100 and N>=1 and N<=100 and R>=1 and R<=1000:
            self.numstreet = N
            self.numave = M
            self.radius = R
    def computing_shortest_distance(self,a1,a2,b1,b2):
        shortest_distance = self.computing_angle_bet_ave(a1,a2,b1,b2)+self.computing_street(a2,b2)
        print(shortest_distance)
        return 0
    def computing_angle_bet_ave(self,a1,a2,b1,b2):
        # absolute value
        # shortest -> M counts a lot
        # when Theta >2, the way along to the streets are shorter than along to the arc
        if a2 > b2:
           lowest_street = b2
        else:
            lowest_street = a2
        if b1 > a1:
            abs = b1 - a1
        else:
            abs = a1 - b1
        self.theta = (abs / self.numave) * self.pi
        if self.theta > 2:
            return 2*lowest_street/self.numstreet*self.radius
        else:
            return self.theta * self.radius / self.numstreet*lowest_street
    def computing_street(self,a2,b2):

        if a2 > b2:
            return (a2-b2)*self.radius/self.numstreet
        else:
            return (b2-a2)*self.radius/self.numstreet
M = int(input())
N = int(input())
R = float(input())
a1 = int(input()) #ave1
a2 = int(input()) #street1
b1 = int(input()) #ave2
b2 = int(input()) #street2
ok = amsterdam(M,N,R)
ok.computing_shortest_distance(a1,a2,b1,b2)
