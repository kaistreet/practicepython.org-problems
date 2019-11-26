#Write a function that takes the base and height of a triangle and return its area.
def area_of_triangle():
    base = int(input('Enter base of triangle: '))
    height = int(input('Enter height of triangle: '))
    area = base*height
    print('Area of triangle is '+str(area)+'.')
area_of_triangle()
