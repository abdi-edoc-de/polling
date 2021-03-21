from flask import Blueprint,render_template
from polling.main.froms import PersonRegisterForm
main=Blueprint('main',__name__)

@main.route('/')
@main.route('/index',methods=['GET','POST'])
def index():
    person_form=PersonRegisterForm()
    
    return render_template('index.html',person_form=person_form)