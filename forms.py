from wtforms import Form, BooleanField, TextField, PasswordField, validators, SelectField, IntegerField, DateTimeField

class RegistrationForm(Form):
    name 			= TextField('Name', [validators.Length(min=4, max=25)])
    email 			= TextField('Email Address', [validators.Length(min=6, max=35)], validators.Email())
    password 		= PasswordField('New Password', [validators.Required(), validators.EqualTo('confirm', message='Passwords must match')])
    confirm 		= PasswordField('Repeat Password')
    business_name 	= TextField('Business Name', [validators.Length(min=4, max=25)])
    website_url 	= TextField('Website Url', [validators.Length(min=6, max=100)])
    shopping_cart 	= TextField('Shopping Cart', [validators.Length(min=4, max=25)])
    trees_per_order	= SelectField('Trees Per Order')
    card_number		= IntegerField('Card Number', [validators.Length(min=4, max=30)])	
    expiration		= DateTimeField('Expiration')
    ccv				= IntegerField('CCV', [validators.Length(min=3, max=10)])				