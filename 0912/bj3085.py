def count(board):
    ans = 1
    for i in range(len(board)): # 행 확인
        cnt = 1
        for j in range(len(board) - 1):
            if board[i][j] == board[i][j + 1]:
                cnt += 1
            else:
                cnt = 1
            ans = max(ans, cnt)
    
    for i in range(len(board)): # 열 확인
        cnt = 1
        for j in range(len(board) - 1):
            if board[j][i] == board[j + 1][i]:
                cnt += 1
            else:
                cnt = 1
            ans = max(ans, cnt)
    
    return ans
                
n = int(input())

board = []

for i in range(n):
    string = input().rstrip()
    str = []
    for j in string:
        str.append(j)
    board.append(str)

ans = 0

for i in range(n):
    for j in range(n):
        if j != n - 1:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            cnt = count(board)
            ans = max(ans, cnt)
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
        
        if i != n - 1:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            cnt = count(board)
            ans = max(ans, cnt)
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

print(ans)