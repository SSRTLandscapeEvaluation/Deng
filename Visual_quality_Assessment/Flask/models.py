# 根据数据库表结构创建数据库模型

from exts import db
from datetime import datetime


class imagesinfodf(db.Model):
    index = db.Column(db.Integer, primary_key=True, autoincrement=True)
    imagename = db.Column(db.Text)
    time = db.Column(db.Text)
    long = db.Column(db.Float)
    lat = db.Column(db.Float)


class Imageseval(db.Model):
    __tablename__ = 'imageseval'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    imagename = db.Column(db.String(255), nullable=False)
    good = db.Column(db.Integer)
    medium = db.Column(db.Integer)
    poor = db.Column(db.Integer)
    eval = db.Column(db.Text)
    eval_time = db.Column(db.DateTime, default=datetime.now)
    #image_id == db.Column(db.Integer, db.ForeignKey('imagesinfodf.index'))
    #image_info == db.relationship('imagesinfodf', backref=db.backref('img_info'))
