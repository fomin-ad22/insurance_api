from sqlmodel import SQLModel,Field

class Insurance(SQLModel,table = True):
    id:int = Field(primary_key=True)
    date:str
    cargo_type:str=Field(nullable=False)
    rate:float = Field(nullable=False)
