
import random

player_one_two = round(random.random())
player_one_three = round(random.random())
player_three_two = round(random.random())

player_one_has_paid = input("Have you paid? (type 1 if yes or 0 if not): ")


player_one = player_one_two ^ player_one_three if player_one_has_paid == "0" else int(not(player_one_two ^ player_one_three))
player_two = round(random.random()) if player_one_has_paid == 0 else player_one_two ^ player_three_two
player_three = round(random.random()) if player_one_has_paid == 0 else player_one_two ^ player_three_two

result = player_one ^ player_two ^ player_three
result_text = "It gives 1 (True), someone among players must have paid then." if result == 1 else "It gives 0 (False) Someone else must have paid then."

print(f"""
You share {player_one_two} with player two and {player_one_three} with player three.
Player two share {player_one_two} with player one and {player_three_two} with player three.
Player three share {player_one_three} with player one and {player_three_two} with player two.  

You say {player_one}.
Player two says {player_two}.
Player three says {player_three}.

(({player_one} xor {player_two}) xor {player_three}) =  gives us {result}.

{result_text}
""")

# Player two share {player_one_two} with player one and {player_three_two} with player three.
# Player three share {player_one_three} with player one and {player_three_two} with player two.   

