from sqlalchemy import Table, Column, Integer, String, Date, DECIMAL
from config.db import meta

Claims = Table(
    'Claims', meta,
    Column('Id', String(255), primary_key=True),
    Column('CreatedDate', Date),
    Column('CaseNumber', String(255)),
    Column('HAN', String(255)),
    Column('BillAmount', DECIMAL(10, 2)),
    Column('Status', String(50)),
    Column('AccountId', String(18))
)