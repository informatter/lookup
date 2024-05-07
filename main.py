from typing import Any
from lookup import Lookup
import random
import timeit

def action_generator(action_count=400):
    for _ in range(action_count):
        r = random.uniform(0, 1)
        if r > 0.60:
            yield "insert"
        elif r <= 0.15:
            yield "delete"
        else:
            yield "search"

def timer(func):

    def timer_func(*args, **kwargs):

        start_time = timeit.default_timer()
        func(*args, **kwargs)
        end_time = timeit.default_timer()
        run_time = (end_time - start_time) *1000
        print(f"{func.__name__} executed in {run_time} ms")
        return run_time
    return timer_func

@timer
def insert(lookup:Lookup, key:Any, value:Any):
    lookup.insert(key,value)

@timer
def delete(lookup:Lookup, key:Any):
    lookup.delete(key)

@timer
def search(lookup:Lookup, key:Any):
    lookup.delete(key)

def stress_test(size = 500, action_count=1000):
    actions = action_generator(action_count)
    
    lookup  = Lookup(length=size)
    total_inserts = 0
    average_insert_rt = 0
    total_searches = 0
    average_search_rt = 0
    total_deletions = 0
    average_deletion_rt = 0

    for action in actions:
        key = random.randint(0,size*3)
        if action == "insert":
            run_time = insert(lookup,key,"aa")
            total_inserts+=1
            average_insert_rt+=run_time
        elif action == "delete":
            run_time = delete(lookup,key)
            total_deletions+=1
            average_deletion_rt+=run_time
        else:
            run_time = search(lookup,key)
            total_searches+=1
            average_search_rt+=run_time
        
    print(f"{total_searches} searches executed at an average runtime of { round(average_search_rt / total_searches,4 )} ms")
    print(f"{total_inserts} insertion executed at an average runtime of { round(average_insert_rt / total_inserts,4) } ms")
    print(f"{total_deletions} deletions executed at an average runtime of {round(average_deletion_rt / total_deletions,4 )} ms")

if __name__ == "__main__":

    actions = 100000
    table_size = 500
    stress_test(table_size,actions)
    

