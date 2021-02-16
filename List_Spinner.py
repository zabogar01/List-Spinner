def counterClockwise(lst):
    result = []
    for y in range(len(lst[0])-1,-1,-1):
        result.append('|')
        for x in range(len(lst)):    
            result.append(lst[x][y])
    
    return result
        
m =[[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
[13, 14, 15, 16]]

counterClockwise(m)