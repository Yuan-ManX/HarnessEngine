# HarnessEngine

一个创新的、原创的智能策略搜索与环境交互框架

## 概述

HarnessEngine 是一个开创性的原创框架，旨在通过先进的基于汤普森采样的树搜索解决智能策略优化与环境交互的挑战。无论您正在构建游戏代理、自主决策系统还是代码即策略应用，HarnessEngine 都能为您提供高效探索、评估和优化策略所需的工具。

## 核心功能

- **带汤普森采样的树搜索**: 使用 Beta 分布采样实现智能的探索-利用平衡，引导搜索向有前景的策略候选靠拢
- **多种 Harness 模式**:
  - `ACTION_VERIFIER`: 验证和校验动作
  - `ACTION_FILTER`: 过滤和优先级排序合法动作
  - `CODE_AS_POLICY`: 将自定义代码直接嵌入为策略
- **环境抽象**: 灵活的基础环境接口，可与自定义环境无缝集成
- **模拟执行**: 内置的模拟执行器，用于在目标环境中评估策略
- **优化编排**: 结合搜索、评估和改进的自动化策略优化流程

## 快速入门

### 安装

克隆仓库并安装依赖：

```bash
git clone https://github.com/yourusername/HarnessEngine.git
cd HarnessEngine
pip install -r requirements.txt
```

### 使用示例：井字棋演示

运行内置的井字棋演示，查看 HarnessEngine 的实际效果：

```python
from harness_engine.environment.rollout import RolloutExecutor
from harness_engine.examples.tictactoe_env import TicTacToeEnvironment
from harness_engine.examples.tictactoe_harness import TicTacToeHarness

def main():
    env = TicTacToeEnvironment()
    harness = TicTacToeHarness()
    executor = RolloutExecutor(env, harness)

    print(f"正在运行 {env.get_game_name()} 演示...")
    feedback = executor.run_rollout(max_steps=20)
    all_steps = feedback.get_all_feedback()

    print("\n=== 模拟执行结果 ===")
    for i, step in enumerate(all_steps):
        observation, action, reward, done, is_legal, error_msg = step
        print(f"\n第 {i + 1} 步:")
        print("棋盘:")
        print(observation)
        print(f"动作: {action}")
        print(f"奖励: {reward}")
        print(f"合法性: {is_legal}")
        if error_msg:
            print(f"错误: {error_msg}")

    print(f"\n=== 最终棋盘 ===")
    print(all_steps[-1][0] if all_steps else env.reset())

if __name__ == "__main__":
    main()
```

或者直接运行演示：

```bash
python -m harness_engine.examples.demo
```

## 项目结构

```
HarnessEngine/
├── harness_engine/
│   ├── core/                      # 核心编排与优化
│   │   └── refinement_orchestrator.py
│   ├── environment/               # 环境接口与模拟执行
│   │   ├── base_environment.py
│   │   ├── feedback.py
│   │   └── rollout.py
│   ├── examples/                  # 示例实现
│   │   ├── demo.py
│   │   ├── tictactoe_env.py
│   │   └── tictactoe_harness.py
│   ├── harness/                   # Harness 模式和基类
│   │   ├── action_filter.py
│   │   ├── action_verifier.py
│   │   ├── base_harness.py
│   │   ├── code_as_policy.py
│   │   └── harness_mode.py
│   └── search/                    # 带汤普森采样的树搜索
│       ├── thompson_sampling.py
│       └── tree_node.py
├── LICENSE
├── README.md
├── README_CN.md
└── requirements.txt
```

## 许可证

HarnessEngine 采用 MIT 许可证发布。有关更多详细信息，请参阅 [LICENSE](LICENSE)。

---

HarnessEngine - 一次一个树节点，创新策略搜索！
