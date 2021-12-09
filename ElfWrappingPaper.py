'''
The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions
(length l, width w, and height h) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier:
 find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

For example:

A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?
'''


def calculateArea(present_dimension):
    # present_dimension = '1x1x10'
    converted_present_dimension = present_dimension.split('x')
    # print(converted_present_dimension)

    for item in range(0, len(converted_present_dimension)):
        converted_present_dimension[item] = int(converted_present_dimension[item])
    # print(converted_present_dimension)

    length = converted_present_dimension[0]
    width = converted_present_dimension[1]
    height = converted_present_dimension[2]

    total_square_feet_paper = 0
    # print(length, width, height)
    total_square_feet_paper = (2 * length * width) + (2 * width * height) + (2 * height * length)

    converted_present_dimension.sort()

    total_square_feet_paper = total_square_feet_paper + (
            converted_present_dimension[0] * converted_present_dimension[1])

    print(total_square_feet_paper)
    return total_square_feet_paper

def calculate_ribbon(present_dimension):
    converted_present_dimension = present_dimension.split('x')
    for item in range(0,len(converted_present_dimension)):
        converted_present_dimension[item] = int(converted_present_dimension[item])

    length = converted_present_dimension[0]
    width = converted_present_dimension[1]
    height = converted_present_dimension[2]

    converted_present_dimension.sort()

    total_ribbon_required = (converted_present_dimension[0] + converted_present_dimension[0] + converted_present_dimension[1] + converted_present_dimension[1]) + (length * width * height)
    return total_ribbon_required


with open('elfpackaging_input.txt', 'rt') as textFile:
    result = 0
    ribbon_result = 0
    for line in textFile:
        result = result + calculateArea(line)
        ribbon_result = ribbon_result + calculate_ribbon(line)
    print(result)
    print(ribbon_result)
