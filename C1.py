class cube:
    def __init__(self, length, Area, Volume):
        self.length = length
        self.Area = Area
        self.Volume = Volume
    def Calc(self):
        Area = 6*(self.length)**2
        Volume = (self.length)**3
        return f"Side length = {self.length}, Area = {Area}, Volume = {Volume}"
    
while True:
    try:
        cl = cube(int(input()), 0, 0)
        print(cl.Area)
        print(cl.Calc())
        print(cl.Area)
    except:
        break

