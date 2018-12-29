from app import ma
from marshmallow import post_load, fields
from flask import request
from app.validatros import *


class AuthorNameSchema(ma.ModelSchema):
    class Meta:
        model = AuthorName
        fields = ('name',)


class BookSchema(ma.ModelSchema):
    class Meta:
        model = Book
    authors_names = ma.Nested(AuthorNameSchema, many=True)


class ClientSchema(ma.ModelSchema):
    class Meta:
        model = Client
        strict = True
        exclude = ('id', 'password_hash', 'opinions')
    email = fields.Email(validate=validate_email, required=True)

    @post_load
    def set_password_hash(self, client):
        password = request.json.get('password')
        client.hash_password(password)
        return client


class RegistrationClientSchema(ClientSchema):
    class Meta:
        strict = True
    password = fields.String(required=True, validate=validate_password)


author_name_schema = AuthorNameSchema()
book_schema = BookSchema()
books_schema = BookSchema(many=True)
client_schema = ClientSchema()
registration_client_schema = RegistrationClientSchema()
