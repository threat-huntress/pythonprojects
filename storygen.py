import random

when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago']
who = ['a rabbit', 'a mouse', 'a turtle', 'a cat']
name = ['Ali', 'Sam', 'Kayla', 'Ella']
residence = ['France', 'Italy', 'Georgia', 'Spain']
went = ['movie', 'university', 'school', 'work']
happened = ['made a friend', 'found a secret hiding place', 'solved a mystery', 'wrote a book']

print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))
