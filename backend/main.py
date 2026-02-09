from fastapi import FastAPI
from pydantic import BaseModel
from .llm import text_to_sql  

app = FastAPI(title="Text-to-SQL API")  

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    sql: str

@app.post("/generate-sql", response_model=QueryResponse)
def generate_sql(request: QueryRequest):
    sql = text_to_sql(request.question)
    return {"sql": sql}
