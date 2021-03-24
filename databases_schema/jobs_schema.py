from marshmallow import Schema, fields, EXCLUDE


# Represent Jobs schema database
class JobsSchema(Schema):
    id = fields.Integer(allow_none=True)
    company_name = fields.Str(required=True, error_messages={"required": "A jobs needs at least a company name"})
    title = fields.Str(required=True, error_messages={"required": "A candidate needs at least a title"})
    skills = fields.Str(allow_none=True)

    class Meta:
        unknown = EXCLUDE