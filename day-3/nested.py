height_of_person_in_line = int(input('what is your height in cm?\t'))

if height_of_person_in_line > 120:
    print('great, take a seat')

    age_of_person_on_ride = int(input('how old are you?\t'))
    if age_of_person_on_ride <= 18:
        print('[TEENAGER PRICING]: that will be $7 please')
    else:
        print('[ADULT PRICING]: that will be $12 please')
else:
    print('apologies, you cannot take a seat on the ride.')