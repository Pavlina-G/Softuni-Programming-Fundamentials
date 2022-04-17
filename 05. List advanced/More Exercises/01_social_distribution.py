population = list(map(int, input().split(", ")))
min_wealth = int(input())

if sum(population) < len(population) * min_wealth:
    print("No equal distribution possible")
else:
    for num in range(len(population)):
        poorest = min(population)
        richest = max(population)
        poor_index = population.index(poorest)
        rich_index = population.index(richest)
        population[poor_index] += min_wealth - poorest
        population[rich_index] -= min_wealth - poorest
    print(population)
