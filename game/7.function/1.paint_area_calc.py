test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

def paint_calc(height, width, cover):
    number_of_cans = round(height * width / cover)

    print(number_of_cans)

paint_calc(height = test_h, width = test_w, cover= coverage)

