class Box:
    def __init__(self, w: float, l: float, h: float) -> None:
        self.width = w
        self.length = l
        self.height = h
    
    @property
    def volume(self):
        return self.width * self.length * self.height
    
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width > 0 and "int" in str(type(width)):
            self._width = width
        else:
            raise Exception("Width must be a integer > 0")

    #CHANGE TO LENGTH AND HEIGHT
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width > 0 and "int" in str(type(width)):
            self._width = width
        else:
            raise Exception("Width must be a integer > 0")

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width > 0 and "int" in str(type(width)):
            self._width = width
        else:
            raise Exception("Width must be a integer > 0")

    def display_dimensions(self):
        print(f"{self.width} x {self.length} x {self.height}")

for _ in range(3):
    w = float(input("Enter width: "))
    l = float(input("Enter length: "))
    h = float(input("Enter height: "))
    box = Box(w,l,h)
    print(f"Vol: {box.volume}")
    box.display_dimensions()