from datetime import datetime

odds = [
    1, 3, 5, 7, 9, 11, 13 , 15, 17, 19,
    21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
    41, 43, 45, 46, 47, 49, 51, 53, 54, 55, 57, 59
]

this_time = datetime.today().minute

if this_time in odds:
    print('This minute seems a little odd.')
else:
    print('not an odd minute')
