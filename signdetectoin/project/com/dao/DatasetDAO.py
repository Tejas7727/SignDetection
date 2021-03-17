from project.com.vo import DatasetVO
from project.com.dao import condb
datasetVO = DatasetVO
class DatasetDAO:
    def insertDataset(self,datasetVO):

            connection = condb()

            cursor1 = connection.cursor()

            cursor1.execute("INSERT INTO datasetmaster(datasetName,datasetPath, datasetDescription) VALUES('{}','{}','{}')".format(
                datasetVO.datasetName,datasetVO.datasetPath, datasetVO.datasetDescription))

            connection.commit()

            cursor1.close()

            connection.close()
    def selectDataset(self):

            connection = condb()

            cursor1 = connection.cursor()

            cursor1.execute("SELECT  * FROM datasetmaster WHERE datasetActiveStatus = 'active'")

            a=cursor1.fetchall()

            cursor1.close()

            connection.close()

            return a

    def deleteDataset(self,datasetVO):

            connection = condb()

            cursor1 = connection.cursor()

            cursor1.execute("UPDATE datasetmaster SET datasetACtiveStatus = 'deactive' WHERE datasetId = '"+datasetVO.datasetId+"'")

            connection.commit()

            cursor1.close()

            connection.close()

