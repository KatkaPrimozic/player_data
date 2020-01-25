class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg


class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(
            first_name=first_name,
            last_name=last_name,
            height_cm=height_cm,
            weight_kg=weight_kg
        )
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(
            first_name=first_name,
            last_name=last_name,
            height_cm=height_cm,
            weight_kg=weight_kg
        )
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


choose_sport = input("First enter the sport of your best player! You can only choose between football and basketball: ")
if choose_sport.lower() == "football":
    print("Enter data of your best football player!")
    first_name = input("Enter players first name: ")
    last_name = input("Enter players last name: ")
    height_cm = input("Enter players height in centimeters: ")
    weight_kg = input("Enter players weight in kilograms: ")
    goals = input("Enter the number of players goals: ")
    yellow_cards = input("Enter the number of players yellow_cards: ")
    red_cards = input("Enter the number of players red_cards: ")

    new_player = FootballPlayer(
        first_name=first_name,
        last_name=last_name,
        height_cm=float(height_cm),
        weight_kg=float(weight_kg),
        goals=int(goals),
        yellow_cards=int(yellow_cards),
        red_cards=int(red_cards)
    )

if choose_sport.lower() == "basketball":
    print("Enter data of your best basketball player!")
    first_name = input("Enter players first name: ")
    last_name = input("Enter players last name: ")
    height_cm = input("Enter players height in centimeters: ")
    weight_kg = input("Enter players weight in kilograms: ")
    points = input("Enter the number of players points: ")
    rebounds = input("Enter the number of players rebounds: ")
    assists = input("Enter the number of players inputs: ")

    new_player = BasketballPlayer(
        first_name=first_name,
        last_name=last_name,
        height_cm=float(height_cm),
        weight_kg=float(weight_kg),
        points=float(points),
        rebounds=float(rebounds),
        assists=float(assists)
    )

with open("player_data.txt", "w") as added_player:
    added_player.write(str(new_player.__dict__))

print("Your best player was successfully added to the list.")
print("Your players data: {0}".format(new_player.__dict__))


