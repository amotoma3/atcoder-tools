from typing import List

from atcodertools.common.judgetype import Judge

class ProblemConstantSet:

    def __init__(self,
                 mod: int = None,
                 yes_str: str = None,
                 no_str: str = None,
                 judge_method: Judge = None,
                 output_texts: List[str] = None,
                 constraint_texts: List[str] = None,
                 ):
        self.mod = mod
        self.yes_str = yes_str
        self.no_str = no_str
        self.judge_method = judge_method
        self.output_texts = output_texts
        self.constraint_texts = constraint_texts
