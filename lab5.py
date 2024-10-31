from typing import Any

import data


# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.

# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
def time_add(t1 : data.Time, t2 : data.Time) -> data.Time:
    seconds = t1.second + t2.second
    minutes = t1.minute + t2.minute + seconds // 60
    hours = t1.hour + t2.hour + minutes // 60
    updatedSeconds = seconds % 60
    updatedMinutes = minutes % 60
    updatedHours = hours
    return data.Time(updatedHours, updatedMinutes, updatedSeconds)



# Part 4
def is_descending(l1 : list[float]) -> bool:
    for i in range(1, len(l1)):
        if l1[i] >= l1[i-1]:
            return False
    return True


# Part 5
def largest_between(numbers : list[int], lower : int, upper : int) -> int:
    if lower > upper:
        return numbers[lower]
    lower = max(0, lower)
    upper = min(len(numbers), upper)
    maxnum = lower
    for i in range(lower, upper + 1):
        if numbers[i] > numbers[maxnum]:
            maxnum = i
    return maxnum

def largest_between_float(numbers : list[float], lower : int, upper : int) -> int:
    if lower > upper:
        return numbers[lower]
    lower = max(0, lower)
    upper = min(len(numbers), upper)
    maxnum = lower
    for i in range(lower, upper + 1):
        if numbers[i] > numbers[maxnum]:
            maxnum = i
    return maxnum


# Part 6
def furthest_from_origin(finder : list[data.Point]) -> int:
    if len(finder) == 0:
        return None
    dists = []
    for d in finder:
        dists.append(d.origin_distance())
    return largest_between_float(dists, 0, len(dists) - 1)