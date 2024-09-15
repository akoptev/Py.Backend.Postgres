from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    MetaData,
    Column,
    Integer,
    String,
    TIMESTAMP,
    ForeignKey,
    Boolean,
    JSON,
    Table,
    func,
)

metadata = MetaData()

Base = declarative_base()


admin_user_table = Table(
    "admin_user",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String, nullable=False),
    Column("role", String, nullable=False),
    Column("expire_at", TIMESTAMP, default=func.current_timestamp()),
    Column("active", Boolean, nullable=False),
)


class AdminUserModel(Base):
    __table__ = admin_user_table


question_text_table = Table(
    "question_text",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("position", String, nullable=False),
    Column("question", String, nullable=False),
    Column("title", String, nullable=False),
    Column("version", String, nullable=False),
    Column("updated_at", TIMESTAMP, default=func.current_timestamp(), nullable=False),
    Column("group", String, nullable=False),
    Column("group_data", JSON),
)

question_result_table = Table(
    "question_result",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("vc_number", String, nullable=False),
    Column("question_id", Integer, ForeignKey("question_text.id"), nullable=False),
    Column("selection", String),
    Column("selections_history", JSON),
    Column("updated_at", TIMESTAMP, default=func.current_timestamp(), nullable=False),
)

class QuestionTextModel(Base):
    __table__ = question_text_table

class QuestionResultModel(Base):
    __table__ = question_result_table
