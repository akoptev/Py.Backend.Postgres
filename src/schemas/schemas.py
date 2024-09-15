from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

from enum_types.enum_types import AdminRoleType, QuestionGroupType


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
    id: int
    position: int
    question: str
    title: str
    version: str
    updated_at: Optional[datetime] = datetime.now()
    group: QuestionGroupType
    group_data: Optional[str]


class GroupDataPrs(BaseModel):
    low: Optional[List[str]]
    middle: Optional[List[str]]
    high: Optional[List[str]]


class QuestionResult(BaseModel):
    id: int
    vc_number: str
    question_id: str
    selection: Optional[str]
    updated_at: datetime = datetime.now()
