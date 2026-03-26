from typing import List, Tuple, Dict, Optional


class FeedbackCollector:
    def __init__(self):
        self._feedback: List[Tuple[str, str, float, bool, bool, Optional[str]]] = []

    def add_step(
        self,
        observation: str,
        action: str,
        reward: float,
        done: bool,
        is_legal: bool,
        error_msg: Optional[str] = None
    ) -> None:
        self._feedback.append((observation, action, reward, done, is_legal, error_msg))

    def get_all_feedback(self) -> List[Tuple[str, str, float, bool, bool, Optional[str]]]:
        return self._feedback.copy()

    def clear(self) -> None:
        self._feedback = []

    def calculate_success_rate(self) -> float:
        if not self._feedback:
            return 0.0
        last_step = self._feedback[-1]
        _, _, _, done, _, _ = last_step
        return 1.0 if done and last_step[2] > 0 else 0.0
