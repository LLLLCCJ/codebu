def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0
    for i in range(len(dice1)):
        for j in range(len(dice2)):
            if dice1[i] > dice2[j]:
                dice1_wins += 1
            if dice1[i] < dice2[j]:
                dice2_wins += 1
    if dice1_wins > dice2_wins:
        return dice1
    elif dice1_wins < dice2_wins:
        return dice2
    else:
        return dice1


def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)
    for i in range(len(dices)):
        for j in range(len(dices)):
            if i == j:
                continue
            if count_wins(dices[i], dices[j]) == dices[i]:
                if j == len(dices) - 1:
                    return i
                if i == len(dices) - 1 and j == len(dices) - 2:
                    return i
            else:
                break
    return -1


def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)
    strategy = dict()
    strategy["choose_first"] = True
    strategy["first_dice"] = 0
    if find_the_best_dice(dices) == -1:
        strategy["choose_first"] = False
        for i in range(len(dices)):
            for j in range(len(dices)):
                if i==j:
                    continue
                if count_wins(dices[i],dices[j])==dices[i]:
                    continue
                else:
                    strategy[i]=j
                    break
        return strategy
    else:
        strategy["first_dice"]=find_the_best_dice(dices)
        return strategy


print(compute_strategy([[4, 4, 4, 4, 0, 0], [3, 3, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [5, 5, 5, 1, 1, 1]]))
