from datetime import datetime
import jdatetime


def convert_to_persian_date(date_obj: datetime) -> str:
    persian_date = jdatetime.date.fromgregorian(date=date_obj)
    return f'{persian_date.year}-{persian_date.month:02d}-{persian_date.day:02d}'


def convert_to_persian_week(year: int, week: int) -> str:
    first_day_of_week = datetime.strptime(f'{year}-W{week}-1', "%Y-W%W-%w")
    jalali_date = jdatetime.date.fromgregorian(date=first_day_of_week)
    jalali_week_number = jalali_date.isocalendar()[1]
    return f'هفته {jalali_week_number} از سال {jalali_date.year}'


def convert_to_persian_month(year: int, month: int) -> str:
    miladi_date = datetime(year, month, 1)
    jalali_date = jdatetime.date.fromgregorian(date=miladi_date)
    jalali_month_name = jalali_date.j_months_fa[jalali_date.month - 1]
    return f'ماه {jalali_month_name} از سال {jalali_date.year}'

