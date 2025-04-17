from mongoengine import Document, IntField, DateTimeField, ObjectIdField, StringField, ListField, DictField


class Transaction(Document):
    merchantId = ObjectIdField(required=True)
    amount = IntField(required=True)
    createdAt = DateTimeField(required=True)

    meta = {
        'collection': 'transaction'
    }


class TransactionSummary(Document):
    mode = StringField(required=True, choices=['daily', 'weekly', 'monthly'])
    summary = ListField(DictField())
    lastUpdate = DateTimeField(required=True)

    meta = {
        'collection': 'transaction_summary'
    }
