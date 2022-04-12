

import os
from flask import*
from werkzeug.utils import secure_filename

app = Flask (__name__)
app.secret_key="key"
from src.dbconnection import *

import functools
def login_required(func):
    @functools.wraps(func)
    def secure_function():
        if "lid"  not in session:
            return redirect ("/")
        return func()
    return secure_function

@app.route("/")
def login():
    return render_template("admin/login.html")

@app.route("/getLogin",methods=['post','get'])
def getLogin():
    uname = request.form['textfield']
    pwd = request.form['textfield2']
    qry = "select * from login where username =%s and password=%s"
    vals =(uname,pwd)
    result= selectone(qry,vals)
    if result is None:
        return '''<script>alert ("no result");window.location="/"</script>'''
    elif result[3] =='admin':
        session['lid']= result[0]
        return render_template("admin/home.html")
    elif result[3] =="contractor" :
        session['lid']= result[0]
        return  render_template("CONTRACTOR/home.html")
    elif result[3] =="user" :
        session['uid']= result[0]
        return  render_template("user/home.html")    
    else :
        return '''<script>alert("sorry invalid");window.location="/"</script>'''
        


@app.route("/signup")
def signup():
    return render_template("admin/signup.html")

@app.route("/Adminlaoyt")

def Adminlaoyt():
    return render_template("admin/home.html")    

@app.route("/add_signup",methods=['post'])
def add_signup():
    catogary = request.form['catogary']
    print(catogary)
    if(catogary == 'Contractor'):
                 username = request.form['user']
                 password = request.form['password']
                 fname = request.form['textfield']
                 lname = request.form['textfield1']
                 gender = request.form['textfield3']
                 place = request.form['textfield4']
                 post = request.form['textfield5']
                 pincode = request.form['textfield6']
                 phone = request.form['textfield7']
                 service = request.form['textfield8']
                 logqry = "INSERT INTO `login` VALUES (NULL,%s,%s,'contractor')"
                 logval=(username,password)
                 lid=iud(logqry,logval)
                 qry = "INSERT INTO `contractor` VALUES (NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                 val = (fname, lname, gender, place,post,pincode,phone,service,str(lid))
                 iud(qry,val)
                 return '''<script>alert("signup successfully");window.location="/contracters"</script>'''
    else :
                 username = request.form['user']
                 password = request.form['password']
                 fname = request.form['textfield']
                 lname = request.form['textfield1']
                 place = request.form['textfield4']
                 post = request.form['textfield5']
                 pincode = request.form['textfield6']
                 phone = request.form['textfield7']
                 logqry = "INSERT INTO `login` VALUES (NULL,%s,%s,'user')"
                 logval=(username,password)
                 lid=iud(logqry,logval)
                 print(lid)
                 qry = "INSERT INTO `users` VALUES (NULL,%s,%s,%s,%s,%s,%s,%s)"
                 val = (fname, lname, place,post,pincode,phone,str(lid))
                 iud(qry,val)
                 return '''<script>alert("signup successfully");window.location="/user"</script>'''


@app.route("/logout")
def logout():
    return redirect('/')


# @app.route("/contractor")
# def contractor():
#     qry="SELECT contractor.* FROM login JOIN contractor ON login.loginid=contractor.loginid WHERE login.usertype ='pending'"
#     res=select(qry)
#     return render_template("admin/contractor.html",val=res)



# @app.route("/AcceptContractor")
# def AcceptContractor():
#     id=request.args.get('id')
#     accept='contractor'
#     qry="UPDATE `login` SET `usertype`=%s WHERE `loginid`=%s"
#     val=(accept,id)
#     iud(qry,val)
#     return '''<script>alert("accept successfully");window.location="/contractor"</script>'''


# @app.route("/RejectContractor")
# def RejectContractor():
#     id=request.args.get('id')
#     qry="DELETE FROM`login`WHERE `loginid`=%s"
#     iud(qry,str(id))
#     return '''<script>alert("reject successfully");window.location="/contractor"</script>'''

@app.route("/ViewContractor")
@login_required

def ViewContractor():
    qry="SELECT * FROM contractor "
    res=select(qry)
    return render_template("admin/ViewContractor.html",val=res)


@app.route("/ApproveRejectContractor")
def ApproveRejectContractor():
    id=request.args.get('id')
    qry="DELETE FROM`contractor`WHERE `loginid`=%s"
    iud(qry,str(id))
    return '''<script>alert("reject successfully");window.location="/ViewContractor"</script>'''


@app.route("/view_users")
@login_required
def view_users():
    qry="SELECT users.* FROM login JOIN users ON login.loginid = users.loginid "
    res=select(qry)
    return render_template("admin/view users.html",val=res)

# @app.route("/view_job_vacancy")
# def view_job_vacancy():
#     qry = "SELECT * FROM `contractor`"
#     res=select(qry)
#     return render_template("admin/view_job_vacancy.html",val=res)



# @app.route("/view_job_vacancynew",methods=['post'])
# def view_job_vacancynew():
#     service =request.form['service']
#     qry = "SELECT `contractor`.*,`vaccancy`.* FROM `vaccancy` JOIN `contractor` ON `contractor`.`loginid`=`vaccancy`.`contractid` WHERE `contractor`.`sevice`=%s"
#     val=(service)
#     res=selectall(qry,val)
#     return render_template("admin/view_job_vacancy.html",val1=res)

@app.route("/view_feedback")
# @login_required
def view_feedback():
    qry ="SELECT  `users`. *,feedback.*,`contractor`.* FROM  feedback JOIN users ON `users`.`loginid`=`feedback`.`userid` join `contractor` on `contractor`.`loginid`=`feedback`.`cid`"
    res=select(qry)

    return render_template("admin/view feedback.html",val=res)

@app.route("/view_complains")
# @login_required
def view_complains():
    qry= "SELECT users.*,complaint.*,`contractor`.* FROM `complaint` JOIN `users` ON `users`.`loginid`=`complaint`.`userid` JOIN `contractor` ON `contractor`.`loginid`=`complaint`.`conid` WHERE `complaint`.`replay`='pending'"
    res=select(qry)
    return render_template("admin/view complains.html",val=res)


@app.route("/sent_replynew")
# @login_required
def sent_replynew():
    id = request.args.get('id')
    session['id']=id
    return render_template("admin/sent reply.html" )

@app.route("/sent_reply",methods=['post'] )
def sent_reply():
    replay = request.form['textarea']
    qry ="UPDATE `complaint` SET `replay` = %s WHERE `complaintid`=%s"
    val=(replay,session['id'])
    iud(qry,val)
    return '''<script>alert("reply successfully");window.location="view_complains"</script>'''


@app.route("/admins")
# @login_required
def admins():
    return render_template("admin/home.html")



@app.route("/block_user_and_contractor")
# @login_required
def block_user_and_contractor():
    qry = "SELECT * FROM `contractor`"
    res = select(qry)
    return render_template("admin/block user and contractor.html",val=res)



@app.route("/manege_Vaccancy")
# @login_required
def manege_Vaccancy():
    return render_template("admin/manege_Vaccancy.html")



@app.route("/view_contractor_vacancy")
# @login_required
def view_contractor_vacancy():
    return render_template("admin/view contractor vacancy.html")



# *****************************************************************************************************



@app.route("/contracters")
# @login_required
def contracters():
    return render_template("CONTRACTOR/home.html")


@app.route("/add_job_vacancy")
# @login_required
def add_job_vacancy():
    return render_template("CONTRACTOR/ADD JOB VACCANCY.html")


@app.route("/add_skill_and_vaccancy")
# @login_required
def add_skill_and_vaccancy():
    return render_template("CONTRACTOR/ADD SKILL AND DETAILS.html")

@app.route("/new_add_skill_and_vaccancy",methods=['post'])
def new_add_skill_and_vaccancy():
    conid=session['lid']
    skill = request.form['textfield1']
    exprience = request.form['textfield2']
    work = request.form['Document']
    qry="INSERT INTO `features` VALUES (NULL,%s,%s,%s,%s)"
    val=(conid,skill,exprience,work)
    iud(qry,val)
    return '''<script>alert("added successfully");window.location="/add_skill_and_vaccancy"</script>'''

@app.route("/add_new")
# @login_required
def add_new():
    return render_template("CONTRACTOR/addnew.html")

@app.route("/get_add_new" ,methods=['post'])
def get_add_new():
    job=request.form['textfield1']
    vaccancy = request.form['textfield2']
    details = request.form['textfield3']
    qry="INSERT INTO `vaccancy` VALUES (NULL,%s,%s,%s,CURDATE(),%s)"
    val=(job,details,session['lid'],vaccancy)
    iud(qry,val)
    return '''<script>alert("added successfully");window.location="/manege_vaccancy"</script>'''

@app.route("/delete", methods=['post','get'])
def delete():
    id = request.args.get('id')
    qry="DELETE FROM `vaccancy` WHERE  `vaccid`=%s "
    iud(qry,id)
    return '''<script>alert("delete successfully");window.location="/manege_vaccancy"</script>'''

@app.route("/edit_new")
# @login_required
def edit_new():
    id = request.args.get('id')
    session['editid']=id
    qry="SELECT * FROM `vaccancy` WHERE `vaccid`=%s"
    res=selectone(qry,id)
    return render_template("CONTRACTOR/editnew.html",val=res)

@app.route("/edit_new_vacancy", methods=['post'])
def edit_new_vacancy():
    job=request.form['textfield1']
    vaccancy = request.form['textfield2']
    details = request.form['textfield3']
    qry="UPDATE `vaccancy` SET `job` =%s ,`details`=%s,`vacancy`=%s where vaccid=%s "
    val=(job,vaccancy,details,session['editid'])
    iud(qry,val)
    return '''<script>alert("edit successfully");window.location="/manege_vaccancy"</script>'''


@app.route("/manege_vaccancy")
# @login_required
def manege_vaccancy():
    qry="SELECT * FROM `vaccancy` "
    res=select(qry)
    return render_template("CONTRACTOR/MANEGE VACCANCY.html",val=res)




@app.route("/view_job_request")
# @login_required
def view_job_request():
    qry="SELECT users.*,`vaccancy`.*,`applyjob`.* FROM `vaccancy` JOIN `applyjob` ON `vaccancy`.`vaccid`=`applyjob`.`vacancyid` JOIN `users` ON `users`.`loginid`=`applyjob`.`userid` WHERE `applyjob`.`status`='pending'"
    res=select(qry)
    return render_template("CONTRACTOR/VIEW JOB REQUEST.html",val=res)

@app.route("/AcceptJobRequest")
# @login_required
def AcceptJobRequest():
    accept='accept'
    id = request.args.get('id')
    qry="UPDATE applyjob SET  status = %s WHERE applyid=%s"
    val=(accept,id)
    iud(qry,val)
    return '''<script>alert("Accept successfully");window.location="/view_job_request"</script>'''

@app.route("/RejectJobRequest")
# @login_required
def RejectJobRequest():
    Reject='Reject'
    id = request.args.get('id')
    qry="UPDATE applyjob SET  status = %s WHERE applyid=%s"
    val=(Reject,id)
    iud(qry,val)
    return '''<script>alert("Accept successfully");window.location="/view_job_request"</script>'''

@app.route("/view_feedbacks")
# @login_required
def view_feedbacks():
    qry="SELECT users.*,`feedback`.* FROM `feedback` JOIN `users` ON `users`.`loginid`=`feedback`.`userid` "
    res=select(qry)
    return render_template("CONTRACTOR/view feedback.html",val=res)



@app.route("/view_request")
# @login_required
def view_request():
    qry="SELECT users.*,`request`.* FROM `request` JOIN `users` ON `users`.`loginid`=`request`.`userid` "
    res=select(qry)
    return render_template("CONTRACTOR/view request.html",val=res)

@app.route("/accept_request")
def accept_request():
    accept = "accept"
    id = request.args.get('id')
    session['id'] = id
    qry = "UPDATE `request` SET `status` = %s WHERE requestid =%s"
    val = (accept, session['id'])
    iud(qry, val)
    return '''<script>window.location="/view_request"</script>'''

@app.route("/reject_request")
def reject_request():
    id = request.args.get('id')
    session['id'] = id
    qry = "DELETE FROM request WHERE requestid =%s"
    iud(qry,id)
    return '''<script> window.location="/view_request"</script>'''

@app.route("/view_request_Deatails")
# @login_required
def view_request_Deatails():
    return render_template("CONTRACTOR/workDeatails.html")



@app.route("/Get_view_request_Deatails",methods=['post'])
def Get_view_request_Deatails():
    details = request.form['Deatail']
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join("static",filename))
    qry="INSERT INTO `workdeatails` VALUES (NULL,%s,%s,%s)"
    val=(details,filename,session['lid'])
    iud(qry,val)
    return '''<script>alert("Add successfully");window.location="/view_request"</script>'''

@app.route("/status")
# @login_required
def status():
    return render_template("CONTRACTOR/status.html")



@app.route("/view_work")
# @login_required
def view_work():
    qry="SELECT `users`.*,`works`.* FROM `users` JOIN `works` ON  `users`.`loginid`=`works`.`loginid` "
    res=select(qry)
    return render_template("CONTRACTOR/view work.html",val=res)


@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    print(filename)
    print(app.root_path)
    full_path = os.path.join(app.root_path, "static")
    print(full_path)
    return send_from_directory(full_path, filename)

@app.route("/Massege_view_work")
# @login_required
def Massege_view_work():
    accept='your work accept'
    id = request.args.get('id')
    qry="UPDATE works SET  status = %s WHERE workid =%s"
    val=(accept,id)
    iud(qry,val)
    return '''<script>alert("Request successfully");window.location="/view_work"</script>'''

# ****************************************************************************************************************

@app.route("/user")
# @login_required
def user():
    return render_template("user/home.html")

@app.route("/ViewContractorWork")
# @login_required
def ViewContractorWork():
    qry="SELECT `contractor`.*,`features`.* FROM `contractor` JOIN `features` ON `contractor`.`loginid`=`features`.`contractid` "
    res=select(qry)
    return render_template("user/ViewContractorWork.html",val=res)

@app.route("/GetViewContractorWork",methods=['post'])
def GetViewContractorWork():
    servis =request.form['catogary']
    place =request.form['place']
    qry="SELECT `contractor`.*,`features`.* FROM `contractor` JOIN `features` ON `contractor`.`cid`=`features`.`contractid` WHERE `contractor`.`sevice`=%s OR `contractor`.`place`=%s"
    val1=(servis,place)
    res=selectall(qry,val1)
    return render_template("user/GetViewContractorWork.html",val=res)

@app.route("/Add_work")
# @login_required
def Add_work():
    return render_template("user/AddWork.html")   

@app.route("/Get_Add_work",methods=['post'])
def Get_Add_work():
     Work =request.form['Work']
     file = request.files['Document']
     filename = secure_filename(file.filename)
     file.save(os.path.join("static",filename))
     qry="INSERT INTO `works` VALUES (NULL,%s,%s,%s,'pending')"
     val=(session['uid'],Work,filename)
     iud(qry,val)
     return '''<script>alert("Add successfully");window.location="/Add_work"</script>'''

@app.route("/ViewVaccancy")
# @login_required
def ViewVaccancy():
    qry="SELECT `contractor`.*,`vaccancy`.* FROM `contractor` JOIN `vaccancy`  ON `contractor`.`loginid`=`vaccancy`.`contractid`"
    res=select(qry)
    return render_template("user/ViewVaccancy.html",val=res) 

@app.route("/GetViewVaccancy",methods=['post'])
def GetViewVaccancy():
    servis =request.form['catogary']
    place =request.form['place']
    qry="SELECT `contractor`.*,`vaccancy`.* FROM `contractor` JOIN `vaccancy`  ON `contractor`.`cid`=`vaccancy`.`contractid`  WHERE `contractor`.`sevice`=%s OR `contractor`.`place`=%s"
    val1=(servis,place)
    res=selectall(qry,val1)
    return render_template("user/GetViewVaccancy.html",val=res)

@app.route("/ApplyJob")
# @login_required
def ApplyJob():
    id = request.args.get('id')
    session['rid'] = id
    return render_template("user/ApplyJob.html")  

@app.route("/GetApplyjob",methods=['post'])
def GetApplyjob():
    file =request.form['file']
    qry="INSERT INTO `Applyjob` VALUES (NULL,%s,%s,CURDATE(),'pending',%s)"
    val=(session['rid'],session['uid'],file)
    iud(qry,val)
    return '''<script>alert("Apply successfully");window.location="/ViewVaccancy"</script>'''

@app.route("/WorkDeatails")
# @login_required
def WorkDeatails():
    id = request.args.get('id')
    session['cid'] = id
    qry="SELECT `contractor`.*,`features`.* FROM `contractor` JOIN `features` ON `contractor`.loginid=`features`.`contractid` WHERE `contractor`.`loginid`=%s"
    res=selectone(qry,id)
    qry1="SELECT `users`.*,`feedback`.* FROM `users` JOIN `feedback` ON `users`.`loginid`=`feedback`.`userid` WHERE `feedback`.`cid`=%s"
    res1=selectall(qry1,id)
    return render_template("user/WorkDeatail.html",val=res,val1=res1)

@app.route("/Work_Request")
# @login_required
def Work_Request():
    return render_template("user/WorkDeitailFile.html")  

@app.route("/Get_Work_Request",methods=['GET', 'POST'])
def Get_Work_Request():
    fil =request.files['files'] 
    filename = secure_filename(fil.filename)
    fil.save(os.path.join("static",filename))
    qry="INSERT INTO `request` VALUES (NULL,%s,%s,%s,CURDATE(),'pending')"
    val=(session['uid'],session['cid'],filename)
    iud(qry,val)
    return '''<script>alert("Work Request successfully");window.location="/ViewContractorWork"</script>'''


@app.route("/ViewWorkREquest")
# @login_required
def ViewWorkREquest():
    qry="SELECT `contractor`.*,`request`.* FROM `request` JOIN `contractor` ON `contractor`.`loginid`=`request`.`conid` WHERE `request`.`status`='pending' OR `request`.`status`='accept'"
    res=select(qry)
    return render_template("user/ViewWorkREquest.html",val=res)


@app.route("/RemoveViewWorkREquest")
# @login_required
def RemoveViewWorkREquest():
    id = request.args.get('id')
    qry="DELETE FROM request WHERE requestid =%s"
    iud(qry,id)
    return '''<script>alert("Delete successfully");window.location="/ViewWorkREquest"</script>'''

@app.route("/Sent_Complaints")
# @login_required
def Sent_Complaints():
    id = request.args.get('id')
    session['Sid'] = id
    qry="SELECT * FROM `complaint` WHERE `conid`=%s"
    res=selectone(qry,id)
    return render_template("user/SentComplaint.html",val=res) 

@app.route("/Get_Sent_Complaints",methods=['post'])
def Get_Sent_Complaints():
    Complaint =request.form['Complaint']
    qry="INSERT INTO `complaint` VALUES (NULL,%s,CURDATE(),%s,'pending',%s)"
    val=(Complaint,session['uid'],session['Sid'])
    iud(qry,val)
    return '''<script>alert(" successfully");window.location="/ViewWorkREquest"</script>'''

@app.route("/View_WOrk_Deatails_Request_Work")
# @login_required
def View_WOrk_Deatails_Request_Work():
    id = request.args.get('id')
    session['contraid'] = id
    qry="SELECT * FROM `workdeatails` WHERE `cid`=%s"
    res=selectone(qry,id)
    return render_template("user/View_WOrk_Deatails_Request_Work.html",val=res) 

@app.route("/FeedBack")
# @login_required
def FeedBack():
    id = request.args.get('id')
    session['feedid'] = id
    return render_template("user/FeedBack.html") 

@app.route("/Get_FeedBack",methods=['post'])
def Get_FeedBack():
    FeedBack =request.form['FeedBack']
    qry="INSERT INTO `feedback` VALUES (NULL,%s,%s,CURDATE(),%s)"
    val=(FeedBack,session['uid'],session['feedid'])
    iud(qry,val)
    return '''<script>alert("Feedback add successfully");window.location="/ViewWorkREquest"</script>'''

@app.route('/page')
# @login_required
def Location():
	return render_template('admin/index.html')

if __name__ == "__main__":
    app.run(debug=True)


