
# To store all the independent sets of the graph
independentSets = set()

# To store all maximal independent sets in the graph
maximalIndependentSets = set()

# Dictionary to store edges representing enemy relationships
edges = dict()

# List to store vertices representing friends
vertices = []

# Function to print all independent sets
def printAllIndependentSets():
    for independentSet in independentSets:
        print("{", end=" ")
        for friend in independentSet:
            print(friend, end=" ")
        print("}", end='')
    print()

# Function to extract all maximal independent sets
def printMaximalIndependentSets():
    maxCount = 0
    localCount = 0
    for independentSet in independentSets:
        localCount = len(independentSet)
        if localCount > maxCount:
            maxCount = localCount

    for independentSet in independentSets:
        localCount = len(independentSet)
        tempMaximalSet = set()

        if localCount == maxCount:
            maximalIndependentSets.add(frozenset(independentSet))

    for maximalSet in maximalIndependentSets:
        print("{", end=" ")
        for friend in maximalSet:
            print(friend, end=" ")
        print("} ", end="")
    print()

# Function to check if a node is a safe node.
def isSafeForIndependentSet(vertex, tempSolutionSet):
    for friend in tempSolutionSet:
        if (friend, vertex) in edges or (vertex, friend) in edges:
            return False
    return True

# Recursive function to find all independent sets
def findAllIndependentSets(currV, setSize, tempSolutionSet):
    for i in range(currV, setSize + 1):
        if isSafeForIndependentSet(vertices[i - 1], tempSolutionSet):
            tempSolutionSet.add(vertices[i - 1])
            findAllIndependentSets(i + 1, setSize, tempSolutionSet)
            tempSolutionSet.remove(vertices[i - 1])

    independentSets.add(frozenset(tempSolutionSet))

# Driver Program
if __name__ == '__main__':
    # Function to get user input for friends and enemies
    def get_user_input():
        num_friends = int(input())
        friends = [input() for _ in range(num_friends)]

        enemies = {}
        for friend in friends:
            enemy_list = input().split(': ')[1].split(', ')
            enemies[friend] = [enemy.strip() for enemy in enemy_list]

        return friends, enemies

    # Function to generate the enemies list based on user input
    def generate_enemies_list(friends, enemies):
        # Creating the enemies list
        enemies_list = []

        for friend, enemy_list in enemies.items():
            for enemy in enemy_list:
                if (friend, enemy) not in enemies_list and (enemy, friend) not in enemies_list:
                    enemies_list.append((friend, enemy))

        return enemies_list

    # Example usage:
    friends, enemies = get_user_input()
    enemies_list = generate_enemies_list(friends, enemies)

    # Creating the graph based on the enemies list
    vertices = friends

    for edge in enemies_list:
        edges[edge] = True

    tempSolutionSet = set()

    # Finding all independent sets
    findAllIndependentSets(0, len(vertices) - 1, tempSolutionSet)

    # print("Friends who can be invited together: ")
    # printAllIndependentSets()
    print("\nMaximal Set of Friends who can be invited:")
    printMaximalIndependentSets()
