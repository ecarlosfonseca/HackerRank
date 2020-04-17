def climbingLeaderboard(scores, alice):

    # Returns several positions on a Dense Ranking score board (scores) depending the score (alice)
    # Assuming sorted scores

    no_reps_l = sorted(list(set(scores)))
    positions = []
    aux = 0
    for score_a in alice:
        if score_a < no_reps_l[0]:
            position = len(no_reps_l) + 1
            positions.append(position)
        elif score_a > no_reps_l[-1]:
            positions.append(1)

        else:
            for score_l_count in range(aux, len(no_reps_l)):
                if score_a < no_reps_l[score_l_count]:
                    position = len(no_reps_l) - (score_l_count-1)
                    positions.append(position)
                    aux = score_l_count
                    break
                elif score_a == no_reps_l[score_l_count]:
                    position = len(no_reps_l) - (score_l_count)
                    positions.append(position)
                    aux = score_l_count
                    break

    return positions


if __name__ == '__main__':
    s = [100, 90, 90, 80, 75, 60]
    a = [50, 65, 77, 90, 102]
    print(climbingLeaderboard(s, a))

"""

Not assuming sorted scores, RunTime error on HackerRank for 3 tests

no_reps_l = sorted(list(set(scores)), reverse=True)
    positions = []
    for score_a in alice:
        if score_a < no_reps_l[len(no_reps_l)-1]:
            position = len(no_reps_l) + 1
            positions.append(position)

        else:
            for score_l_count in range(len(no_reps_l)):
                if score_a >= no_reps_l[score_l_count]:
                    position = score_l_count + 1
                    positions.append(position)
                    break

    return positions
"""
