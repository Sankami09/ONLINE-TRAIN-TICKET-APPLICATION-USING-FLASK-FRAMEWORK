from flask import Flask,render_template,request,redirect
import pymysql
app=Flask(__name__)
@app.route('/home')
def a():
    return "WELCOME FOR ONLINE TRAIN TICKET"
@app.route('/')
def home():
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="trainapp")
        ssql="select * from ticket"
        cu=db.cursor()
        cu.execute(ssql)
        data=cu.fetchall()
        db.commit()
        print(data)
        return render_template('dashboard.html',d=data)
    except Exception:
        print("the error is",Exception)
    return render_template('dashboard.html')


@app.route('/form')
def form():
    return render_template('form.html')
@app.route('/store',methods=['POST'])
def store():
    pn=request.form['Name']
    ge=request.form['Gender']
    ag=request.form['Age']
    dj=request.form['DateOfJourney']
    cl=request.form['Coach']
    sp=request.form['ArrivalPoint']
    dp=request.form['DestinationPoint']
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="trainapp")
        insql="insert into ticket(Name,Gender,Age,DateOfJourney,Coach,ArrivalPoint,DestinationPoint)values('{}','{}','{}','{}','{}','{}','{}')".format(pn,ge,ag,dj,cl,sp,dp)
        cu=db.cursor()#execute sql queries
        cu.execute(insql)
        db.commit()
        return redirect('/')
    except Exception:
        print("Error is",Exception)

@app.route('/delete/<rid>')
def delete(rid):
    #return "Id is"+rid
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="trainapp")
        cus=db.cursor()
        dsql="delete from ticket where Id={}".format(rid)
        cus.execute(dsql)
        db.commit()
        return redirect('/')
    except Exception:
        print("The error is",Exception)
@app.route('/edit/<rid>')
def edit(rid):
    #return "ID is:"+rid
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="trainapp")
        cu=db.cursor()
        sql="select * from ticket where Id= '{}'".format(rid)
        cu.execute(sql)
        data=cu.fetchone()
        return render_template('editform.html',d=data)
        
    except Exception as e:
        print("Error:",e)
 
@app.route('/update/<rid>',methods=['POST'])
def update(rid):
    #return "ID to be  update in db is:"+rid
    pn=request.form['Name']
    ge=request.form['Gender']
    ag=request.form['Age']
    dj=request.form['DateOfJourney']
    cl=request.form['Coach']
    sp=request.form['ArrivalPoint']
    dp=request.form['DestinationPoint']
    #return t+dt+d
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="trainapp")
        cu=db.cursor()
        sql="update ticket SET Name='{}',Gender='{}',Age='{}',DateOfJourney='{}',Coach='{}',ArrivalPoint='{}',DestinationPoint='{}' where Id='{}'".format(pn,ge,ag,dj,cl,sp,dp,rid)
        cu.execute(sql)
        db.commit()
        return redirect('/')
    except Exception as e:
        print("Error:",e)

app.run()
