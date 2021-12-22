from datetime import datetime
from dateutil import parser as date_parser


def parse_date(date):
    if date:
        return date_parser.parse(date)
    return datetime.today()
