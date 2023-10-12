import requests

from fastapi import FastAPI, Path, Request
from fastapi.responses import JSONResponse

from app import schemas
from bootstrap import mongodb


app = FastAPI()
mongodb.install(app)


class CepNotFoundException(Exception):
    pass



async def save_address(address: dict):
    app.db.insert_one(address)


@app.exception_handler(CepNotFoundException)
async def cep_not_found_handler(request: Request, exc: CepNotFoundException):
    return JSONResponse(status_code=404, content={"message": "Cep não encontrado"})


@app.get("/address/{cep}", response_model=schemas.AddressOutput)
async def search_adderss_by_cep(cep: str = Path(max_length=8, min_length=8)):
    address = app.db.find_one({"cep": f"{cep[:5]}-{cep[5:]}"})

    if not address:
        response = requests.get(f"http://viacep.com.br/ws/{cep}/json/")
        address = response.json()

        if "erro" in address:
            raise CepNotFoundException

        await save_address(address)
    return address
