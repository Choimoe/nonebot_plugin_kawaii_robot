from typing import Tuple
from pydantic import BaseModel, Extra

class Config(BaseModel, extra=Extra.ignore):
    leaf_permission:str = "ALL"
    leaf_ignore:Tuple[str, ...] = tuple()
    leaf_reply_type: int = 1
    leaf_poke_rand:int = 20
    leaf_repeater_limit:Tuple[int, int] = (2, 6)
    leaf_interrupt:int = 20
