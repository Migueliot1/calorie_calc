from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
import funct

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):

        return render_template('index.html')


class CalculatorPage(MethodView):

    def get(self):

        query_form = QueryForm()
        return render_template('calculator.html', query=query_form)


    def post(self):

        query = QueryForm(request.form)

        # Create Calories instance
        cal = funct.Calories(weight=int(query.weight.data),
                            height=int(query.height.data),
                            age=int(query.age.data),
                            country=query.country.data,
                            city=query.city.data)

        return render_template('calculator.html',
                                query = query,
                                calories=cal.calculate())


class QueryForm(Form):

    weight = StringField('Weight(kg): ', default=75)
    height = StringField('Height(cm): ', default=180)
    age = StringField('Age: ', default=30)
    country = StringField('Country: ', default='Australia')
    city = StringField('City: ', default='Sydney')

    button = SubmitField('Calculate')


app.add_url_rule('/', view_func=HomePage.as_view('index'))
app.add_url_rule('/calculator', view_func=CalculatorPage.as_view('calculator'))

app.run(debug=True)
