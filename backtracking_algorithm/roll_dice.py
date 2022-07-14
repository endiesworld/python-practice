# Yet to finish this
def roll_dice(dice):
    store = []
    return _roll_dice(dice, store)


def _roll_dice(dice, rolled_dice):
    if dice == 0:
        return ''
    store = []
    dice_number = dice
    for number in range(1, 7):
        data = _roll_dice(dice - 1)
        dice_val = '{},{}'.format(data, number)
        store.append((dice_val))
    return store


print(roll_dice(2))
