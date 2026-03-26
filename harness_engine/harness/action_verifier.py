from .base_harness import BaseHarness
from .harness_mode import HarnessMode


class ActionVerifierHarness(BaseHarness):
    def __init__(self):
        super().__init__(HarnessMode.ACTION_VERIFIER)

    def propose_action(self, board: str) -> str:
        raise NotImplementedError("ActionVerifierHarness requires external action proposal")

    def is_legal_action(self, board: str, action: str) -> bool:
        return True
