def queensAtackII(n, k, r_q, c_q, obstacles):

    # Returns possible positions for the queens next move, given the Queens position(r_q, c_q), the size of the borad
    # (n x n) and an array with positions for obstacles

    #  Determining number of general possible positions:
    if n != c_q and n != r_q and c_q != 1 and r_q != 1:
        n_houses_no_obs = n - r_q + r_q - 1 + n - c_q + c_q - 1 + min((n-c_q), (n-r_q)) + min((r_q-1), (c_q-1)) + min((n-c_q), (r_q-1)) + min((n-r_q), (c_q-1))
    # Special cases:
    #  Right wall
    elif n == c_q and n != r_q and r_q != 1:
        n_houses_no_obs = n - r_q + r_q - 1 + n - c_q + c_q - 1 + min((r_q-1), (c_q-1)) + min((n-r_q), (c_q-1))
    #  Bot wall
    elif n != c_q and r_q == 1 and c_q != 1:
        n_houses_no_obs = n - r_q + r_q - 1 + n - c_q + c_q - 1 + min((n-c_q), (n-r_q)) + min((n-r_q), (c_q-1))
    #  Top Right
    elif n == c_q and n == r_q:
        n_houses_no_obs = n - r_q + r_q - 1 + n - c_q + c_q - 1 + min((r_q-1), (c_q-1))
    #  Left wall
    elif n != r_q and 1 != r_q and c_q == 1:
        n_houses_no_obs = n - r_q + r_q - 1 + n - c_q + c_q - + min((n-c_q), (r_q-1)) + min((n-c_q), (n-r_q))
    #  Top wall
    elif r_q == n and c_q != n and c_q != 1:
        n_houses_no_obs = n - r_q + r_q - 1 + n - c_q + c_q - 1 + min((r_q-1), (c_q-1)) + min((n-c_q), (r_q-1))
    #  Bot Left
    elif c_q == 1 and r_q == 1:
        n_houses_no_obs = n - r_q + r_q - 1 + n - c_q + c_q - 1 + min((n-c_q), (n-r_q))
    #  Top Left
    elif c_q == 1 and r_q == n:
        n_houses_no_obs = n - r_q + r_q - 1 + n - c_q + c_q - 1 + min((n-c_q), (r_q-1))
    #  Bot Right
    elif c_q == n and r_q == 1:
        n_houses_no_obs = n - r_q + r_q - 1 + n - c_q + c_q - 1 + min((c_q-1), (n-r_q))

    # Subtracting the houses with and behind obstacles
    for v in obstacles:
        if v[0] - r_q != 0 and v[1] - c_q == 0:
            if v[0] > r_q:
                n_houses_no_obs -= (n-v[0]+1)
            elif v[0] < r_q:
                n_houses_no_obs -= v[0]
        elif v[0] - r_q == 0 and v[1] - c_q != 0:
            if v[1] > c_q:
                n_houses_no_obs -= (n-v[1]+1)
            elif v[1] < c_q:
                n_houses_no_obs -= v[1]
        elif abs(v[0] - r_q) == abs(v[1] - c_q):
            n_houses_no_obs -= min(v[0], v[1])

    return min((n-c_q), (n-r_q)),  min((r_q-1), (c_q-1)), min((n-c_q), (c_q-1)), min((n-r_q), (r_q-1)), n_houses_no_obs


if __name__ == '__main__':
    size = 8
    n_obs = 0
    l_q = 5
    co_q = 4
    obs = []
    print(queensAtackII(size, n_obs, l_q, co_q, obs))

"""
n = 5
k = 3
r_qc_q = (4, 3)
r_q = 4
c_q = 3
obstacles = [
    [5, 5],
    [4, 2],
    [2, 3]
]

# Create natural obsctacles, e.g the boarders of the chess table
obst_w = [r_q, 0]
obst_e = [r_q, n+1]
obst_n = [n+1, c_q]
obst_s = [0, c_q]

if r_q + c_q <= n+1:
    obst_nw = [r_q+c_q, 0]
    obst_se = [0, c_q+r_q]
else:
    obst_nw = [n+1, c_q-(n+1-r_q)]
    obst_se = [r_q - (n+1-c_q), n+1]

if r_q - c_q >= 0:
    obst_sw = [r_q-c_q, 0]
    obst_ne = [n+1, c_q + (n+1-r_q)]
else:
    obst_sw = [0, c_q-r_q]
    obst_ne = [r_q + (n+1-c_q), n+1]

# Evaluate each obstacle, determining if they cross the paths of the queen and if they are the closest to the queen position for each of the 8 directions
for obstacle in obstacles:
    # W condition
    if obstacle[0] == r_q and obstacle[1] < c_q and obstacle[1] > obst_w[1]:
        obst_w = obstacle
    # E condition
    elif obstacle[0] == r_q and obstacle[1] > c_q and obstacle[1] < obst_e[1]:
        obst_e = obstacle
    # N condition
    elif obstacle[1] == c_q and obstacle[0] > r_q and obstacle[0] < obst_n[0]:
        obst_n = obstacle
    # S condition
    elif obstacle[1] == c_q and obstacle[0] < r_q and obstacle[0] > obst_s[0]:
        obst_s = obstacle
    # NW condition
    elif obstacle[1] < c_q and obstacle[0] > r_q and (abs(c_q - obstacle[1]) == abs(r_q - obstacle[0])) and obstacle[0] < obst_nw[0]:
        obst_nw = obstacle
    # SW condition
    elif obstacle[1] < c_q and obstacle[0] < r_q and (abs(c_q - obstacle[1]) == abs(r_q - obstacle[0])) and obstacle[0] > obst_sw[0]:
        obst_sw = obstacle
    # SE condition
    elif obstacle[1] > c_q and obstacle[0] < r_q and (abs(c_q - obstacle[1]) == abs(r_q - obstacle[0])) and obstacle[0] > obst_se[0]:
        obst_se = obstacle
    # NE condition
    elif obstacle[1] > c_q and obstacle[0] > r_q and (abs(c_q - obstacle[1]) == abs(r_q - obstacle[0])) and obstacle[0] < obst_ne[0]:
        obst_ne = obstacle

# Calculate the distances for each direction:
# spaces = N+NW+W+SW+S+SE+E+NE
spaces = (obst_n[0]-r_q) + (obst_nw[0]-r_q) + (c_q - obst_w[1]) + (r_q - obst_sw[0]) + (r_q - obst_s[0]) + (r_q - obst_se[0]) + (obst_e[1] - c_q) + (obst_ne[0]-r_q) - 8

print(spaces)

"""