import string
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from flask import request,render_template,session,redirect,url_for,flash
from project import app
from project.com.dao.RegisterDAO import RegisterDAO
from project.com.vo.RegisterVO import RegisterVO
from project.com.vo.LoginVO import LoginVO
from project.com.dao.LoginDAO import LoginDAO
from project.com.controller import LoginController

@app.route('/loadRegister')
def loadRegister():
    return render_template('admin/auth-register.html')

@app.route('/addRegister', methods=["POST"])
def addRegister():
    registerVO = RegisterVO()
    registerDAO = RegisterDAO()
    loginVO = LoginVO()
    loginDAO = LoginDAO()

    registerVO.registerFirstName = request.form['registerFirstName']
    registerVO.registerLastName = request.form['registerLastName']
    registerVO.registerContact = request.form['registerContact']
    registerVO.registerAddress = request.form['registerAddress']
    loginVO.loginEmail = request.form['registerEmail']
    loginVO.loginRole = 'user'

    registerPassword = ''.join((random.choice(string.ascii_letters + string.digits)) for x in range(8))

    loginVO.loginPassword = registerPassword

    #print("registerPassword=" + registerPassword)

    fromaddr = "signdetection@gmail.com"

    toaddr = loginVO.loginEmail

    msg = MIMEMultipart()

    msg['From'] = fromaddr

    msg['To'] = toaddr

    msg['Subject'] = "PYTHON PASSWORD"

    msg.attach(MIMEText(registerPassword, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()

    server.login(fromaddr, "signdetection7727")

    text = msg.as_string()

    server.sendmail(fromaddr, toaddr, text)

    server.quit()

    #print registerVO.registerFirstName
    #print registerVO.registerLastName
    #print registerVO.registerContact
    #print registerVO.registerAddress
    #print loginVO.loginEmail
    #print loginVO.loginPassword

    loginDAO.insertLogin(loginVO)
    registerVO.register_loginId = registerDAO.getmaxId()
    registerVO.register_loginId=registerVO.register_loginId[0]['MAX(loginId)']
    registerDAO.insertRegister(registerVO)

    return render_template('admin/auth-login.html')

@app.route('/viewUser')
def viewUser():
    registerVO = RegisterVO()
    registerDAO = RegisterDAO()

    datasetDict = registerDAO.selectUser()


    return render_template('admin/viewUser.html',datasetDict=datasetDict)
@app.route('/deleteUser',methods=['GET'])
def deleteUser():
    registerVO = RegisterVO()
    registerDAO = RegisterDAO()

    registerVO.register_loginId = request.args.get('loginId')
    registerDAO.deleteUser(registerVO)