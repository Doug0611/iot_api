from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def root(q: str = None, filter: str = None):
    item = {"message": "estou na view"}
    if q is not None:
        item.update({"q": q})
    if filter is not None:
        item.update({"filter": filter})
    return item