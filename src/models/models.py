from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    String,
    TIMESTAMP,
    ForeignKey,
    Boolean,
    JSON,
)

metadata = MetaData()

Base = declarative_base()


class AdminUserModel(Base):
    __tablename__ = "admin_user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)
    expire_at = Column(TIMESTAMP, default=datetime.now)
    active = Column(Boolean, nullable=False)


class QuestionTextModel(Base):
    __tablename__ = "question_text"
    id = Column(Integer, primary_key=True, autoincrement=True)
    position = Column(String, nullable=False)
    question = Column(String, nullable=False)
    title = Column(String, nullable=False)
    version = Column(String, nullable=False)
    updated_at = Column(TIMESTAMP, default=datetime.now, nullable=False)
    group = Column(String, nullable=False)
    group_data = Column(JSON)


class QuestionResultModel(Base):
    __tablename__ = "question_result"
    id = Column(Integer, primary_key=True, autoincrement=True)
    vc_number = Column(String, nullable=False)
    question_id = Column(Integer, ForeignKey("question_text.id"), nullable=False)
    selection = Column(String)
    updated_at = Column(TIMESTAMP, default=datetime.now, nullable=False)
