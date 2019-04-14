from datetime import date

from ariadne import ScalarType

date_scalar = ScalarType("Date")


@date_scalar.serializer
def serialize_date(value: str):
    return date.fromisoformat(value).isoformat() if value != "" else None
