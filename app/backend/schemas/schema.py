from typing import List

from pydantic import BaseModel, EmailStr
from fastapi import Form


class UsersInfo(BaseModel):
    name: str
    last_name: str
    surname: str
    email: EmailStr
    qualification: int
    telegram_id: str
    ready_business_trip: bool
    experience: int

    @classmethod
    def as_form(
        cls,
        name: str = Form(...),
        last_name: str = Form(...),
        surname: str = Form(...),
        email: EmailStr = Form(...),
        qualification: int = Form(...),
        telegram_id: str = Form(...),
        ready_business_trip: bool = Form(...),
        experience: int = Form(...)
    ):
        return cls(
            name=name,
            last_name=last_name,
            surname=surname,
            email=email,
            qualification=qualification,
            telegram_id=telegram_id,
            ready_business_trip=ready_business_trip,
            experience=experience,
        )


class UsersNumber(BaseModel):
    number: str

    @classmethod
    def as_form(
        cls,
        number: str = Form(
            ..., max_length=11,
            min_length=11
        )
    ):
        return cls(number=number)


class UsersProf(BaseModel):
    id_prof: List[int]

    @classmethod
    def as_form(
        cls,
        id_prof: List[int] = Form(...)
    ):
        return cls(id_prof=id_prof)


class UsersCity(BaseModel):
    city: str

    @classmethod
    def as_form(
        cls,
        city: str = Form(...)
    ):
        return cls(city=city)
