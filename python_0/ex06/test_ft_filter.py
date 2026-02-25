print(filter.__doc__)

nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def est_pair(x):
    return x % 2 == 0

nombres_pairs = list(filter(est_pair, nombres))
print(nombres_pairs)  # [2, 4, 6, 8, 10]

def est_pair(x):
    return x % 2 == 0

nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultat = filter(est_pair, nombres)

# IMPORTANT : filter() retourne un objet filter, pas une liste !
print(resultat)        # <filter object at 0x...>
print(list(resultat))  # [2, 4, 6, 8, 10]

users = [
    {"name": "Alice", "active": True},
    {"name": "Bob", "active": False},
    {"name": "Charlie", "active": True},
]

active_users = list(filter(lambda u: u["active"], users))

print(active_users)

data = [1, None, 2, None, 3]

clean = list(filter(lambda x: x is not None, data))

print(clean)

class Ticket:
    def __init__(self, id, urgent):
        self.id = id
        self.urgent = urgent

tickets = [
    Ticket("T1", True),
    Ticket("T2", False),
    Ticket("T3", True),
]

urgent_tickets = list(filter(lambda t: t.urgent, tickets))

print([t.id for t in urgent_tickets])

text = "Hello123World"

letters = list(filter(lambda c: c.isalpha(), text))

print("".join(letters))  # HelloWorld

text = "Hello123World"

letters = list(filter(lambda c: c.isdigit(), text))

print("".join(letters))  # 123