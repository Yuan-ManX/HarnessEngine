from typing import List, Optional


class TreeNode:
    def __init__(self, code: str, heuristic_value: float, parent: Optional['TreeNode'] = None):
        self.code = code
        self.heuristic_value = heuristic_value
        self.visits: int = 0
        self.successes: int = 0
        self.children: List['TreeNode'] = []
        self.parent = parent

    def add_child(self, child: 'TreeNode') -> None:
        self.children.append(child)

    def update_stats(self, success: bool) -> None:
        self.visits += 1
        if success:
            self.successes += 1
