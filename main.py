from lookup import Lookup
import random

def action_generator(action_count=400):
    for _ in range(action_count):
        r = random.uniform(0, 1)
        if r > 0.60:
            yield "insert"
        elif r <= 0.15:
            yield "delete"
        else:
            yield "search"

def stress_test(size = 500, action_count=1000):
    actions = action_generator(action_count)
    
    lookup  = Lookup(length=size)

    for action in actions:
        key = random.randint(0,size*3)
        if action == "insert":

            lookup.insert(key,"aa")
        elif action == "delete":
            lookup.delete(key)
        else:
            lookup.search(key)
    
    print(f"total items: {lookup.size}")
    print(f"total slots: {lookup.length}")

if __name__ == "__main__":

    actions = 200000
    table_size = 500
    stress_test(table_size,actions)
    

