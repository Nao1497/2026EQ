from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


class ReviewAnalysis(BaseModel):
    sentiment: str = Field(description="positive / negative / neutral")
    score: int = Field(ge=1, le=5, description="1〜5の評価スコア")
    summary: str = Field(description="レビューの要約（1文）")
    keywords: list[str] = Field(description="キーワードのリスト")


llm = ChatOpenAI(
    model="your-model",
    base_url="http://localhost:8080/v1",
    api_key="dummy",
)

structured_llm = llm.with_structured_output(ReviewAnalysis)

result = structured_llm.invoke(
    "配送が早くて助かりました。梱包も丁寧でした。"
)

print(type(result))
print(result.score)
print(result.model_dump())