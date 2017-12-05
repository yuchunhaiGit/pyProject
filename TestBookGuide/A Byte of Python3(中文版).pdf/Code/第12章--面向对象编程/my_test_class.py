class coordinate:
    def __init__(self,x=0,y=0):
        self.x=int(x)
        self.y=int(y)
    def getx(self):
        return self.x
    def gety(self):
        return self.y
def main():
    xx=coordinate()
    print('坐标x的初始化值是：',xx.getx())
    print('坐标y的初始化值是：',xx.gety())
    xy=coordinate(3,6)
    print('更改后的x坐标是：',xy.getx())
    print('更改后的y坐标是：',xy.gety())
    input()
if __name__=='__main__':
    main()
else:
    print('I was imported!')
