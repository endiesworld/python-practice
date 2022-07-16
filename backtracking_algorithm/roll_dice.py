# Yet to finish this
def roll_dice(dice):
    store = []
    return _roll_dice(dice, store)


def _roll_dice(dice, rolled_dice):
    if dice == 0:
        return print(rolled_dice)
    # store = []
    # dice_number = dice
    for number in range(1, 7):
        rolled_dice.append(number)
        _roll_dice(dice - 1, rolled_dice)
        rolled_dice.pop()


print(roll_dice(2))
