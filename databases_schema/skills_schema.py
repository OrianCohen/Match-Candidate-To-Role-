from marshmallow import Schema, fields, EXCLUDE


# Represent products schema database
class SkillsSchema(Schema):
    id = fields.Integer(allow_none=True)
    skill_name = fields.Str(allow_none=True)

    class Meta:
        unknown = EXCLUDE