import numpy as np

ticket = np.random.choice(np.arange(1,51),size=6,replace=False)

winning = np.random.choice(np.arange(1,51),size=6,replace=False)

matches = np.intersect1d(ticket,winning)

print("Ticket numbers: ",ticket)
print("Winning numbers: ",winning)
print("total matches: ",len(matches))