class Line(object):
    def __init__(self,coor1,coor2):
        self.coor1=coor1
        self.coor2=coor2
    def distance(self):
        x1,y1=self.coor1
        x2,y2=self.coor2
        return ((x1-x2)**2 + (y1-y2)**2)**0.5

coordinate1=(1,0)
coordinate2=(0,8)

li=Line(coordinate1,coordinate2)

print(li.distance())