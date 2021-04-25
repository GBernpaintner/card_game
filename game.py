def roll(*, state):
    '''Returns the new state after rolling the unkept dice.'''
    values = [randint(1,6) if not keep else x for x, keep in zip(state['values'], state['kept'])]
    counter = state['counter'] + 1
    return {**state, 'values': values, 'counter': counter}


def keep(index, *, state):
    kept = state['kept'].copy()
    kept[index] = not kept[index]
    return {**state, 'kept': kept}


def reset(*, state):
    counter = 0
    kept = [False, False, False, False, False]
    return {**state, 'counter': counter, 'kept': kept }

