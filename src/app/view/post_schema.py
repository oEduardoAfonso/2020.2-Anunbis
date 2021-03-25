from . import ma
from marshmallow import fields, validate, validates, ValidationError
from ..model.dao import post_dao


class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = post_dao.Post

    reg_student = fields.Integer(required=True, validate=validate.Range(min=0))
    id_professor = fields.Integer(required=True, validate=validate.Range(min=0))
    discipline_code = fields.String(required=True, validate=validate.Length(max=80))
    content = fields.String(required=True, validate=validate.Length(min=1, max=480))
    rating = fields.Float(required=True, validate=validate.Range(min=0, max=10))
    is_anonymous = fields.Boolean(required=True)
    post_date = fields.Date()
