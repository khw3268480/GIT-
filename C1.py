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
        length = int(input())
        cl = cube(length, 0, 0)
        print(cl.Calc())
    except:
        break



