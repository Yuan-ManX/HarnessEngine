from enum import Enum


class HarnessMode(Enum):
    ACTION_VERIFIER = "action_verifier"
    ACTION_FILTER = "action_filter"
    CODE_AS_POLICY = "code_as_policy"
