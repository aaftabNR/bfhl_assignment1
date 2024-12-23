from fastapi import FastAPI, HTTPException
from schemas.Account import Account
from config.db import con
from models.index import Accounts
from schemas.Claims import Claim
from models.index import Claims
from schemas.Policies import Policy
from models.index import Policies
from loguru import logger

logger.add("app.log", rotation="1 MB")
logger.info("Logger setup successful.")

app = FastAPI()

@app.get('/api/getAllAccounts')
async def index():
    try:
        logger.info("Fetching all accounts.")
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

        logger.info("Fetched all accounts successfully.")
        return {
            "Success": True,
            "data": data_list
        }
    except Exception as e:
        logger.error(f"Error fetching accounts: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get('/api/Accounts/{account_id}')
async def get_account(account_id: str):
    try:
        logger.info(f"Fetching account with AccountId: {account_id}")
        data = con.execute(Accounts.select().where(Accounts.c.AccountId == account_id)).fetchall()
        
        if not data:
            logger.warning(f"Account with AccountId {account_id} not found.")
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

        logger.info(f"Fetched account data: {data_list}")
        return {
            "Success": True,
            "data": data_list
        }
    except Exception as e:
        logger.error(f"Error fetching account: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.post('/api/Accounts')
async def store(account: Account):
    try:
        logger.info("Storing a new account.")
        data = con.execute(Accounts.insert().values(
            AccountId=account.AccountId,
            Name=account.Name,
            Age=account.Age,
            City=account.City,
            State=account.State,
            Pincode=account.Pincode,
        ))

        if data.is_insert:
            logger.info("New account stored successfully.")
            return {
                "Success": True,
                "msg": "New Account stored successfully"
            }
        else:
            logger.warning("Failed to store the new account.")
            return {
                "Success": False,
                "msg": "New Account not stored successfully"
            }
    except Exception as e:
        logger.error(f"Error storing account: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.put('/api/Accounts/{account_id}')
async def edit(account_id: str):
    try:
        logger.info(f"Editing account with AccountId: {account_id}")
        result = con.execute(Accounts.select().where(Accounts.c.AccountId == account_id)).fetchall()

        if not result:
            logger.warning(f"Account with AccountId {account_id} not found.")
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

        logger.info(f"Fetched account data for editing: {data}")
        return {
            "Success": True,
            "data": data
        }
    except Exception as e:
        logger.error(f"Error editing account: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.delete('/api/Accounts/{account_id}')
async def delete(account_id: str):
    try:
        logger.info(f"Deleting account with AccountId: {account_id}")
        result = con.execute(Accounts.select().where(Accounts.c.AccountId == account_id)).fetchone()

        if not result:
            logger.warning(f"Account with AccountId {account_id} not found.")
            raise HTTPException(status_code=404, detail="Account not found")

        con.execute(Accounts.delete().where(Accounts.c.AccountId == account_id))
        logger.info(f"Account with AccountId {account_id} deleted successfully.")

        return {
            "Success": True,
            "Message": f"Account with AccountId {account_id} has been deleted."
        }
    except Exception as e:
        logger.error(f"Error deleting account: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get('/api/getAllClaims')
async def get_all_claims():
    try:
        logger.info("Fetching all claims.")
        data = con.execute(Claims.select()).fetchall()

        data_list = []
        for row in data:
            data_dict = {
                "Id": row[0],
                "CreatedDate": row[1],
                "CaseNumber": row[2],
                "HAN": row[3],
                "BillAmount": float(row[4]),
                "Status": row[5],
                "AccountId": row[6],
            }
            data_list.append(data_dict)

        logger.info("Fetched all claims successfully.")
        return {
            "Success": True,
            "data": data_list
        }
    except Exception as e:
        logger.error(f"Error fetching claims: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get('/api/Claims/{claim_id}')
async def get_claim(claim_id: str):
    try:
        logger.info(f"Fetching claim with Id: {claim_id}")
        data = con.execute(Claims.select().where(Claims.c.Id == claim_id)).fetchall()

        if not data:
            logger.warning(f"Claim with Id {claim_id} not found.")
            raise HTTPException(status_code=404, detail="Claim not found")

        data_list = []
        for row in data:
            data_dict = {
                "Id": row[0],
                "CreatedDate": row[1],
                "CaseNumber": row[2],
                "HAN": row[3],
                "BillAmount": row[4],
                "Status": row[5],
                "AccountId": row[6]
            }
            data_list.append(data_dict)

        logger.info(f"Fetched claim data: {data_list}")
        return {
            "Success": True,
            "data": data_list
        }
    except Exception as e:
        logger.error(f"Error fetching claim: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.post('/api/postClaims')
async def store_claim(claim: Claim):
    try:
        logger.info("Storing a new claim.")
        data = con.execute(Claims.insert().values(
            Id=claim.Id,
            CreatedDate=claim.CreatedDate,
            CaseNumber=claim.CaseNumber,
            HAN=claim.HAN,
            BillAmount=claim.BillAmount,
            Status=claim.Status,
            AccountId=claim.AccountId,
        ))

        if data.is_insert:
            logger.info("New claim stored successfully.")
            return {
                "Success": True,
                "msg": "New Claim stored successfully"
            }
        else:
            logger.warning("Failed to store the new claim.")
            return {
                "Success": False,
                "msg": "New Claim not stored successfully"
            }
    except Exception as e:
        logger.error(f"Error storing claim: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.delete('/api/deleteClaims/{claim_id}')
async def delete_claim(claim_id: str):
    try:
        logger.info(f"Deleting claim with Id: {claim_id}")
        result = con.execute(Claims.select().where(Claims.c.Id == claim_id)).fetchone()

        if not result:
            logger.warning(f"Claim with Id {claim_id} not found.")
            raise HTTPException(status_code=404, detail="Claim not found")

        con.execute(Claims.delete().where(Claims.c.Id == claim_id))
        logger.info(f"Claim with Id {claim_id} deleted successfully.")

        return {
            "Success": True,
            "Message": f"Claim with Id {claim_id} has been deleted."
        }
    except Exception as e:
        logger.error(f"Error deleting claim: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get('/api/AccountDetails/{account_id}')
async def fetch_account_details(account_id: str):
    try:
        logger.info(f"Fetching details for AccountId: {account_id}")
        account_result = con.execute(
            Accounts.select().where(Accounts.c.AccountId == account_id)
        ).fetchone()

        if not account_result:
            logger.warning(f"No account found with AccountId: {account_id}")
            return {
                "success": False,
                "msg": f"No account found with AccountId: {account_id}"
            }

        account_data = dict(account_result._mapping)
        logger.info(f"Fetched account data: {account_data}")

        claims_result = con.execute(
            Claims.select().where(Claims.c.AccountId == account_id)
        ).fetchall()

        claims_data = [dict(row._mapping) for row in claims_result]
        logger.info(f"Fetched claims data: {claims_data}")

        policies_data = []
        if claims_data:
            policy_ids = [claim["HAN"] for claim in claims_data if "HAN" in claim]
            policies_result = con.execute(
                Policies.select().where(Policies.c.HAN.in_(policy_ids))
            ).fetchall()

            policies_data = [dict(row._mapping) for row in policies_result]
            logger.info(f"Fetched policies data: {policies_data}")

        return {
            "success": True,
            "account": account_data,
            "claims": claims_data,
            "policies": policies_data,
        }

    except Exception as e:
        logger.error(f"Error fetching account details: {e}")
        return {
            "success": False,
            "msg": f"Error occurred: {str(e)}"
        }
