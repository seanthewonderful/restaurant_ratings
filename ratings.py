"""Restaurant rating lister."""


# put your code here
open_file = open("scores.txt")
rating_dict = {}

for line in open_file:
    line = line.rstrip('\n').split(':')
    rating_dict[line[0]] = int(line[1])
    
# print(rating_dict)
def sort_ratings():
    each = rating_dict.items()
    sorts = sorted(each)
    for ea in sorts:
        print(f"{ea[0]} is rated at {ea[1]}.")
    rate_more = input("Do you want to rate another restaurant? Type y or n:\n")
    if rate_more == "y":
        user_input()
    
def user_input():
    rest = input("What is the name of the restaurant:\n")
    rating = int(input("Rate the restaurant from 1-5:\n"))
    rating_dict[rest] = rating
    sort_ratings()

user_input()
