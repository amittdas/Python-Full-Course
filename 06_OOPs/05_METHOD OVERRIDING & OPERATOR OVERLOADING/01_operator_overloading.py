class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def sum(self, p):
        return point((self.x + p.x) , (self.y + p.y))
    def print_point(self):
        print(f'The sum of the two point is p({self.x}, {self.y})')
    def __add__(self, p):
        return point((self.x + p.x) , (self.y + p.y))

p1 = point(3, 4)
p2 = point(7, 6)

# p = p1.sum(p2) # Returns a new point which is sum of p1 and p2

p = p1 + p2   # Operator overloading by def __add__(self, p):

p.print_point()