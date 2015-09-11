import os
import json
import time

# Constants
STARTING_MONEY = 200
APARTMENT_COMPLETION_TIME = 10
SINGLE_STORY_HOUSE_COMPLETION_TIME = 20
TWO_STORY_HOUSE_COMPLETION_TIME = 40
MANSION_COMPLETION_TIME = 60
COMMERCIAL_COMPLETION_TIME = 120

class Player(object):
    def __init__(self):
        self.game_log = ['Welcome to House Painters!']
        self.crew = {
            'apprentice' : 0,
            'journeyman' : 1,
            'master' : 0
        }
        self.bank = { 
            'money' : STARTING_MONEY 
        }
        self.equipment = { 
            'paintbrush' : 1,
            'paint' : 1,
            'roller' : 0,
            'sprayer' : 0,
            'ladder' : 0,
            'scaffolding' : 0
        }

# Game definitions
job_class = {
    'apprentice' : 100,
    'journeyman' : 500,
    'master' : 1000
}

catalog = {
   'paintbrush' : 100,
   'paint' : 100,
   'roller' : 200,
   'sprayer' : 1000,
   'ladder' : 500,
   'scaffolding' : 5000
}

earnings = {
    'apartment' : 500,
    'single-story-house' : 1000,
    'two-story-house' : 2000,
    'mansion' : 10000,
    'commercial' : 20000
}

jobs = {
    'apartment' : 
        {
         'paintbrush' : 1, 
         'paint' : 1,
         'time' : APARTMENT_COMPLETION_TIME,
         'bid' : 500
        },
    'single-story-house' : 
        {
         'paintbrush' : 2,
         'roller' : 2,
         'paint' : 4,
         'time' : SINGLE_STORY_HOUSE_COMPLETION_TIME,
         'bid' : 1000
        },
    'two-story-house' : 
        {
         'paintbrush' : 4,
         'roller' : 4,
         'ladder' : 1,
         'paint' : 8,
         'time' : TWO_STORY_HOUSE_COMPLETION_TIME,
         'bid' : 2000
        },
    'mansion' : 
        {
         'paintbrush' : 8,
         'roller' : 8,
         'sprayer' : 1,
         'ladder' : 4,
         'paint' : 16,
         'time' : MANSION_COMPLETION_TIME,
         'bid' : 5000
        },
    'commercial' : 
        {
         'paintbrush' : 20,
         'roller' : 20,
         'sprayer' : 4,
         'ladder' : 4,
         'scaffolding' : 2,
         'paint' : 32,
         'time' : COMMERCIAL_COMPLETION_TIME,
         'bid' : 10000
        }
}

def show_stats(player):
    #print("Crew: ", [x.job_class for x in player.crew])
    print("Crew: ", player.crew)
    print("Equipment: ", player.equipment)
    print("Money: $" + str(player.bank['money']))
    print("Game Log: ")
    for i in player.game_log[-10:]:
        print(i)

def print_hire_painter_menu():
    print("---------------------")
    print("1) Hire Apprentice: $" + str(job_class['apprentice']))
    print("2) Hire Journeyman: $" + str(job_class['journeyman']))
    print("3) Hire Master: $" + str(job_class['master']))
    print("4) Back to menu")

def hire_painter(player):
    os.system('clear')
    show_stats(player)
    print_hire_painter_menu()
    hire_painter_input = input("Enter: ")

    if hire_painter_input == '1':
        if player.bank['money'] < job_class['apprentice']:
            player.game_log.append("You do not have enough money.")
        else:
            if 'apprentice' in player.crew:
                player.crew['apprentice'] += 1
            else:
                player.crew['apprentice'] = 1
            player.bank['money'] -= job_class['apprentice']
            player.game_log.append("You hired a new apprentice!")
    elif hire_painter_input == '2':
        if player.bank['money'] < job_class['journeyman']:
            player.game_log.append("You do not have enough money.")
        else:
            if 'journeyman' in player.crew:
                player.crew['journeyman'] += 1
            else:
                player.crew['journeyman'] = 1
            player.bank['money'] -= job_class['journeyman']
            player.game_log.append("You hired a new journeyman!")
    elif hire_painter_input == '3':
        if player.bank['money'] < job_class['master']:
            player.game_log.append("You do not have enough money.")
        else:
            if 'master' in player.crew:
                player.crew['master'] += 1
            else:
                player.crew['master'] = 1
            player.bank['money'] -= job_class['master']
            player.game_log.append("You hired a new master!")

def print_equipment_menu():
    print("---------------------")
    print("1) Paintbrush: $" + str(catalog['paintbrush']))
    print("2) Roller: $" + str(catalog['roller']))
    print("3) Sprayer: $" + str(catalog['sprayer']))
    print("4) Ladder: $" + str(catalog['ladder']))
    print("5) Scaffolding: $" + str(catalog['scaffolding']))
    print("6) paint: $" + str(catalog['paint']))
    print("7) Back to menu")

def buy_equipment(player):
    while(True):
        try:
            os.system('clear')
            show_stats(player)
            print_equipment_menu()
            buy_equipment_input = input("Enter: ")
            if buy_equipment_input == '1':
                quantity = int(input("Enter quantity: "))
                total_amount = catalog['paintbrush'] * quantity
                if player.bank['money'] < total_amount:
                    player.game_log.append("You do not have enough money.")
                else:
                    player.equipment['paintbrush'] += quantity
                    player.bank['money'] -= total_amount
                    if quantity == 1:
                        player.game_log.append("You bought a paintbrush.")
                    else:
                        player.game_log.append("You bought " + str(quantity) + " paintbrushes.")
                    break
            elif buy_equipment_input == '7':
                break
            else:
                player.game_log.append("Invalid input...")
        except ValueError:
            player.game_log.append("Invalid input...")

def print_job_menu():
    print("---------------------")
    print("1) Apartment: $" + str(jobs['apartment']['bid']))
    print("2) Single Story House: $" + str(jobs['single-story-house']['bid']))
    print("3) Two Story House: $" + str(jobs['two-story-house']['bid']))
    print("4) Mansion: $" + str(jobs['mansion']['bid']))
    print("5) Commercial: $" + str(jobs['commercial']['bid']))
    print("6) Main menu")

def working_progress(player, job):
    seconds = job['time']
    bid = job['bid']
    player.game_log.append("Started job.")
    for x in range(seconds+1):
        time.sleep(1)
        os.system('clear')
        show_stats(player)
        #print_job_menu()
        if x % (seconds / 10) == 0:
            player.game_log.append("Progress: " + str(int((x/seconds)*100)) + "%")
    player.game_log.append("Finished job and customer is happy!")
    player.game_log.append("You earned $" + str(bid))
    player.bank['money'] += bid

def new_job(player):
    while(True):
        try:
            os.system('clear')
            show_stats(player)
            print_job_menu()
            job_menu_input = input("Enter: ")

            if job_menu_input == '1':
                working_progress(player, jobs['apartment'])
            elif job_menu_input == '2':
                working_progress(player, jobs['single-story-house'])
            elif job_menu_input == '3':
                working_progress(player, jobs['two-story-house'])
            elif job_menu_input == '4':
                working_progress(player, jobs['mansion'])
            elif job_menu_input == '5':
                working_progress(player, jobs['commercial'])
            elif job_menu_input == '6':
                break
            else:
                player.game_log.append("Invalid input...")
        except ValueError:
            player.game_log.append("Invalid input...")

def save_game(player):
    player.game_log.append("Saving game...")
    if not os.path.exists('save'):
        os.makedirs('save')
    with open('save/save-state.json', 'w') as fp:
        json.dump(player.__dict__, fp)

def load_game():
    player = Player()
    with open('save/save-state.json') as json_data:
        json_file = json.load(json_data)
        json_data.close()
        player.__dict__ = json_file
    return player

def game_menu(player):
    while(True):
        os.system('clear')
        show_stats(player)
        print("---------------------")
        print("1) Hire new painter")
        print("2) Buy equipment")
        print("3) New job")
        print("4) Save game")
        print("5) Main menu")
        game_input = input("Enter: ")

        if game_input == '1':
            hire_painter(player)
        elif game_input == '2':
            buy_equipment(player)
        elif game_input == '3':
            new_job(player)
        elif game_input == '4':
            save_game(player)
        elif game_input == '5':
            break

def new_game_defaults():
    player = Player()
    return player

def main():
    while(True):
        os.system('clear')
        print("House Painters Simulation game")
        print("------ Main Menu ------")
        print("1) New Game")
        print("2) Continue Game")
        print("3) Exit")
        menu_input = input("Enter: ")

        if menu_input == '1':
            print("New Game")
            game_menu(new_game_defaults())
        elif menu_input == '2':
            print("Continue Game")
            game_menu(load_game())
        elif menu_input == '3':
            print("Good Bye!")
            exit()

if __name__ == '__main__':
    main()
