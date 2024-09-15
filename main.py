
import random

player_one_two = round(random.random())
player_one_three = round(random.random())
player_three_two = round(random.random())

x = round(random.random())

player_one = player_one_two ^ player_one_three if x == 0 else int(not(player_one_two ^ player_one_three))
player_two =  round(random.random()) if x == 0 else int(player_one_two ^ player_three_two)
player_three = round(random.random()) if x == 0 else player_one_three ^ player_three_two


result = player_one ^ player_two ^ player_three
result_text = "It gives 1 (True), someone among players must have paid then. \nBy looking at what each of them revealed, can you guess who paid?" if result == 1 else "It gives 0 (False) Someone else must have paid then."

print(f"""

Player one shares {player_one_two} with player two and {player_one_three} with player three.
Player two share {player_one_two} with player one and {player_three_two} with player three.
Player three share {player_one_three} with player one and {player_three_two} with player two.   

Player one says {player_one}.
Player two says {player_two}.
Player three says {player_three}.

(({player_one} xor {player_two}) xor {player_three}) =  gives us {result}.

{result_text}
""")

