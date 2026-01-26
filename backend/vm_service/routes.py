from fastapi import APIRouter
from .appliance import import_ova

router = APIRouter()

@router.post("/vm/import")
def import_vm(path: str):
    return import_ova(path)
