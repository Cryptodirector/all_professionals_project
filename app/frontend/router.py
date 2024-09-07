from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse

from app.backend.db.service import insert_user, Info
from app.backend.schemas.schema import (
    UsersInfo,
    UsersProf,
    UsersCity,
    UsersNumber
)

router = APIRouter(
    prefix='',
    tags=['Пользователь']
)

templates = Jinja2Templates(
    directory="app/frontend/templates"
)


@router.get(
    '/registration'
)
async def get_registration(
        request: Request,
        city: list = Depends(Info.get_city),
        prof: list = Depends(Info.get_prof)
):
    return templates.TemplateResponse(
        request=request,
        name="registration.html",
        context={'city': city, 'prof': prof}
    )


@router.post(
    '/registration'
)
async def registration(
        user: UsersInfo = Depends(UsersInfo.as_form),
        prof: UsersProf = Depends(UsersProf.as_form),
        city: UsersCity = Depends(UsersCity.as_form),
        number: UsersNumber = Depends(UsersNumber.as_form)
):
    await insert_user(
        user,
        prof,
        city,
        number
    )
    return RedirectResponse(
        url='https://all-professionals.ru/redirect',
        status_code=302
    )


@router.get('/redirect')
async def red(
    request: Request,
):
    return templates.TemplateResponse(
        request=request,
        name="redirect.html",

    )
