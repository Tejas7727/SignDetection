from flask import request,render_template,session,redirect,url_for,flash
from project import app

from project.com.dao.LoginDAO import LoginDAO
from project.com.vo.LoginVO import LoginVO

@app.route('/')
def login():
    return  render_template('admin/auth-login.html')


@app.route('/checkLogin' , methods=['POST'])

def checkLogin():
    loginDAO = LoginDAO()
    loginVO = LoginVO()

    loginVO.loginEmail = request.form["loginEmail"]
    loginVO.loginPassword = request.form["loginPassword"]

    loginDict = loginDAO.searchLogin(loginVO)
    if (len(loginDict)==0):
        return render_template("admin/auth-login.html",loginEmailErrorDict="Enter Valid Email")

    elif (loginVO.loginPassword != loginDict[0]['loginPassword']):
            return render_template("admin/auth-login.html",loginPasswordErrorDict="Enter Valid Password")
    elif (loginDict[0]['loginRole']=="user"):

            session['loginRole'] = loginDict[0]['loginRole']
            session['loginId'] = loginDict[0]['loginId']
            return redirect(url_for('loadIndexUser'))
    else:
        session['loginRole']=loginDict[0]['loginRole']
        session['loginId']=loginDict[0]['loginId']
        return redirect(url_for('loadIndex'))
@app.route('/logout')
def logout():
    session.clear()
    return render_template('admin/auth-login.html')
@app.route('/loadIndex')
def loadIndex():
    if session['loginRole'] != 'admin':
        return render_template('admin/auth-login.html')

    return render_template('admin/index.html')

@app.route('/loadIndexUser')
def loadIndexUser():
      return render_template('admin/indexUser.html')
