#cylinder
class cylinder:
    def __init__(self, radius, height, color):
        self.r = radius
        self.h = height
        self.rangi = color

    def calc_area(self, is_closed=True):
        if is_closed == True:
            area = (2 * 22/7 * self.r ** 2 * self.h) + (2 * 22/7 * self.r * self.h)
            print(f"Area of the closed cylinder is {area}")
        else:
            area = (22/7 * self.r ** 2 * self.h) + (2 * 22/7 * self.r * self.h)
            print(f"Area of the open cylinder is {area}")

    def calc_volume(self):
        volume = 22/7 * self.r ** 2 * self.h
        print(f"Volume of the cylinder is {volume}")

c1 = cylinder(10, 11, "Red")
c2 = cylinder(7.8, 22.6, "Blue")
c1.calc_volume()
c1.calc_area(is_closed=False)