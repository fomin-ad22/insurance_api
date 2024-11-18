from fastapi import FastAPI,Depends
from sqlmodel import create_engine,Session,SQLModel,select
from models import Insurance
import requests

app = FastAPI()

engine=create_engine("sqlite:///./database.db",connect_args={"check_same_thread": False})

def get_session():
    with Session(engine) as session:
            yield session

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


@app.post("/tariff/")
async def upload_tariff(tariffs:dict,session:Session= Depends(get_session)):
    if(tariffs):
        for tariff in tariffs:
            print(tariff,tariffs[tariff])
            for insure_data in tariffs[tariff]:
                newinsurance=Insurance(date=tariff,cargo_type=insure_data["cargo_type"],rate=insure_data["rate"])
                session.add(newinsurance)
                session.commit()


@app.get("/insurance/")
async def calculate_insurance(insurance_request:dict,session:Session=Depends(get_session)):
    if(insurance_request):
        insurance_in_bd = session.exec(select(Insurance).where(Insurance.cargo_type==insurance_request["cargo_type"])).all()
        print(f"Actual insurance: {insurance_in_bd[-1]}")
        return insurance_request["declared_value"]*insurance_in_bd[-1].rate
