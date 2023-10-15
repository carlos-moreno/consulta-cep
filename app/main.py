import requests
from bootstrap import mongodb
from fastapi import FastAPI, Path, Request
from fastapi.responses import JSONResponse

from app import schemas

app = FastAPI()
mongodb.install(app)


class CepNotFoundException(Exception):
    pass


async def save_address(address: dict):
    app.db.insert_one(address)


@app.exception_handler(CepNotFoundException)
async def cep_not_found_handler(request: Request, exc: CepNotFoundException):
    return JSONResponse(
        status_code=404, content={"message": "Cep não encontrado"}
    )


@app.get("/address/{cep}", response_model=schemas.AddressOutput, tags=["search"])
async def search_address_by_cep(cep: str = Path(max_length=9, min_length=9)):
    """Search for an address according to the zip code entered

    The format used for the query must be:
    > `99999-999`
    """
    address = app.db.find_one({"cep": cep})

    if not address:
        response = requests.get(f"http://viacep.com.br/ws/{cep}/json/")
        address = response.json()

        if "erro" in address:
            raise CepNotFoundException

        await save_address(address)
    return address
