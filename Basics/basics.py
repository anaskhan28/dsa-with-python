
from typing import List, Set

# def say_goodbye(name: str, hour: int) -> str:
#     return f"Goodbye, {name}. See you again at {hour} o'clock"


# print(say_goodbye("Anas", 12))


# my_list = ["I love", 143]

# my_list[0] = 2

# print(my_list);


# def list_to_set(nums: List[int]) -> Set[int]:
#     my_set = set()

#     for n in nums:
#         my_set.add(n)
#     return my_set

# print(list_to_set([1,2548,18,4,69,78]))

def contains_duplicate(words: List[str]) -> bool:
    my_set = set(words)
    if len(my_set)< len(words):
        return print('TRUE')
   
    return None
    
print(contains_duplicate(["hello", "world", "hello"]))
