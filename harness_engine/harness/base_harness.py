from abc import ABC, abstractmethod
from .harness_mode import HarnessMode


class BaseHarness(ABC):
    def __init__(self, mode: HarnessMode):
        self._mode = mode

    @abstractmethod
    def propose_action(self, board: str) -> str:
        pass

    @abstractmethod
    def is_legal_action(self, board: str, action: str) -> bool:
        pass

    def get_mode(self) -> HarnessMode:
        return self._mode
