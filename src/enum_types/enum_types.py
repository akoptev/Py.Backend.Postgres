from enum import Enum


class AdminRoleType(Enum):
    user = "user"
    master = "master"
    question = "question"
    vc = "vc"


class QuestionGroupType(Enum):
    prs = "prs"
    pls = "pls"
    offers = "offers"
