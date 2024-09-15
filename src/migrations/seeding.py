from datetime import datetime
import json
import sys
from typing import List
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from enum_types.enum_types import QuestionGroupType
from models.models import QuestionResultModel, QuestionTextModel
from schemas.schemas import GroupDataPrs, SelectionEntry
from config import DB_HOST, DB_PORT, DB_USER, DB_NAME, DB_PASS
from utils.utils import DateTimeEncoder

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()


def seed_db_data():
    try:
        questions_count: int = session.query(QuestionTextModel).count()
        if questions_count != 0:
            return
    except Exception:
        print(f"Database connection error: {DATABASE_URL}. Shutting down...")
        sys.exit(1)

    seed_questions()
    seed_results()


def seed_questions():
    questions: List[QuestionTextModel] = []
    groupDataPrs = GroupDataPrs(
        low=["Point 1", "Point 2"],
        middle=["Point 1", "Point 2"],
        high=["Point 1", "Point 2"],
    )

    groupDataJson = json.dumps(groupDataPrs.model_dump())
    question = QuestionTextModel(
        id=1,
        position=1,
        question="What is the capital of France?",
        title="Geography Question",
        version="1",
        group=QuestionGroupType.prs.name,
        group_data=groupDataJson,
    )

    questions.append(question)
    session.add_all(questions)
    session.commit()


def seed_results():
    results: List[QuestionResultModel] = []

    selectionEntry = SelectionEntry(selection="4", timestamp=datetime.now())
    selectionEntryJson = json.dumps([selectionEntry.model_dump()], cls=DateTimeEncoder)
    result = QuestionResultModel(
        id=1,
        vc_number="12345",
        question_id=1,
        selection="Point 1",
        updated_at=datetime.now(),
        selections_history=selectionEntryJson,
    )

    results.append(result)
    session.add_all(results)
    session.commit()


def delete_records():
    session.query(QuestionTextModel).delete()
    session.commit()
