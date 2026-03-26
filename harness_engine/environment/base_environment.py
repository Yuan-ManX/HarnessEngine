from abc import ABC, abstractmethod
from typing import Tuple, Dict


class BaseEnvironment(ABC):
    @abstractmethod
    def reset(self) -> str:
        pass

    @abstractmethod
    def step(self, action: str) -> Tuple[str, float, bool, Dict]:
        pass

    @abstractmethod
    def get_game_name(self) -> str:
        pass
