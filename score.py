from test_scores import *

def get_frame(scoring, frame):
    return filter( lambda x: x[0] == frame, scoring  )

def next_two_roles(scoring, frame_no):
    next_frame = get_frame(scoring, frame_no + 1)
    if len(next_frame) < 2:
        return next_frame + get_frame(scoring, frame_no + 2)[:1]
    return next_frame

def is_strike(frame):
    return (len(frame) == 1) and (frame[0][2] == 10)

def is_spare(frame):
    return  (len(frame)>1) and ((frame[0][2] + frame[1][2]) == 10)

def score(scoring, frame_no=1 ):
    frame = get_frame(scoring, frame_no)
    if len(frame) == 0 or frame_no > 10:
        return 0

    if is_strike(frame):
        bonus_rolls = map(lambda x: x[2], next_two_roles(scoring, frame_no))
        bonus = sum(bonus_rolls)
        frame_score = bonus + 10
        return score(scoring, frame_no+1 ) + frame_score

    elif is_spare(frame):
        next_frame = get_frame(scoring, frame_no+1)
        frame_score = 10 + next_frame[0][2]
        return score(scoring, frame_no+1 ) + frame_score

    else:
        frame_score = 0
        if len(frame) < 2:
            frame_score = frame[0][2]
        else:
            roll_1, roll_2 = frame
            frame_score = roll_1[2] + roll_2[2]
        return score(scoring, frame_no+1 ) + frame_score


if __name__ == '__main__':
    assert(score(perfect_game) == 300)
    assert(score(score_a) == 133)
    assert(score(score_b) == 28)
    assert(score(score_c) == 20)
