from typing import List
from fastapi import FastAPI, Request, Response, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ValidationException
from fastapi.responses import JSONResponse

from enum_types.enum_types import AdminRoleType, QuestionGroupType
from migrations.seeding import seed_db_data
from schemas.schemas import AdminUser, QuestionResult, QuestionText, User


app = FastAPI(title="Trading App")
seed_db_data()


# Improve Logs for "Internal server error"
@app.exception_handler(ValidationException)
async def validation_exception_handler(request: Request, exc: ValidationException):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()}),
    )


@app.get("/user/login")
def user_login(response: Response) -> User:
    user = User(
        name="UserName",
        token="fsdfk34545345",
        role=AdminRoleType.user,
        vc_numbers=["12345"],
    )
    response.status_code = status.HTTP_202_ACCEPTED
    return user


@app.post("/admin/add")
def add_admin_user(user: AdminUser, response: Response) -> str:
    response.status_code = status.HTTP_202_ACCEPTED
    return "ok"


@app.get("/questions/{vc}")
def get_questions(vc: str) -> List[QuestionText]:
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
def save_questions_results(question_results: List[QuestionResult]) -> str:
    return "ok"
