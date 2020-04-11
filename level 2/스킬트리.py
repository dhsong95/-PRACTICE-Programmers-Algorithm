def valid_skill_tree(skill, skill_tree):
    location = [skill_tree.find(sk) for sk in skill]

    while location and location[-1] == -1:
        location.pop(-1)

    if location and location[0] == -1:
        return False

    if len(location) <= 1:
        return True

    prev_loc = location[0]
    for loc in location[1:]:
        if prev_loc > loc:
            return False
        prev_loc = loc
    return True


def solution(skill, skill_trees):
    valid = 0
    for skill_tree in skill_trees:
        valid += (1 if valid_skill_tree(skill, skill_tree) else 0)
    return valid


assert solution('CBD', ["BACDE", "CBADF", "AECB", "BDA"]) == 2