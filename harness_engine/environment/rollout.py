from .base_environment import BaseEnvironment
from .feedback import FeedbackCollector


class RolloutExecutor:
    def __init__(self, env: BaseEnvironment, harness):
        self.env = env
        self.harness = harness

    def run_rollout(self, max_steps: int = 1000) -> FeedbackCollector:
        feedback = FeedbackCollector()
        observation = self.env.reset()
        done = False
        step_count = 0

        while not done and step_count < max_steps:
            action = self.harness.propose_action(observation)
            is_legal = self.harness.is_legal_action(observation, action)
            error_msg = None

            if is_legal:
                try:
                    next_observation, reward, done, info = self.env.step(action)
                except Exception as e:
                    is_legal = False
                    error_msg = str(e)
                    reward = 0.0
                    done = False
                    next_observation = observation
            else:
                reward = 0.0
                done = False
                next_observation = observation

            feedback.add_step(observation, action, reward, done, is_legal, error_msg)
            observation = next_observation
            step_count += 1

        return feedback
