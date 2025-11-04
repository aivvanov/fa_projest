from fastapi import FastAPI, Query, Path, Body
from typing import Annotated
import uuid
from db import Transaction, Category, CategoriesFilterParams, mock_transactions

app = FastAPI()


@app.get('/transactions')
async def get_transactions(skip: Annotated[int, Query(deprecated = True, title = 'Offset of lost')] = 0, 
                           limit: int = 10
                           ) -> list[Transaction]:
    return mock_transactions[skip : skip + limit]


@app.get('/transactions/{trx_id}')
async def get_transaction(trx_id: Annotated[str, Path(title='The ID of the transaction to get')]):
    return {"trx_id": trx_id}


@app.post('/transactions')
async def add_transaction(transaction: Transaction):
    trx = transaction.model_dump()
    trx.update({"id": uuid.uuid4()})
    return trx


@app.get('/categories')
async def create_category(filter_query: Annotated[CategoriesFilterParams, Query()]):
    return 1


@app.post('/categories')
async def create_category(category: Category, importance: Annotated[int | None, Body(ge=0, le=10)] = None):
    result = category.model_dump()
    if importance:
        result.update({"importance": importance})
    return result