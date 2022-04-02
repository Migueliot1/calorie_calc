from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from funct import Temperature, Calories

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):

        return render_template('index.html')


class QueryFormPage(MethodView):

    def get(self):

        return render_template('query_form_page.html')


    def post(self):

        return render_template('query_form_page.html')


class QueryForm(Form):

    weight = StringField('Weight(kg): ', default=75)
    height = StringField('Height(cm): ', default=180)
    age = StringField('Age: ', default=30)
    country = StringField('Country: ', default='Australia')
    city = StringField('City: ', default='Sydney')

    button = SubmitField('Calculate')


app.add_url_rule('/', view_func=HomePage.as_view('index'))
app.add_url_rule('/query', view_func=QueryFormPage.as_view('query_form'))

app.run(debug=True)
