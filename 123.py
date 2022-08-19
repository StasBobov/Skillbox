"""
Pyramid
height = width
  *
 * *
* * *
input blocks_number
calc height
print pyramid

function1:
input_total_blocks_number()
parameters? NONE
return? total_blocks


function2
calc_pyramid_height()
parameters? total_blocks
return? TO DO

function3
create_string_to_print()
parameters?
return?



"""


def input_total_blocks_number():
    while True:
        n = input("Enter blocks number: ")
        if not n.isdigit():
            print('Please print numerical value')
            continue
        elif int(n) <= 0:
            print('Incorrect blocks number entered')
            continue
        else:
            n = int(n)
            return n





def calc_pyramid_height(pyr_bloks):
    next_row_blocks = 0
    blocks_left = pyr_bloks
    while True:
        next_row_blocks += 1
        blocks_left -= next_row_blocks
        if blocks_left < next_row_blocks +1: break

    return next_row_blocks


def create_string_to_print(pyr_hght):
    return


total_blocks = input_total_blocks_number()

height = calc_pyramid_height(total_blocks)

# create_string_to_print(calc_pyramid_height(total_blocks))
# pyramid_string = create_string_to_print(height)
#
# print(pyramid_string)
