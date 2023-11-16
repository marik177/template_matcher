import datetime
import re
from typing import Optional, Tuple

from pydantic import BaseModel, EmailStr, ValidationError, field_validator

FIELDS = ["email", "phone", "date"]


class FormModel(BaseModel):
    """Class for parsing  data from a form."""

    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    date: Optional[str] = None

    @field_validator("phone")
    def validate_phone(cls, value):
        regex = r"^\+7\d{10}$"
        if not re.match(regex, value):
            raise ValueError(
                "The phone number must be in the format +"
                "7XXXXXXXXXX (X - number from 0 to 9) and have a "
                "length of 11"
            )
        return value

    @field_validator("date")
    def validate_date(cls, value):
        try:
            datetime.datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            try:
                datetime.datetime.strptime(value, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Date must be in the format DD.MM.YYYY or YYYY-MM-DD")
        return value


def is_valid(data):
    return data is True


def validate(data: dict):
    """Validate POST data"""
    data_to_validate, filtered_original_data = _prepare_data(data)
    try:
        FormModel(**data_to_validate)
        return True, filtered_original_data
    except ValidationError as e:
        return False, e.errors()[0]["msg"]


def _prepare_data(data: dict) -> tuple[dict, dict]:
    # Create the updated dictionary with keys from FIELDS
    data_to_validate = {
        field: data[key] for key in data for field in FIELDS if field in key
    }

    # Remove all non-mathching keys
    filtered_original_data = {
        k: v for k, v in data.items() if any(field in k for field in FIELDS)
    }
    return data_to_validate, filtered_original_data
