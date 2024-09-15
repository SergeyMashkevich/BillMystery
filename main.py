
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
Friend two says {player_two}.
Friend three says {player_three}.

(({player_one} xor {player_two}) xor {player_three}) =  gives us {result}.

{result_text}
""")

 


# import random

# player_one_two = round(random.random())
# player_one_three = round(random.random())
# player_three_two = round(random.random())

# x = round(random.random())

# player_one = player_one_two ^ player_one_three if x == 0 else int(not(player_one_two ^ player_one_three))
# player_two =  round(random.random()) if x == 0 else int(player_one_two ^ player_three_two)
# player_three = round(random.random()) if x == 0 else player_one_two ^ player_three_two


# result = player_one ^ player_two ^ player_three
# result_text = "It gives 1 (True), someone among players must have paid then." if result == 1 else "It gives 0 (False) Someone else must have paid then."

# print(f"""
# Three friends sit down at a café, enjoying their time together.
# The bill arrives, but in a twist of events, they decide to keep it a secret if one of them has paid—or if no one has at all.
# The challenge?
# They must figure out if someone settled the bill, but without revealing who it was, keeping everyone in the dark about the details.

# The game revolves around a simple but clever process inspired by cryptographic principles.
      
# How it works:
# Pairing and Sharing:
# Each player secretly pairs up with the other two and exchanges a random value—either a 1 or a 0.

# Private XOR Calculation:
# With the values they received from their pairs, each player performs an XOR operation. This operation allows them to combine the two values while maintaining secrecy.

# Reveal with a Twist:
# After the XOR, players share their results with a twist:

# If they didn't pay the bill, they tell the truth and reveal the honest XOR result.
# But if they did pay, they must lie and reveal the opposite of the result.
# Final XOR Check:
# Finally, the group combines the shared results using one final XOR operation. If the outcome is 0, nobody paid the bill. If it's 1, someone did—but the identity of the payer remains hidden.



# Player one shares {player_one_two} with player two and {player_one_three} with player three.
# Player two share {player_one_two} with player one and {player_three_two} with player three.
# Player three share {player_one_three} with player one and {player_three_two} with player two.   

# Player one says {player_one}.
# Player two says {player_two}.
# Player three says {player_three}.

# (({player_one} xor {player_two}) xor {player_three}) =  gives us {result}.

# {result_text}
# """)

