def make_chocolate(small, big, goal):
    five_count = goal//5
    if 5 * five_count > big * 5 + small or 5 * big + small < goal or 5 * five_count + small < goal:
        return -1
    elif 5 * big + small >= goal and big > five_count:
        return goal - 5 * five_count
    return goal - 5 * big
print(make_chocolate(4, 4, 13))