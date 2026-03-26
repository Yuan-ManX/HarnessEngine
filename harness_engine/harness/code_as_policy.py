from .base_harness import BaseHarness
from .harness_mode import HarnessMode


class CodeAsPolicyHarness(BaseHarness):
    def __init__(self):
        super().__init__(HarnessMode.CODE_AS_POLICY)

    def propose_action(self, board: str) -> str:
        return ""

    def is_legal_action(self, board: str, action: str) -> bool:
        return True
