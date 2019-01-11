# import enum
# class YESORNO(enum.Enum):
#     yes = 1
#     no= 2
# from django.db  import models as enum_models
# from django_enumfield import enum
# from model_utils import Choices
#
# class Article(enum_models.Model):
#     STATUS = Choices('draft', 'published')
#     status = enum_models.CharField(choices=STATUS, default=STATUS.draft, max_length=20)
# class YESORNO(enum.Enum):
#     yes = 1
#     no= 2
#
#     labels = {
#         yes: 'Yes',
#         no: 'No',
#     }
# class Status(enum_models.Model):
#      style = enum.EnumField(YESORNO, default=YESORNO.no)
#
# class EnumFiled(enum_models.Model):
#     def __init__(self, *args, **kwargs):
#         super(EnumFiled, self).__init__(*args, *kwargs)
#         assert self.choices, "Need choices fro enumeration"
#
#     def db_type(self, connection):
#         return 'enum("android","ios")'