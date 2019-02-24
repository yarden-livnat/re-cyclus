from marshmallow import Schema, fields, pre_load, post_dump


class UserSchema(Schema):
    username = fields.Str()
    email = fields.Email()
    password = fields.Str(load_only=True)
    createdAt = fields.DateTime(attribute='created_at', dump_only=True)
    updatedAt = fields.DateTime(attribute='updated_at')

    class Meta:
        strict = True


class TokenSchema(Schema):
    id = fields.Integer()
    token_type = fields.Str()
    expires = fields.DateTime(attribute='expires')


user_schema = UserSchema()
user_schemas = UserSchema(many=True)
