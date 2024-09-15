from datetime import datetime
from typing import Any, List, Optional
from pydantic import BaseModel

from enum_types.enum_types import AdminRoleType, QuestionGroupType
from schemas.classes.classes import SelectionEntry


class User(BaseModel):
    name: str
    token: str
    role: AdminRoleType = AdminRoleType.user
    vc_numbers: List[str] = []


class AdminUser(BaseModel):
    name: str
    role: AdminRoleType = AdminRoleType.user
    expire_at: datetime
    active: bool


class QuestionText(BaseModel):
    id: str
    position: int
    question: str
    title: str
    version: str
    updated_at: Optional[datetime] = datetime.now()
    group: QuestionGroupType
    group_data: Optional[str]


class QuestionResult(BaseModel):
    id: str
    vc_number: str
    question_id: str
    selection: Optional[str]
    updated_at: datetime = datetime.now()
    selections_history: List[dict[str, Any]]
