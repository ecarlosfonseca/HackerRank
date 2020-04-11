"""
Determine all the positions the queen may atack
There are obstacles
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
directions = [[1, 0], [0, 1], [1, 1], [-1, 0], [0, -1], [-1, -1], [1, -1], [-1, 1]]
positions = []
r_obstacles = []

for v in obstacles:
    dir_o_r = v[0] - r_q
    dir_o_c = v[1] - c_q

    for d in directions:

        div = dir_o_r[0]/d[0] if d[0] else 1

        for w in zip(dir_o_r[1:], d[1:]):
            if v[0] != div * v[1]:
                pass
        else:
            r_obstacles.append([dir_o_r, dir_o_c])
        #if d[0] != 0 and d[1] != 0:
        #if isinstance(dir_o_r/d[0], int) and isinstance(dir_o_c/d[1], int):
        # r_obstacles.append([dir_o_r, dir_o_c])
        #elif d[0] == 0 and d[1] != 0:
        # if isinstance(dir_o_c/d[1], int):
        #  r_obstacles.append([dir_o_r, dir_o_c])
        #elif d[0] != 0 and d[1] == 0:
        # if isinstance(dir_o_r/d[0], int):
#   r_obstacles.append([dir_o_r, dir_o_c])

for i in range(1, n):
    for j in range(len(directions)):
        if r_q + i*directions[j][0] > 0 and r_q + i*directions[j][0] <= n and c_q + i*directions[j][1] > 0 and c_q + i*directions[j][1] <= n:
            positions.append([r_q + i*directions[j][0], c_q + i*directions[j][1]])

for valores in r_obstacles:
    for l in positions:
        if isinstance(valores[0]/l[0], int) and isinstance(valores[1]/l[1], int):
            positions.remove(l)
print(r_obstacles)
#print(len(positions))

"""