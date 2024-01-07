def invite_friends(friends, enemies):
    invited = []

    while friends:
        enemy_counts = {friend: sum(1 for enemy in enemies[friend] if enemy not in invited) for friend in friends}
        chosen_friend = min(enemy_counts, key=enemy_counts.get)

        if all(enemy not in invited for enemy in enemies[chosen_friend]):
            invited.append(chosen_friend)
            friends.remove(chosen_friend)

        else:
            friends.remove(chosen_friend)

    return invited

def get_user_input():
    num_friends = int(input())
    friends = [input() for _ in range(num_friends)]

    enemies = {}
    for friend in friends:
        enemy_list = input().split(': ')[1].split(', ')
        enemies[friend] = [enemy.strip() for enemy in enemy_list]
    
    return friends, enemies

friends, enemies = get_user_input()
invited_friends = invite_friends(friends.copy(), enemies.copy())
print("Optimal invitation list:", invited_friends)

