# Introduction

The game is built on the concept of cryptographic anonymity using the principles of XOR operations and obfuscation. Specifically, it draws inspiration from the Diffie-Hellman key exchange and the idea of secure multi-party computation (SMPC). These concepts allow multiple participants to collaboratively compute a result (in this case, whether the bill has been paid) without revealing individual inputs (who paid the bill).


# BillMystery 

Three friends sit down at a café, enjoying their time together. The bill arrives, but in a twist of events, they decide to keep it a secret if one of them has paid—or if no one has at all. The challenge? They must figure out if someone settled the bill, but without revealing who it was, keeping everyone in the dark about the details. <br>
The game revolves around a simple but clever process inspired by cryptographic principles.

How it works:<br>
Pairing and Sharing:
Each friend secretly pairs up with the other two and exchanges a random value—either a 1 or a 0.

Private XOR Calculation:<br>
With the values they received from their pairs, each friend performs an XOR operation. This operation allows them to combine the two values while maintaining secrecy.

After the XOR, friends share their results:<br>
If nobody paid the bill, they all tell the truth and reveal the honest XOR result.
But if someone among them did pay, he who did that must have said the opposite of his own result.

Final XOR Check: <br>
Finally, the group combines the shared results using one final XOR operation. If the outcome is 0, nobody paid the bill. If it's 1, someone did—but the identity of the payer remains hidden.














