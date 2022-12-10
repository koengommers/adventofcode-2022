shape_scores = {
    'A': 1,
    'B': 2,
    'C': 3,
}
win_score = 6
draw_score = 3

win_conditions = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}


def is_draw(opponent_move, my_move):
    return opponent_move == my_move

def is_win(opponent_move, my_move):
    return win_conditions[my_move] == opponent_move

def calculate_score(opponent_move, my_move):
    score = shape_scores[my_move]
    if is_win(opponent_move, my_move):
        score += win_score
    elif is_draw(opponent_move, my_move):
        score += draw_score
    return score

score = 0

with open('input') as f:
    for line in f:
        opponent_move, strategy = line.strip().split(' ')
        if strategy == 'X':
            my_move = win_conditions[opponent_move]
        elif strategy == 'Y':
            my_move = opponent_move
        elif strategy == 'Z':
            my_move = win_conditions[win_conditions[opponent_move]]
        score += calculate_score(opponent_move, my_move)

print(score)

