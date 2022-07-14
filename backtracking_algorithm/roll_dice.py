def roll_dice(dice_number):
    if dice_number == 0:
        return ''
    store = []
    for number in range(1, 7):
        data = roll_dice(dice_number - 1)
        dice_val = '{},{}'.format(data, number)
        store.append((dice_val))
    return store


print(roll_dice(2))
