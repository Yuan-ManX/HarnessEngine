from typing import Optional
from harness_engine.search import ThompsonSampling
from harness_engine.environment import RolloutExecutor
from harness_engine.harness import BaseHarness


class RefinementOrchestrator:
    def __init__(self, search: ThompsonSampling, env, initial_code: str):
        self.search = search
        self.env = env
        self.initial_code = initial_code
    
    def run_refinement(self, max_iterations: int, target_heuristic: float = 1.0):
        for _ in range(max_iterations):
            current_node = self.search.select_node()
            
            if current_node.heuristic_value >= target_heuristic:
                break
            
            new_code = self._refine_code(current_node.code)
            heuristic_value, feedback = self.evaluate_code(new_code)
            
            new_node = self.search.expand_node(current_node, new_code, heuristic_value)
            success = heuristic_value >= current_node.heuristic_value
            self.search.update_node(new_node, success)
    
    def evaluate_code(self, code: str):
        harness = self._create_harness_from_code(code)
        rollout_executor = RolloutExecutor(self.env, harness)
        feedback = rollout_executor.run_rollout()
        heuristic_value = feedback.calculate_success_rate()
        return heuristic_value, feedback
    
    def get_best_harness(self):
        if self.search.best_node:
            return self.search.best_node.code
        return self.initial_code
    
    def _refine_code(self, code: str) -> str:
        return code + "\n# Refinement step"
    
    def _create_harness_from_code(self, code: str) -> BaseHarness:
        from harness_engine.harness import HarnessMode
        
        class TempHarness(BaseHarness):
            def __init__(self):
                super().__init__(HarnessMode.CODE_AS_POLICY)
            
            def propose_action(self, board: str) -> str:
                return "no_op"
            
            def is_legal_action(self, board: str, action: str) -> bool:
                return True
        
        return TempHarness()
