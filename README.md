# HarnessEngine

An Innovative, Original Framework for Intelligent Policy Search and Environment Interaction

## Overview

HarnessEngine is a groundbreaking, original framework designed to solve the challenge of intelligent policy refinement and environment interaction through advanced tree search with Thompson sampling. Whether you're building game-playing agents, autonomous decision systems, or code-as-policy applications, HarnessEngine provides the tools you need to explore, evaluate, and refine policies efficiently.

## Key Features

- **Tree Search with Thompson Sampling**: Intelligent exploration-exploitation balance using beta-distribution sampling to guide search toward promising policy candidates
- **Multiple Harness Modes**:
  - `ACTION_VERIFIER`: Verify and validate actions
  - `ACTION_FILTER`: Filter and prioritize legal actions
  - `CODE_AS_POLICY`: Embed custom code directly as policy
- **Environment Abstraction**: Flexible base environment interface for seamless integration with custom environments
- **Rollout Execution**: Built-in rollout executor for evaluating policies in target environments
- **Refinement Orchestration**: Automated policy refinement pipeline combining search, evaluation, and improvement

## Quick Start

### Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/HarnessEngine.git
cd HarnessEngine
pip install -r requirements.txt
```

### Example Usage: Tic Tac Toe Demo

Run the built-in Tic Tac Toe demo to see HarnessEngine in action:

```python
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
```

Or run the demo directly:

```bash
python -m harness_engine.examples.demo
```

## Project Structure

```
HarnessEngine/
├── harness_engine/
│   ├── core/                      # Core orchestration and refinement
│   │   └── refinement_orchestrator.py
│   ├── environment/               # Environment interface and rollouts
│   │   ├── base_environment.py
│   │   ├── feedback.py
│   │   └── rollout.py
│   ├── examples/                  # Example implementations
│   │   ├── demo.py
│   │   ├── tictactoe_env.py
│   │   └── tictactoe_harness.py
│   ├── harness/                   # Harness modes and base classes
│   │   ├── action_filter.py
│   │   ├── action_verifier.py
│   │   ├── base_harness.py
│   │   ├── code_as_policy.py
│   │   └── harness_mode.py
│   └── search/                    # Tree search with Thompson sampling
│       ├── thompson_sampling.py
│       └── tree_node.py
├── LICENSE
├── README.md
├── README_CN.md
└── requirements.txt
```

## License

HarnessEngine is released under the MIT License. See [LICENSE](LICENSE) for more details.

---

HarnessEngine - Innovating Policy Search, One Tree Node at a Time!
