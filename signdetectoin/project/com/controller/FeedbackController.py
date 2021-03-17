from flask import request,render_template,redirect,url_for,session
from project import app
from datetime import datetime
from project.com.vo.FeedbackVO import FeedbackVO
from project.com.dao.FeedbackDAO import FeedbackDAO

@app.route('/addFeedback')

def addFeedback():
    return render_template('admin/addFeedback.html')

@app.route('/loadFeedback',methods=['POST'])

def loadFeedback():
    feedbackVO = FeedbackVO()
    feedbackDAO = FeedbackDAO()
    feedbackVO.feedbackFrom = session['loginId']
    feedbackVO.feedbackRating = request.form["rating"]
    feedbackVO.feedbackDescription = request.form["feedbackDescription"]
    feedbackVO.feedbackDate = datetime.now()
    feedbackVO.feedbackTime = datetime.now()
    feedbackVO.feedbackActiveStatus = 'active'

    feedbackDAO.insertFeedback(feedbackVO)

    return render_template('admin/addFeedback.html')
@app.route('/viewFeedback')
def viewFeedback():
    feedbackVO = FeedbackVO()
    feedbackDAO = FeedbackDAO()

    datasetDict = feedbackDAO.selectFeedback(feedbackVO)
    return render_template("admin/viewFeedback.html", datasetDict=datasetDict)

@app.route('/view',methods=['GET'])
def view():
    feedbackVO = FeedbackVO()
    feedbackDAO = FeedbackDAO()

    feedbackVO.feedbackTo = session['loginId']
    feedbackVO.feedbackID = request.args.get('feedbackId')

    #print feedbackVO.feedbackTo
    feedbackDAO.viewFeedback(feedbackVO)

    return redirect(url_for('viewFeedback'))


@app.route('/viewFeedbackUser')
def viewFeedbackUser():
    feedbackVO = FeedbackVO()
    feedbackDAO = FeedbackDAO()
    feedbackVO.feedbackFrom = session['loginId']

    datasetDict = feedbackDAO.selectFeedbackUser(feedbackVO)
    return render_template("admin/viewFeedbackUser.html",datasetDict=datasetDict)

@app.route('/deleteFeedback',methods=['GET'])
def deleteFeedback():
    feedbackVO = FeedbackVO()
    feedbackDAO = FeedbackDAO()

    feedbackVO.feedbackID = request.args.get('feedbackId')
    feedbackDAO.deleteFeedback(feedbackVO)

    return redirect(url_for('viewFeedbackUser'))