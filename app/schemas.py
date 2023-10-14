from typing import Optional

from pydantic import BaseModel


class AddressInput(BaseModel):
    cep: str
    logradouro: str
    complemento: Optional[str] = None
    bairro: str
    localidade: str
    uf: str
    ibge: int
    gia: int
    ddd: int


class AddressOutput(BaseModel):
    cep: str
    logradouro: str
    complemento: Optional[str] = None
    bairro: str
    localidade: str
    uf: str
