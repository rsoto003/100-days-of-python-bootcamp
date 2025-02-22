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


wants_photo = input("Would you like your photo to be taken? Y or N\t")

if wants_photo == 'Y':
    print("Add +$3 to total.")
else:
    print("Great, have a great rest of your day.")