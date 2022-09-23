#!/usr/bin/env python3

def showInstructions():
    # print a main menu and the commands
    print('''
Welcome to Pete's house!
====================
Commands:
  go [direction]
  get [item]

  Collect the key and potion and find your way to the Garden to win!
''')


def showStatus():
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
        print('')
    # print description for room
    if 'desc' in rooms[currentRoom]:
        print(rooms[currentRoom]['desc'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {

    'Hall': {
        'north': 'Front Door',
        'south': 'Kitchen',
        'east': 'Dining Room',
        'west': 'Master Bedroom',
        'item': 'key',
        'desc': 'I better explore this mansion and try to find a way out.\nLooks like I can go north, south, east or west.'
    },
    'Master Bedroom': {
        'east': 'Hall',
        'north': 'Garage',
        'item': 'pillow',
        'desc': '\nOh look, a bed! I am pretty sleepy but I do not want to go to bed on an empty stomach. Maybe there is something in the pantry.\nLooks like I can go north or east.'
    },
    'Garage': {
        'south': 'Master Bedroom',
        'desc': '\nHey! There is a car in the garage. But wait... it is missing a tire and you cannot find a spare.\nLooks like I can only go south.'
    },
    'Front Door': {
        'south': 'Hall'
    },
    'Kitchen': {
        'north': 'Hall',
        'item': 'monster',
    },
    'Living Room': {
        'desc': '\nYou see a monster sleeping on the couch but you also notice a ladder going to the roof. Go back the way you came or be very quiet going up...\nLooks like I can go west or up.',
        'up': 'Roof'
    },
    'Roof': {
        'down': 'Living Room',
        'desc': '\nI see a garden and it is not too far!\nLooks like I can go down or south.',
        'south': 'Garden'
    },
    'Dining Room': {
        'west': 'Hall',
        'east': 'Living Room',
        'south': 'Garden',
        'item': 'potion',
        'north': 'Pantry',
        'desc': '\nLooks like I can go north, south, east or west.'
    },
    'Garden': {
        'north': 'Dining Room',
        'desc': '\nLooks like I can only go north.'
    },
    'Pantry': {
        'south': 'Dining Room',
        'item': 'cookie',
        'desc': '\nLooks like I can only go south.'
    }
}

# start the player in the Hall
currentRoom = 'Hall'

# count player moves
move_count = 0

showInstructions()

# loop forever
while True:

    showStatus()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]

        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    # Increment move count
    move_count += 1

    # Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        print(f'You won in {move_count} moves!')
        break
    # If player enters bedroom with cookie and pillow in inventory
    elif currentRoom == 'Master Bedroom' and 'cookie' in inventory and 'pillow' in inventory:
        print('\nPoison cookies and comfy pillows are making you sleepy.. Endlessy sleepy. GAME OVER!')
        print(f'You lost in {move_count} moves.')
        break
    # If a player tries to go out the front door
    elif currentRoom == 'Front Door':
        print('Not so fast! You opened the front door and are greeted with a horde of monsters... GAME OVER!')
        if move_count == 1:
            print(f'You lost in {move_count} move.')
        else:
            print(f'You lost in {move_count} moves.')
        break

    # If a player enters a room with a monster
    elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        if move_count == 1:
            print(f'You lost in {move_count} move.')
        else:
            print(f'You lost in {move_count} moves.')
        break
