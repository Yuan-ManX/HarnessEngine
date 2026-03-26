from harness_engine.environment.base_environment import BaseEnvironment
from typing import Tuple, Dict


class TicTacToeEnvironment(BaseEnvironment):
    def __init__(self):
        self.board = None
        self.current_player = None

    def reset(self) -> str:
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        return self._board_to_string()

    def _board_to_string(self) -> str:
        return (
            f"{self.board[0]}|{self.board[1]}|{self.board[2]}\n"
            f"-----\n"
            f"{self.board[3]}|{self.board[4]}|{self.board[5]}\n"
            f"-----\n"
            f"{self.board[6]}|{self.board[7]}|{self.board[8]}"
        )

    def _check_winner(self) -> str:
        winning_lines = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for line in winning_lines:
            a, b, c = line
            if self.board[a] == self.board[b] == self.board[c] != ' ':
                return self.board[a]
        return None

    def _is_board_full(self) -> bool:
        return ' ' not in self.board

    def step(self, action: str) -> Tuple[str, float, bool, Dict]:
        try:
            pos = int(action)
        except ValueError:
            raise ValueError("Action must be a string representing an integer 0-8")

        if pos < 0 or pos >= 9:
            raise ValueError("Position must be between 0 and 8")
        if self.board[pos] != ' ':
            raise ValueError("Position is already occupied")

        self.board[pos] = self.current_player
        winner = self._check_winner()
        done = winner is not None or self._is_board_full()

        if winner == 'X':
            reward = 1.0
        elif winner == 'O':
            reward = -1.0
        else:
            reward = 0.0

        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return self._board_to_string(), reward, done, {}

    def get_game_name(self) -> str:
        return "Tic Tac Toe"
