from sqlalchemy import Table, Column, Integer, String, Float, TIMESTAMP, MetaData

metadata = MetaData()


operation = Table(
    "operation",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("item_name", String),
    Column("operation_type", String),
    Column("price", String),
    Column("date", TIMESTAMP)
)

