from fastapi import APIRouter, Request
from starlette import status
from starlette.responses import JSONResponse


router = APIRouter()


@router.get(
    "/income",
    name='api:income',
    status_code=status.HTTP_200_OK
)
async def income(request: Request):
    try:
        pass
    except:
        pass

    a = await request.json()
    print(a)
    return JSONResponse(
        {'response': "HELLO FROM ORKS!"}
    )


@router.get(
    "/outcome",
    name='api:outcome',
    status_code=status.HTTP_200_OK
)
async def outcome(request: Request):
    return JSONResponse(
        {'response': "HELLO FROM ORKS!"}
    )


@router.get(
    "/new",
    name='api:new',
    status_code=status.HTTP_200_OK
)
async def new(request: Request):
    return JSONResponse(
        {'response': "HELLO FROM ORKS!"}
    )

