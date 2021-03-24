from marshmallow import Schema, fields, EXCLUDE


# Represent products schema database
class CandidatesSchema(Schema):
    id = fields.Integer(allow_none=True)
    name = fields.Str(required=True, error_messages={"required": "A candidate needs at least a name"})
    phone = fields.Integer(required=True, error_messages={"required": "A candidate requires phone"})
    city = fields.Str(required=True, error_messages={"required": "A candidate requires location"})
    title = fields.Str(required=True, error_messages={"required": "A candidate needs at least a title"})
    skills = fields.Str(allow_none=True)

    class Meta:
        unknown = EXCLUDE