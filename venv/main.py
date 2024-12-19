from fastapi import FastAPI, HTTPException
from schemas.Account import Account
from config.db import con
from models.index import Accounts
import pandas as pd

app = FastAPI()

@app.get('/api/getAllAccounts')
async def index():
    data = con.execute(Accounts.select()).fetchall()
    
    data_list = []
    for row in data:
        data_dict = {
            "AccountId": row[0],
            "Name": row[1],
            "Age": row[2],
            "City": row[3],
            "State": row[4],
            "Pincode": row[5]
        }
        data_list.append(data_dict)
    
    return {
        "Success": True,
        "data": data_list
    }

@app.get('/api/Accounts/{account_id}')
async def get_account(account_id: str):
    data = con.execute(Accounts.select().where(Accounts.c.AccountId == account_id)).fetchall()
    if not data:
        raise HTTPException(status_code=404, detail="Account not found")
    data_list = []
    for row in data:
        data_dict = {
            "AccountId": row[0],
            "Name": row[1],
            "Age": row[2],
            "City": row[3],
            "State": row[4],
            "Pincode": row[5]
        }
        data_list.append(data_dict)
    
    return {
        "Success": True,
        "data": data_list
    }

@app.post('/api/Accounts')
async def store(Account:Account):
    data=con.execute(Accounts.insert().values(
        AccountId=Account.AccountId,
        Name=Account.Name,
        Age=Account.Age,
        City=Account.City,
        State=Account.State,
        Pincode=Account.Pincode,
    ))

    if data.is_insert:
        return {
            "Success":True,
            "msg":"New Account stored successfully"
        }
    else:
        return {
            "Success":False,
            "msg":"New Account not stored successfully"
        }

from fastapi import HTTPException
from sqlalchemy.orm import session

@app.put('/api/Accounts/{account_id}')
async def edit(account_id: str):
    result = con.execute(Accounts.select().where(Accounts.c.AccountId == account_id)).fetchall()
    
    if not result:
        raise HTTPException(status_code=404, detail="Account not found")
    data = []
    for row in result:
        data_dict = {
            "AccountId": row[0],
            "Name": row[1],
            "Age": row[2],
            "City": row[3],
            "State": row[4],
            "Pincode": row[5],
        }
        data.append(data_dict)
    
    return {
        "Success": True,
        "data": data
    }


@app.delete('/api/Accounts/{account_id}')
async def delete(account_id: str):
    result = con.execute(Accounts.select().where(Accounts.c.AccountId == account_id)).fetchone()

    if not result:
        raise HTTPException(status_code=404, detail="Account not found")

    con.execute(Accounts.delete().where(Accounts.c.AccountId == account_id))

    return {
        "Success": True,
        "Message": f"Account with AccountId {account_id} has been deleted."
    }