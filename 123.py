# def print_triangle(h,s):
#     triangle_string = ""
#     for row_number in range(h):
#         triangle_string =+(row_number + 1) * (s +" ") + "\n"
def print_triangle(h,s):
    triangle_string = ""
    for row_number in range(h):
        triangle_string +=(row_number + 1) * (s +" ") + "\n"

    print(triangle_string)

hight = int(input("Enter hight:"))
sym = input("Enter symbol:")
print_triangle(hight,sym)
