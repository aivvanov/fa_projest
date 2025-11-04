from pydantic import BaseModel, Field
from datetime import datetime, timedelta
from typing import Literal

class Transaction(BaseModel):
    amount: int | float
    category: str = 'another'
    date: datetime
    description: str | None = None


class CategoryImage(BaseModel):
    url: str
    name: str


class Category(BaseModel):
    name: str = "unknown"
    description : str | None = None
    tags: set[str] = set()
    image: CategoryImage | None = None


class CategoriesFilterParams(BaseModel):
    model_config = {"extra": "forbid"}

    limit: int = Field(100, gt=0, le = 100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"


mock_transactions = [
    Transaction(
        amount=1200.5,
        category='salary',
        date=datetime.now() - timedelta(days=10),
        description='Месячная зарплата'
    ),
    Transaction(
        amount=-320,
        category='food',
        date=datetime.now() - timedelta(days=7),
        description='Покупка продуктов'
    ),
    Transaction(
        amount=-501.2,
        category='transport',
        date=datetime.now() - timedelta(days=3),
        description='Такси до аэропорта'
    ),
    Transaction(
        amount=250.0,
        category='freelance',
        date=datetime.now() - timedelta(days=20),
        description='Проект по автоматизации'
    ),
]