
# Variables

ans1 = 'Your day will be very smooth.'
#1,5
ans2 = 'Nothing special about your day today.'
#2,6
ans3 = 'I forsee a very rough day ahead. Brace yourself.'
#3,7
ans4 = 'You will be very lucky today. But if you push your luck, you will suffer instead.'
#4,8


print('Welcome to Paper Fortune Teller')
color = input('Please choose a color from Red, Orange, Green, and Blue: ')

if color == 'Red' or color == 'red':
    num = int(input('Please enter a number from 1, 2, 5, or 6: '))
    if num == 1 or num == 5:
        num = int(input('Please enter a number from 3, 4, 7, 8: '))
        if num == 3 or num == 7:
            print(ans3)
        elif num == 4 or num == 8:
            print(ans4)
        else:
            print('Invalid Value')
    elif num == 2 or num == 6:
        num = int(input('Please enter a number from 1, 2, 5, or 6: '))
        if num == 1 or num == 5:
            print(ans1)
        elif num == 2 or num == 6:
            print(ans2)
        else:
            print('Invalid Value')
    else:
        print('Invalid Value')
elif color == 'Orange' or color == 'orange':
    num = int(input('Please enter a number from 3, 4, 7, or 8: '))
    if num == 3 or num == 7:
        num = int(input('Please enter a number from 1, 2, 5, or 6: '))
        if num == 1 or num == 5:
            print(ans1)
        elif num == 2 or num == 6:
            print(ans2)
        else:
            print('Invalid Value')
    elif num == 4 or num == 8:
        num = int(input('Please enter a number from 3, 4, 7, 8: '))
        if num == 3 or num == 7:
            print(ans3)
        elif num == 4 or num == 8:
            print(ans4)
        else:
            print('Invalid Value')
    else:
        print('Invalid Value')
elif color == 'Green' or color == 'green':
    num = int(input('Please enter a number from 1, 2, 5, or 6: '))
    if num == 1 or num == 5:
        num = int(input('Please enter a number from 3, 4, 7, 8: '))
        if num == 3 or num == 7:
            print(ans3)
        elif num == 4 or num == 8:
            print(ans4)
        else:
            print('Invalid Value')
    elif num == 2 or num == 6:
        num = int(input('Please enter a number from 1, 2, 5, or 6: '))
        if num == 1 or num == 5:
            print(ans1)
        elif num == 2 or num == 6:
            print(ans2)
        else:
            print('Invalid Value')
    else:
        print('Invalid Value')
elif color == 'Blue' or color == 'blue':
    num = int(input('Please enter a number from 3, 4, 7, or 8: '))
    if num == 3 or num == 7:
        num = int(input('Please enter a number from 1, 2, 5, or 6: '))
        if num == 1 or num == 5:
            print(ans1)
        elif num == 2 or num == 6:
            print(ans2)
        else:
            print('Invalid Value')
    elif num == 4 or num == 8:
        num = int(input('Please enter a number from 3, 4, 7, 8: '))
        if num == 3 or num == 7:
            print(ans3)
        elif num == 4 or num == 8:
            print(ans4)
        else:
            print('Invalid Value')
    else:
        print('Invalid Value')
else:
    print('Invalid Value')