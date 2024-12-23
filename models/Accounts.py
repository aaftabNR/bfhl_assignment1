from config.db import meta
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String

Accounts = Table(
    'Accounts', meta,
    Column('AccountId', String(18), primary_key=True),
    Column('Name', String(255)),
    Column('Age', Integer),
    Column('City', String(255)),
    Column('State', String(255)),
    Column('Pincode', String(10))
)
