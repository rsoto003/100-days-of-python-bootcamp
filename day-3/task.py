water_level = 50
if water_level > 80:
    print('drain water initiated')
else:
    print('continue filling tub')


print('welcome to the rollercoaster ride')
height = int(input('what is your height in centimeters?\n'))

if height >= 120:
    print('please proceed to rollercoaster, have fun!')
else:
    parental_guardian = input('do you have a parent or guardian to ride the ride with you?')
    if parental_guardian == 'yes':
        print('great! have fun on the ride!')
    else:
        print('my apologies, you cannot ride this ride.')

