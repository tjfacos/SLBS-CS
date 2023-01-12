class Trigonometry:
    def square_area(side):
        return side ** 2
    
    def rectangle_area(x,y):
        return x*y
    
    def triangle_area(b, h):
        return 0.5 * b * h

area = Trigonometry.square_area(int(input("Enter Square Side Length: ")))
print(f"Area: {area}")

area = Trigonometry.rectangle_area(
    *list(map(int, input("Enter the side lengths of a rectange, separated by a " "[space] : ").split()))
)
print(f"Area: {area}")

area = Trigonometry.triangle_area(
    *list(map(int, input("Enter the base and height of a triangle, separated by a " "[space] : ").split()))
)
print(f"Area: {area}")
