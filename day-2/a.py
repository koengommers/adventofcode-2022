shape_scores = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}
win_score = 6
draw_score = 3

win_conditions = {
    'X': 'C',
    'Y': 'A',
    'Z': 'B'
}

opponent_moves = ['A', 'B', 'C']
my_moves = ['X', 'Y', 'Z']

def is_draw(opponent_move, my_move):
    return opponent_moves.index(opponent_move) == my_moves.index(my_move)

def is_win(opponent_move, my_move):
    return win_conditions[my_move] == opponent_move

score = 0

with open('input') as f:
    for line in f:
        opponent_move, my_move = line.strip().split(' ')
        score += shape_scores[my_move]
        if is_win(opponent_move, my_move):
            score += win_score
        elif is_draw(opponent_move, my_move):
            score += draw_score

print(score)

