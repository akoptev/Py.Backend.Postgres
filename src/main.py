from typing import List
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ValidationException
from fastapi.responses import JSONResponse

from enum_types.enum_types import QuestionGroupType
from schemas.schemas import AdminUser, QuestionResult, QuestionText, User


app = FastAPI(title="Trading App")


# Improve Logs for "Internal server error"
@app.exception_handler(ValidationException)
async def validation_exception_handler(request: Request, exc: ValidationException):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()}),
    )


@app.get("/user/login", response_model=User)
def user_login():
    return {"status": 200, "data": "added"}


@app.post("/admin/add")
def add_admin_user(user: AdminUser):
    return {"status": 200, "data": "added"}


@app.get("/questions/{vc}", response_model=List[QuestionText])
def get_questions(vc: str):
    question = QuestionText(
        id=1,
        position=1,
        question="What is the capital of France?",
        title="Geography Question",
        version="1.0",
        group=QuestionGroupType.prs,
        group_data=None,
    )
    return [question]


@app.post("/questions/result")
def save_questions_results(question_results: List[QuestionResult]):
    return {"status": 200, "data": "saved"}
