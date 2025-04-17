from apps.transactions.models import Transaction
from typing import Union, Dict, List
from datetime import datetime
from bson import ObjectId

from apps.transactions.date_convertors import (
    convert_to_persian_date,
    convert_to_persian_week,
    convert_to_persian_month,
)


def get_daily_transactions(
        type: str,
        merchant_id: str | None = None,
        start_date: datetime | None = None
) -> List[Dict[str, Union[str, int]]]:
    match_stage = {}
    if merchant_id:
        match_stage['merchantId'] = ObjectId(merchant_id)

    if start_date:
        match_stage['createdAt'] = {'$gte': start_date}

    pipeline = []

    if match_stage:
        pipeline.append({'$match': match_stage})

    pipeline.append({
        '$project': {
            'day': {'$dateToString': {'format': '%Y-%m-%d', 'date': '$createdAt'}},
            'amount': 1
        }
    })

    group_stage = {
        '_id': '$day'
    }

    if type == 'amount':
        group_stage['value'] = {'$sum': '$amount'}

    else:
        group_stage['value'] = {'$sum': 1}

    pipeline.append({
        '$group': group_stage
    })

    pipeline.append({
        '$project': {
            'key': '$_id',
            'value': 1,
            '_id': 0,
        }
    })
    pipeline.append({'$sort': {'key': 1}})

    result = list(Transaction.objects.aggregate(pipeline))
    for entry in result:
        entry['key'] = convert_to_persian_date(datetime.strptime(entry['key'], '%Y-%m-%d'))

    return result


def get_weekly_transactions(
        type: str,
        merchant_id: str | None = None,
        start_date: datetime | None = None,
) -> List[Dict[str, Union[str, int]]]:
    match_stage = {}
    if merchant_id:
        match_stage['merchantId'] = ObjectId(merchant_id)

    if start_date:
        match_stage['createdAt'] = {'$gte': start_date}

    pipeline = []

    if match_stage:
        pipeline.append({'$match': match_stage})

    pipeline.append({
        '$project': {
            'week': {'$isoWeek': '$createdAt'},
            'year': {'$isoWeekYear': '$createdAt'},
            'amount': 1
        }
    })

    group_stage = {
        '_id': {'year': '$year', 'week': '$week'}
    }

    if type == 'amount':
        group_stage['value'] = {'$sum': '$amount'}
    else:
        group_stage['value'] = {'$sum': 1}

    pipeline.append({'$group': group_stage})

    pipeline.append({
        '$project': {
            'key': '$_id',
            'value': 1,
            '_id': 0,
        }
    })
    pipeline.append({'$sort': {'key': 1}})

    result = list(Transaction.objects.aggregate(pipeline))
    for entry in result:
        entry['key'] = convert_to_persian_week(entry['key']['year'], entry['key']['week'])

    return result


def get_monthly_transactions(
        type: str,
        merchant_id: str | None = None,
        start_date: datetime | None = None,
) -> List[Dict[str, Union[str, int]]]:
    match_stage = {}
    if merchant_id:
        match_stage['merchantId'] = ObjectId(merchant_id)

    if start_date:
        match_stage['createdAt'] = {'$gte': start_date}

    pipeline = []

    if match_stage:
        pipeline.append({'$match': match_stage})

    pipeline.append({
        '$project': {
            'month': {'$month': '$createdAt'},
            'year': {'$year': '$createdAt'},
            'amount': 1
        }
    })

    group_stage = {
        '_id': {'year': '$year', 'month': '$month'}
    }

    if type == 'amount':
        group_stage['value'] = {'$sum': '$amount'}
    else:
        group_stage['value'] = {'$sum': 1}

    pipeline.append({'$group': group_stage})
    pipeline.append({
        '$project': {
            'key': '$_id',
            'value': 1,
            '_id': 0,
        }
    })
    pipeline.append({'$sort': {'key': 1}})

    result = list(Transaction.objects.aggregate(pipeline))
    for entry in result:
        entry['key'] = convert_to_persian_month(entry['key']['year'], entry['key']['month'])

    return result
