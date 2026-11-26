def open_box(num):
    global count
    count = num
    print("The box is now open., count:", count)
    count -= 1
    if count == 0:
        return
    open_box()

# count = 10
open_box(10)