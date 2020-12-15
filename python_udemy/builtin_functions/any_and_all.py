friends = [
    {
        'name': 'Rolf',
        'location': 'Washington, D.C.'
    },
    {
        'name': 'Anna',
        'location': 'San Francisco'
    },
    {
        'name': 'Charlie',
        'location': 'San Francisco'
    },
    {
        'name': 'Jose',
        'location': 'San Francisco'
    }
]

your_location = input('Where are you right now? ')
friends_nearby = [friend for friend in friends if friend['location'] == your_location]

if any(friends_nearby):  # True if there's at least one; or False if empty
    print('You are not alone!')

"""
* 0
* None
* [], (), {}
* False
"""

print(bool(0))  # False

print(all([1, 2, 3, 4, 5]))  # True
print(all([0, 1, 2, 3, 4, 5]))  # False
