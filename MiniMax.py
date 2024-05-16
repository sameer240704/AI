# Normal Minimax
import math

def minimax(currentDepth, indexNode, max_min, scores, leafNode, path=[]):
    if currentDepth == leafNode:
        print("Path:", path)
        return scores[indexNode], path    
    if max_min:
        left_score, left_path = minimax(currentDepth + 1,indexNode * 2,False, scores, leafNode, path + [indexNode * 2])
        right_score, right_path = minimax(currentDepth + 1, indexNode * 2 + 1, False, scores, leafNode, path + [indexNode * 2 + 1])
        if left_score > right_score:
            return left_score, left_path
        else:
            return right_score, right_path
    else:
        left_score, left_path = minimax(currentDepth + 1, indexNode * 2,True, scores, leafNode, path + [indexNode * 2])
        right_score, right_path = minimax(currentDepth + 1,indexNode * 2 + 1,True, scores, leafNode, path + [indexNode * 2 + 1])
        if left_score < right_score:
            return left_score, left_path
        else:
            return right_score, right_path

scores = []
                
length = int(input("Enter the Length of the List: "))
for i in range(length):
    num = int(input(f"Enter number {i+1}: "))
    scores.append(num)

lengthNode = int(math.log(len(scores), 2))
max_min = True if (int(math.log(len(scores), 2)) == math.log(len(scores), 2)) else False
print("Minimax Algorithm:")
result, path = minimax(0,0,max_min, scores, lengthNode)
print("Numbers selected on the path:", [scores[node] for node in path])
print("Result:", result)



# Tic Tac Toe using Minimax
import math

# Define constants for representing players and game outcomes
EMPTY = 0
PLAYER_X = 1
PLAYER_O = 2
DRAW = 0
X_WINS = 1
O_WINS = 2

# Define the game board size
BOARD_SIZE = 3

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(str(cell) for cell in row))
        print("-" * (BOARD_SIZE * 4 - 1))

def check_winner(board):
    # Check rows and columns
    for i in range(BOARD_SIZE):
        if all(board[i][j] == PLAYER_X for j in range(BOARD_SIZE)):
            return X_WINS
        elif all(board[i][j] == PLAYER_O for j in range(BOARD_SIZE)):
            return O_WINS
        elif all(board[j][i] == PLAYER_X for j in range(BOARD_SIZE)):
            return X_WINS
        elif all(board[j][i] == PLAYER_O for j in range(BOARD_SIZE)):
            return O_WINS

    # Check diagonals
    if all(board[i][i] == PLAYER_X for i in range(BOARD_SIZE)):
        return X_WINS
    elif all(board[i][BOARD_SIZE - 1 - i] == PLAYER_X for i in range(BOARD_SIZE)):
        return X_WINS
    elif all(board[i][i] == PLAYER_O for i in range(BOARD_SIZE)):
        return O_WINS
    elif all(board[i][BOARD_SIZE - 1 - i] == PLAYER_O for i in range(BOARD_SIZE)):
        return O_WINS

    # Check for draw
    if all(board[i][j] != EMPTY for i in range(BOARD_SIZE) for j in range(BOARD_SIZE)):
        return DRAW

    return None

def minimax(board, depth, maximizing_player):
    winner = check_winner(board)

    if winner is not None:
        if winner == X_WINS:
            return -1
        elif winner == O_WINS:
            return 1
        else:
            return 0

    if maximizing_player:
        max_eval = -math.inf
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    best_eval = -math.inf
    best_move = None
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_O
                eval = minimax(board, 0, False)
                board[i][j] = EMPTY
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

def main():
    board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    game_over = False
    current_player = PLAYER_X

    while not game_over:
        print_board(board)

        if current_player == PLAYER_X:
            row, col = map(int, input("\nEnter row and column (0-2) for X: ").split())
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_X
                current_player = PLAYER_O
        else:
            row, col = find_best_move(board)
            board[row][col] = PLAYER_O
            current_player = PLAYER_X

        winner = check_winner(board)
        if winner is not None:
            print_board(board)
            if winner == DRAW:
                print("\nIt's a draw!")
            elif winner == X_WINS:
                print("X wins!")
            else:
                print("O wins!")
            game_over = True

if __name__ == "__main__":
    main()