from flask_wtf import FlaskForm
from wtforms import FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired

class MovementsForm(FlaskForm):
    from_coin = SelectField('from_coin', validators=[DataRequired()],  
                            choices= [("EUR", "EUR"), ("ETH", "ETH"), ("BNB", "BNB"),
                                     ("ADA", "ADA"), ("DOT", "DOT"), ("BTC", "BTC"),
                                     ("XRP", "XRP"), ("SOL", "SOL"), ("MATIC", "MATIC")], )
                                     
    to_coin = SelectField('to_coin', validators=[DataRequired()],
                            choices= [("EUR", "EUR"), ("ETH", "ETH"), ("BNB", "BNB"),
                                    ("ADA", "ADA"), ("DOT", "DOT"), ("BTC", "BTC"),
                                    ("XRP", "XRP"), ("SOL", "SOL"), ("MATIC", "MATIC")])

    from_quantity = FloatField('from_quantity', validators=[DataRequired()])
    to_quantity = FloatField('to_quantity')
    unit_price = FloatField('unit_price')

    calculate_button = SubmitField('calculate')
    buy_button = SubmitField('buy')



