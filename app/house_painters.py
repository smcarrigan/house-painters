import os

class Painter(object):
    def __init__(self, job_class):
        self.job_class = job_class
        self.working_job = False
        self.health = 10
        self.terminated = False

STARTING_MONEY = 5000

crew = [Painter('Journeyman')]
game_log = ['Welcome to House Painters!']
bank = { 'money' : STARTING_MONEY }
job_class = {
    'Apprentice' : 100,
    'Journeyman' : 500,
    'Master' : 1000
    }

catalog = {'paintbrush' : 100,
           '1-gallon-paint' : 100,
           '5-gallon-paint' : 400,
           'roller' : 200,
           'sprayer' : 1000,
           'ladder' : 500,
           'scaffolding' : 5000 }

equipment = { 'paintbrush' : 1 }


def show_stats():
    print("Crew: ", [x.job_class for x in crew])
    print("Equipment: ", equipment)
    print("Money: $" + str(bank['money']))
    print("Game Log: ")
    for i in game_log[-5:]:
        print(i)

def hire_painter_menu():
    os.system('clear')
    show_stats()
    print("---------------------")
    print("1) Hire Apprentice: $" + str(job_class['Apprentice']))
    print("2) Hire Journeyman: $" + str(job_class['Journeyman']))
    print("3) Hire Master: $" + str(job_class['Master']))
    print("4) Back to menu")
    hire_painter_input = input("Enter: ")

    if hire_painter_input == '1':
        if bank['money'] < job_class['Apprentice']:
            game_log.append("You do not have enough money.")
        else:
            crew.append(Painter('Apprentice'))
            bank['money'] -= job_class['Apprentice']
            game_log.append("You hired a new apprentice!")
    elif hire_painter_input == '2':
        if bank['money'] < job_class['Journeyman']:
            game_log.append("You do not have enough money.")
        else:
            crew.append(Painter('Journeyman'))
            bank['money'] -= job_class['Journeyman']
            game_log.append("You hired a new journeyman!")
    elif hire_painter_input == '3':
        if bank['money'] < job_class['Master']:
            game_log.append("You do not have enough money.")
        else:
            crew.append(Painter('Master'))
            bank['money'] -= job_class['Master']
            game_log.append("You hired a new master!")

def buy_equipment_menu():
    while(True):
        try:
            os.system('clear')
            show_stats()
            print("---------------------")
            print("1) Paintbrush: $" + str(catalog['paintbrush']))
            print("2) Roller: $" + str(catalog['roller']))
            print("3) Sprayer: $" + str(catalog['sprayer']))
            print("4) Ladder: $" + str(catalog['ladder']))
            print("5) Scaffolding: $" + str(catalog['scaffolding']))
            print("6) 1 gallon paint: $" + str(catalog['1-gallon-paint']))
            print("7) 5 gallon paint: $" + str(catalog['5-gallon-paint']))
            print("8) Back to menu")
            buy_equipment_input = input("Enter: ")
            if buy_equipment_input == '1':
                quantity = int(input("Enter quantity: "))
                total_amount = catalog['paintbrush'] * quantity
                if bank['money'] < total_amount:
                    game_log.append("You do not have enough money.")
                else:
                    equipment['paintbrush'] += quantity
                    bank['money'] -= total_amount
                    if quantity == 1:
                        game_log.append("You bought a paintbrush.")
                    else:
                        game_log.append("You bought " + str(quantity) + " paintbrushes.")
                    break
            elif buy_equipment_input == '8':
                break
            else:
                game_log.append("Invalid input...")
        except ValueError:
            game_log.append("Invalid input...")

def new_job_menu():
    pass

def game_menu():
    while(True):
        os.system('clear')
        show_stats()
        print("---------------------")
        print("1) Hire new painter")
        print("2) Buy equipment")
        print("3) New job")
        print("4) Main menu")
        game_input = input("Enter: ")

        if game_input == '1':
            hire_painter_menu()
        elif game_input == '2':
            buy_equipment_menu()
        elif game_input == '3':
            new_job_menu()
        elif game_input == '4':
            break

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
            game_menu()
        elif menu_input == '2':
            print("Continue Game")
            game_menu()
        elif menu_input == '3':
            print("Good Bye!")
            exit()

if __name__ == '__main__':
    main()
