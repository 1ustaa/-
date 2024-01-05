from flask import current_app, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models import Stock
from app import db


class StockAddForm(FlaskForm):
    stockname = StringField('Название склада', validators=[DataRequired()])
    place = StringField('Местоположение', validators=[DataRequired()])
    hostname = StringField('Имя владельца', validators=[DataRequired()])
    content = TextAreaField('Содержимое склада', validators=[Length(min=0, max=200)])
    contact = StringField('Контакты', validators=[DataRequired()])
    capacity = StringField('Вместимость', validators=[DataRequired()])
    submit = SubmitField('Добавить склад')

    def validate_stockname(self, stockname):
        stock = Stock.query.filter_by(stockname=stockname.data).first()
        if stock is not None:
            raise ValidationError('Имя склада уже занято! Пожалуйста, введите другое')


class StockRedactorForm(FlaskForm):

    stockname = StringField('Название склада', validators=[DataRequired()])
    place = StringField('Местоположение', validators=[DataRequired()])
    hostname = StringField('Имя владельца', validators=[DataRequired()])
    content = TextAreaField('Содержимое склада', validators=[Length(min=0, max=200)])
    contact = StringField('Контакты', validators=[DataRequired()])
    capacity = StringField('Вместимость', validators=[DataRequired()])
    submit = SubmitField('Редактировать склад')

    def validate_stockname(self, stockname):
        if stockname.data != self.stockname.default:
            existing_stock = Stock.query.filter_by(stockname=stockname.data).first()
            if existing_stock and existing_stock.id != int(request.args.get('id')):
                raise ValidationError('Имя склада уже занято! Пожалуйста, введите другое.')



'''class StockDeleteForm(FlaskForm):
    def get_stock_choices():
        with current_app.app_context():
            stocks = Stock.query.all()
            return [stock.stockname for stock in stocks]'''

'''    stockchoice = SelectField('Выберите склад для удаления', choices=get_stock_choices)
    submit = SubmitField('Удалить')'''