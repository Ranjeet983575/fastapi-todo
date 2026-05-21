from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.llm_service import LLService
from app.services.rag_service import retrieve_context

router = APIRouter(prefix="/llm", tags=["llm"])
llm_service = LLService()

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str

@router.post("/ask", response_model=AnswerResponse)
def ask_question(request: QuestionRequest):
    try:
        answer = llm_service.ask(request.question)
        return AnswerResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/ask_rag", response_model=AnswerResponse)
def ask_rag(request: QuestionRequest):
    try:
        context = retrieve_context(request.question)
        answer = llm_service.ask_with_context(request.question, context)
        return AnswerResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
