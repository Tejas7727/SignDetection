from flask import request,render_template,redirect,url_for,session
from project import app
from werkzeug.utils import secure_filename,redirect
import os
from project.com.vo.DatasetVO import DatasetVO
from project.com.dao.DatasetDAO import DatasetDAO


@app.route('/loadDataset')
def loadDataset():
    if session['loginRole']!='admin':
        return render_template('admin/auth-login.html')
    return render_template('admin/addDataset.html')


@app.route('/insertDataset', methods = ["POST"])
def insertDataset():
    if session['loginRole']!='admin':
        return render_template('admin/auth-login.html')

    datasetVO = DatasetVO()
    datasetDAO = DatasetDAO()

    UPLOAD_FOLDER = 'C:/Users/baps/PycharmProjects/signdetectoin/project/static/adminResources/dataset'

    app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
    file = request.files['datasetFile']
    description = request.form['datasetDescription']
    print(file)

    filename = secure_filename(file.filename)
    print(filename)

    filepath = os.path.join(app.config['UPLOAD_FOLDER'])
    print(filepath)

    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    datasetVO.datasetName = filename

    datasetVO.datasetPath = filepath

    datasetVO.datasetDescription= description

    datasetDAO.insertDataset(datasetVO)

    return redirect(url_for('loadDataset'))


@app.route('/viewDataset')
def viewDataset():
    if session['loginRole']!='admin':
        return render_template('admin/auth-login.html')

    datasetDAO = DatasetDAO()
    datasetDict=datasetDAO.selectDataset()

    return render_template("admin/viewDataset.html",datasetDict=datasetDict)

@app.route('/viewDatasetUser')
def viewDatasetUser():


    datasetDAO = DatasetDAO()
    datasetDict=datasetDAO.selectDataset()

    return render_template("admin/viewDatasetUser.html",datasetDict=datasetDict)


@app.route('/deleteDataset')
def deleteDataset():
    if session['loginRole']!='admin':
        return render_template('admin/auth-login.html')

    datasetVO = DatasetVO()
    datasetDAO = DatasetDAO()

    datasetVO.datasetId = request.args.get("datasetId")
    datasetDAO.deleteDataset(datasetVO)
    return redirect(url_for('viewDataset'))
