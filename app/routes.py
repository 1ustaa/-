from app import app, db
from flask import render_template, url_for, redirect, flash, request
from app.forms import StockAddForm, StockRedactorForm
from app.models import Stock


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    stocks = Stock.query.all()
    return render_template('index.html', title='Склад', stocks=stocks)


@app.route('/stock_add', methods=['GET', 'POST'])
def stock_add():
    form = StockAddForm()
    if form.validate_on_submit():
        stock = Stock(
            stockname=form.stockname.data,
            place=form.place.data,
            hostname=form.hostname.data,
            content=form.content.data,
            contact=form.contact.data,
            capacity=form.capacity.data)
        db.session.add(stock)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('stock_add.html', title='Добавить склад', form=form)


@app.route('/stock_redactor', methods=['GET', 'POST'])
def stock_redactor():

    stock_id = request.args.get('id')
    stock_to_change = Stock.query.filter_by(id=stock_id).first()
    form = StockRedactorForm(obj=stock_to_change)
    if form.validate_on_submit():
        stock_to_change.stockname = form.stockname.data
        stock_to_change.place = form.place.data
        stock_to_change.hostname = form.hostname.data
        stock_to_change.content = form.content.data
        stock_to_change.contact = form.contact.data
        stock_to_change.capacity = form.capacity.data
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('stock_redactor.html', form=form, title='Редактирование склада')

@app.route('/stock_delete/<int:id>', methods=['POST', 'GET'])
def stock_delete(id):
    stock_to_delete = Stock.query.get_or_404(id)
    db.session.delete(stock_to_delete)
    db.session.commit()
    flash('Склад удален успешно', 'success')
    return redirect(url_for('index'))
