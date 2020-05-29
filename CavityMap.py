def cavityMap(grid):

    if len(grid) == 1:
        return grid
    else:
        new_grid = [grid[0]]
        for line in range(1, len(grid)-1):
            new_line = grid[line]
            for column in range(1, len(grid)-1):
                if int(grid[line][column]) > int(grid[line-1][column]) and int(grid[line][column]) > int(grid[line+1][column]) and int(grid[line][column]) > int(grid[line][column-1]) and int(grid[line][column]) > int(grid[line][column+1]):
                    new_line = new_line[0:column] + 'X' + new_line[column+1:]
            new_grid.append(new_line)
        new_grid.append(grid[-1])

        return new_grid

if __name__ == '__main__':

    grid0 = ['1112', '1912', '1892', '1234']
    print(cavityMap(grid0))
