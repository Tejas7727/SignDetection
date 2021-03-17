from flask import request, render_template, redirect, url_for, session
from project import app

from project.com.vo.ComplaintVO import ComplaintVO
from project.com.dao.ComplaintDAO import ComplaintDAO

from datetime import datetime


@app.route('/addComplaint')
def addComplaint():
    return render_template("admin/addComplaint.html")


@app.route('/loadComplaint', methods=['POST'])
def loadComplaint():
    complaintVO = ComplaintVO()
    complaintDAO = ComplaintDAO()

    complaintSubject = request.form['complaintSubject']
    complaintDescription = request.form['complaintDescription']
    complaintVO.complaintSubject = complaintSubject
    complaintVO.complaintDescription = complaintDescription
    complaintVO.complaintFrom = session['loginId']
    complaintVO.complaintActiveStatus = "active"
    complaintVO.complaintStatus = "pending"
    complaintVO.complaintDate = datetime.now()
    complaintVO.complaintTime = datetime.now()

    complaintDAO.insertComplaint(complaintVO)

    return render_template("admin/addComplaint.html")


@app.route('/viewComplaint')
def viewComplaint():
    complaintDAO = ComplaintDAO()
    complaintVO = ComplaintVO()
    complaintVO.complaintTo = session['loginId']
    datasetDict = complaintDAO.selectComplaint(complaintVO)
    return render_template("admin/viewComplaint.html",datasetDict=datasetDict)


@app.route('/loadReply', methods=['GET'])
def loadReply():
    complaintDAO = ComplaintDAO()
    complaintVO = ComplaintVO()
    complaintVO.complaintFrom = session['loginId']
    complaintVO.complaintId = request.args.get('complaintId')
    datasetDict = complaintDAO.selectComplaintReply(complaintVO)
    #print datasetDict
    return render_template("admin/replyComplaint.html", datasetDict=datasetDict)

@app.route('/addReply',methods=['POST'])
def addReply():
    complaintDAO = ComplaintDAO()
    complaintVO = ComplaintVO()
    complaintVO.complaintTo = session['loginId']
    complaintVO.complaintId = request.form['complaintId']
    complaintVO.complaintStatus = "replied"
    complaintVO.complaintReply = request.form['complaintReply']

    #print complaintVO.complaintTo
    #print complaintVO.complaintId
    #print complaintVO.complaintStatus
    #print complaintVO.complaintReply
    complaintDAO.replyComplaint(complaintVO)


    datasetDict = complaintDAO.selectComplaint(complaintVO)
    return render_template("admin/viewComplaint.html", datasetDict=datasetDict)

@app.route('/viewComplaintUser')
def viewComplaintUser():
    complaintDAO = ComplaintDAO()
    complaintVO = ComplaintVO()
    complaintVO.complaintFrom = session['loginId']
    #print complaintVO.complaintFrom
    datasetDict = complaintDAO.selectComplaintUser(complaintVO)
    #print session['loginId']
    #print complaintVO.complaintId
    #print complaintVO.complaintSubject
    #print complaintVO.complaintDescription
    #print complaintVO.complaintFrom
    #print complaintVO.complaintActiveStatus
    #print complaintVO.complaintStatus

    return render_template("admin/viewComplaintUser.html", datasetDict=datasetDict)


@app.route('/deleteComplaint', methods=['GET'])
def deleteComplaint():
    complaintDAO = ComplaintDAO()
    complaintVO = ComplaintVO()
    complaintVO.complaintId = request.args.get('complaintId')
    complaintDAO.deleteComplaint(complaintVO)
    return redirect(url_for('viewComplaintUser'))
