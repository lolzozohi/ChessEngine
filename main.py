import chess
import chess.engine

board = chess.Board()

def print_board():
    print(board)

def generate_legal_moves():
    return list(board.legal_moves)

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

def find_best_move(board, depth):
  best_move = None
  best_value = -float('inf')
  for move in board.legal_moves:
      board.push(move)
      board_value = minimax(board, depth - 1, -float('inf'), float('inf'), False)
      board.pop()
      if board_value > best_value:
          best_value = board_value
          best_move = move
  return best_move
def play_game():
 # print("input a depth number from 1-10 for AI") 
    #print("Higher = better yet slower. Lower = Faster but poorer moves")
    #depth = input("Enter chosen Depth value (number cant be changed untill program is restarted")
  while not board.is_game_over():
      print("  ")
      print_board()
      print("  ")
      print("A B C D E F G H")
      print(evaluate_board(board))
      if board.turn == chess.WHITE:
          move = input("Enter your move (Ex:e2e4) ")
          if move in [str(m) for m in board.legal_moves]:
              board.push_san(move)
          else:
              print("Invalid move. Try again.")
      else:
          print(" ")
          print("AI is thinking...")
          best_move = find_best_move(board, 3)  # Depth of 3 for simplicity
          board.push(best_move)
          print(f"AI played: {best_move}")

  print("Game over!")
  print(board.result())

if __name__ == "__main__":
  play_game()
