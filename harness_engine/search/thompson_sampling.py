import random
from typing import Optional
from .tree_node import TreeNode


class ThompsonSampling:
    def __init__(self, root_code: str, root_heuristic_value: float):
        self.tree = TreeNode(root_code, root_heuristic_value)
        self.best_node: Optional[TreeNode] = None

    def select_node(self) -> TreeNode:
        current_node = self.tree
        
        while current_node.children:
            current_node = max(
                current_node.children,
                key=lambda node: self._sample_beta(node)
            )
        
        return current_node

    def _sample_beta(self, node: TreeNode) -> float:
        alpha = node.successes + 1
        beta = node.visits - node.successes + 1
        return random.betavariate(alpha, beta)

    def expand_node(self, node: TreeNode, new_code: str, heuristic_value: float) -> TreeNode:
        new_node = TreeNode(new_code, heuristic_value, parent=node)
        node.add_child(new_node)
        
        if (self.best_node is None or 
            heuristic_value > self.best_node.heuristic_value):
            self.best_node = new_node
        
        return new_node

    def update_node(self, node: TreeNode, success: bool) -> None:
        current = node
        while current:
            current.update_stats(success)
            current = current.parent
