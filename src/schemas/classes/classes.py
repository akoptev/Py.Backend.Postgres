from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class SelectionEntry(BaseModel):
    selection: str
    timestamp: datetime = datetime.now()
    
class GroupDataPrs(BaseModel):
    low: Optional[List[str]]
    middle: Optional[List[str]]
    high: Optional[List[str]]
