import HW11.my_chess as my_chess
import chess.engine

# Evaluation function (material count)
def evaluate_board(board):
    piece_values = {my_chess.PAWN: 1, my_chess.KNIGHT: 3, my_chess.BISHOP: 3, my_chess.ROOK: 5, my_chess.QUEEN: 9, my_chess.KING: 100}
    score = 0
    for square in my_chess.SQUARES:
        piece = board.piece_at(square)
        if piece is not None:
            score += piece_values[piece.piece_type] * (1 if piece.color == board.turn else -1)
    return score

# Minimax function with Alpha-Beta pruning
def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)
    
    if maximizing_player:
        max_eval = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cut-off
        return max_eval
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cut-off
        return min_eval

# Find the best move using minimax with Alpha-Beta pruning
def find_best_move(board, depth):
    best_move = None
    max_score = float('-inf')
    for move in board.legal_moves:
        board.push(move)
        score = minimax(board, depth - 1, float('-inf'), float('inf'), False)
        board.pop()
        if score > max_score:
            max_score = score
            best_move = move
    return best_move

# Main function
def main():
    board = my_chess.Board()
    while not board.is_game_over():
        print(board)
        if board.turn == my_chess.WHITE:
            move = input("Enter your move (in algebraic notation): ")
            board.push_san(move)
        else:
            depth = int(input("Enter search depth for engine: "))
            best_move = find_best_move(board, depth)
            board.push(best_move)
    print("Game over. Result: ", board.result())

if __name__ == "__main__":
    main()
