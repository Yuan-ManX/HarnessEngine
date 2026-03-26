from harness_engine.harness.action_verifier import ActionVerifierHarness
import random


class TicTacToeHarness(ActionVerifierHarness):
    def __init__(self):
        super().__init__()

    def _parse_board(self, board: str) -> list:
        lines = board.split('\n')
        positions = []
        for line in lines:
            if line.strip() != '-----':
                positions.extend([c for c in line if c in ['X', 'O', ' ']])
        return positions

    def propose_action(self, board: str) -> str:
        positions = self._parse_board(board)
        legal_positions = [i for i, pos in enumerate(positions) if pos == ' ']
        if legal_positions:
            return str(random.choice(legal_positions))
        return "0"

    def is_legal_action(self, board: str, action: str) -> bool:
        try:
            pos = int(action)
        except ValueError:
            return False

        if pos < 0 or pos >= 9:
            return False

        positions = self._parse_board(board)
        return positions[pos] == ' '
