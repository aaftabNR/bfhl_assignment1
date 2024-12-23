from sqlalchemy import Table, Column, String
from config.db import meta

Policies = Table(
    "Policies",
    meta,
    Column("HAN", String(255), primary_key=True),
    Column("PolicyName", String(255)),
)
