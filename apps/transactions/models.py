from mongoengine import Document, IntField, DateTimeField, ObjectIdField


class Transaction(Document):
    merchantId = ObjectIdField(required=True)
    amount = IntField(required=True)
    createdAt = DateTimeField(required=True)

    meta = {
        'collection': 'transaction'
    }
