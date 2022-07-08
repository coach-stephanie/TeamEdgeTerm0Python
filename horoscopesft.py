import random

#uzs= user's zodiac sign
uzs = input('Please enter your zodiac sign(Cap the first letter): ')

reply = random.randint(1, 5)
if reply == 1:
    ans = 'You will have small lucky and unlucky moments today.'
elif reply == 2:
    ans = 'You will be very lucky today.'
elif reply == 3:
    ans = 'Life-changing events will happen today.'
elif reply == 4:
    ans = 'Cannot see what might happen.'
elif reply == 5:
    ans = 'Expect one thing to go horribly wrong.'



if uzs == 'Aries':
    print(ans)
elif uzs == 'Taurus':
    print(ans)
elif uzs == 'Gemini':
    print(ans)
elif uzs == 'Cancer':
    print(ans)
elif uzs == 'Leo':
    print(ans)
elif uzs == 'Virgo':
    print(ans)
elif uzs == 'Libra':
    print(ans)
elif uzs == 'Scorpio':
    print(ans)
elif uzs == 'Sagittarius':
    print(ans)
elif uzs == 'Capricorn':
    print(ans)
elif uzs == 'Aquarius':
    print(ans)
elif uzs == 'Pisces':
    print(ans)
else:
    print('Invalid Value')
