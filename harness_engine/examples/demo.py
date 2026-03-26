from harness_engine.environment.rollout import RolloutExecutor
from harness_engine.examples.tictactoe_env import TicTacToeEnvironment
from harness_engine.examples.tictactoe_harness import TicTacToeHarness


def main():
    env = TicTacToeEnvironment()
    harness = TicTacToeHarness()
    executor = RolloutExecutor(env, harness)

    print(f"Running {env.get_game_name()} demo...")
    feedback = executor.run_rollout(max_steps=20)
    all_steps = feedback.get_all_feedback()

    print("\n=== Rollout Results ===")
    for i, step in enumerate(all_steps):
        observation, action, reward, done, is_legal, error_msg = step
        print(f"\nStep {i + 1}:")
        print("Board:")
        print(observation)
        print(f"Action: {action}")
        print(f"Reward: {reward}")
        print(f"Legal: {is_legal}")
        if error_msg:
            print(f"Error: {error_msg}")

    print(f"\n=== Final Board ===")
    print(all_steps[-1][0] if all_steps else env.reset())


if __name__ == "__main__":
    main()
