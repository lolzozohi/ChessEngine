import chess
import chess.engine

board = chess.Board()

def print_board():
    print(board)

print_board()
def generate_legal_moves():
    return list(board.legal_moves)

print(generate_legal_moves())
piece_values = {
  chess.PAWN: 1,
  chess.KNIGHT: 3,
  chess.BISHOP: 3,
  chess.ROOK: 5,
  chess.QUEEN: 9,
  chess.KING: 0  
}

def evaluate_board(board):
  score = 0
  for (piece_type, value) in piece_values.items():
      score += len(board.pieces(piece_type, chess.WHITE)) * value
      score -= len(board.pieces(piece_type, chess.BLACK)) * value
  return score

print(evaluate_board(board))
def minimax(board, depth, alpha, beta, maximizing_player):
  if depth == 0 or board.is_game_over():
      return evaluate_board(board)

  if maximizing_player:
      max_eval = -float('inf')
      for move in board.legal_moves:
          board.push(move)
          eval = minimax(board, depth - 1, alpha, beta, False)
          board.pop()
          max_eval = max(max_eval, eval)
          alpha = max(alpha, eval)
          if beta <= alpha:
              break
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
              break
      return min_eval
