from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email= StringField(label="email", validators=[DataRequired(),Email()])
    password= PasswordField(label="password", validators=[DataRequired(), Length(min=6)])
    submit= SubmitField(label="submit")

app= Flask(__name__)

app.secret_key = "any-string-you-want"
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template("index.html")



@app.route("/login", methods=["GET","POST"])
def login():
    form= LoginForm()
    form.validate_on_submit()
    if form.validate_on_submit():
        if form.email.data== "admin@admin.it" and form.password.data== "123456":
            return "SUCCESS"

    return render_template("login.html", form=form)





if __name__ =="__main__":
    app.run(debug=True)


