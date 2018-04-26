from flask import Flask, render_template, request, redirect, session
import random, operator, datetime, time

app = Flask(__name__)
app.secret_key = 'ThisIsASecretKey'

@app.route('/') #This is the root
def index():
    if not ('gold' in session):
        session['gold'] = 0
    if not ('activity' in session):
        session['activity_stat'] = 0
        session['message'] = 0
        session.modified = True
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    farm_random = random.randrange(10,20)
    cave_random = random.randrange(5,10)
    house_random = random.randrange(2,5)
    casino_random = random.randrange(-50,50)
    # ts = time.time()
    # st = datetime.datetime.fromtimestamp(ts).strftime('%Y/%m/%d %H:%M:%S')
    # activity_stat = []
    
    if request.form['building'] == 'farm':
       session['gold'] += farm_random
       session['message'] ="You gained {} gold in the farm!".format(session['gold']) 
    #    session['activity_stat'].extend(session['message'])
        print len(activity_stat)
    if request.form['building'] == 'cave':
        session['gold'] += cave_random
        session['message'] = "You gained {} gold in the cave!".format(session['gold']) 
        # session['activity_stat'].extend( session['message'])
        print cave_random
    if request.form['building'] == 'house':
        session['gold'] += house_random
        session['message'] ="You gained {} gold in the house!".format(session['gold']) 
        # session['activity_stat'].extend( session['message'])
        print house_random
    if request.form['building'] == 'casino':         
        session['gold'] += casino_random
        session['message'] = "You gained/loss {} gold in the casino!".format(session['gold']) 
        # session['activity_stat'].extend(session['message'])
        print session['gold']
        print casino_random
    return render_template('index.html')
    
#need to fix the activity logs
@app.route('/restart')
def restart():

	session.pop('gold')
	return redirect('/')

app.run(debug=True)