from typing import List
from collections import defaultdict
from sortedcontainers import SortedList

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_info = {}  
        self.cuisine_sorted_lists = defaultdict(SortedList)  

        for i in range(len(foods)):
            food, cuisine, rating = foods[i], cuisines[i], ratings[i]
            self.food_info[food] = (rating, cuisine)
            self.cuisine_sorted_lists[cuisine].add((-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        old_rating, cuisine = self.food_info[food]
        self.cuisine_sorted_lists[cuisine].remove((-old_rating, food))
        self.food_info[food] = (newRating, cuisine)
        self.cuisine_sorted_lists[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.cuisine_sorted_lists[cuisine][0][1]