#########################################################################
# TODOS:
# 1. need to figure out how to kick user from program if initial logic is met:
#    - user is too small to ride the ride by themselves
#    - user does not have parent to accompany them.
#########################################################################


print('welcome to the rollercoaster ride ---')

height = int(input('what is your height in centimeters?\t\n - '))
price = 0
can_ride = False

if height > 120:
    can_ride = True
else:
    has_parent = input("Do you have a parent to ride the ride with you? Y or N\t\n - ")
    if has_parent.lower() == 'y':
        can_ride = True
    else:
        print("sorry, you can't ride the ride....")


if can_ride:
    age = int(input('what is your age?\t\n - '))
    want_photos = input("would you like your photo to be taken? Y or N\t\n - ")

    if age < 12:
        price = 5
    elif age <= 18:
        price = 7
    elif 45 <= age <= 55:
        print('The ride is on us!')
    else:
        price = 12

    if want_photos.lower() == 'y':
        price += 3
else:
    print("sorry, you cannot ride the ride.")


print(f"Your total is ${price:.2f}")




