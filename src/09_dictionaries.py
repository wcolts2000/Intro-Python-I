"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with
lists!).

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Add a new waypoint to the list
# YOUR CODE HERE
waypoints.append({"lat": 46,
                  "lon": -80,
                  "name": "a fourth place"})

# print(waypoints)

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# YOUR CODE HERE
# waypoints[0]['name'] = 'not a real place'
# waypoints[0]['lon'] = -130

for waypoint in waypoints:
    if(waypoint['name'] == 'a place'):
        waypoint.update({'name': 'not a real place', 'lon': -130})

print(waypoints)


# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE
for waypoint in waypoints:
    print(waypoint.values())

for waypoint in waypoints:
    print('LIST: ', list(waypoint))
    print('KEYS: ', waypoint.keys())
    print('VALUES: ', waypoint.values())
    print('ITEMS: ', waypoint.items())
for key, value in waypoints[0].items():
    print("ITEMS: ", key,  type(value))
