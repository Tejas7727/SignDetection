from project.com.vo.ComplaintVO import ComplaintVO
from project.com.dao import condb


class ComplaintDAO:
    def insertComplaint(self,complaintVO):

            connection = condb()

            cursor1 = connection.cursor()

            cursor1.execute("INSERT INTO complaintmaster(complaintSubject, complaintDescription, complaintDate, complaintTime, complaintStatus, complaintActiveStatus, complaintFrom) VALUES('{}','{}','{}','{}','{}','{}','{}')".format(
                complaintVO.complaintSubject,complaintVO.complaintDescription, complaintVO.complaintDate, complaintVO.complaintTime,complaintVO.complaintStatus, complaintVO.complaintActiveStatus, complaintVO.complaintFrom))

            connection.commit()

            cursor1.close()

            connection.close()

    def selectComplaintUser(self,complaintVO):

            connection = condb()
            cursor1 = connection.cursor()

            cursor1.execute("SELECT *,loginEmail FROM complaintmaster INNER JOIN loginmaster ON complaintmaster.complaintTo = loginmaster.loginId WHERE complaintActiveStatus = 'active' AND complaintFrom = '"+str(complaintVO.complaintFrom)+"'" )

            a=cursor1.fetchall()

            cursor1.close()

            connection.close()

            return a

    def selectComplaint(self,complaintVO):

            connection = condb()
            cursor1 = connection.cursor()

            cursor1.execute("SELECT *,loginEmail FROM complaintmaster INNER JOIN loginmaster ON complaintmaster.complaintFrom = loginmaster.loginId WHERE complaintActiveStatus = 'active' AND complaintStatus = 'pending'")

            a=cursor1.fetchall()

            cursor1.close()

            connection.close()

            return a

    def selectComplaintReply(self,complaintVO):

            connection = condb()
            cursor1 = connection.cursor()

            cursor1.execute("SELECT * FROM complaintmaster WHERE complaintActiveStatus = 'active' AND complaintStatus = 'pending' AND complaintId = '"+complaintVO.complaintId+"'")

            a=cursor1.fetchall()

            cursor1.close()

            connection.close()

            return a

    def deleteComplaint(self,complaintVO):

            connection = condb()

            cursor1 = connection.cursor()

            cursor1.execute("UPDATE complaintmaster SET complaintActiveStatus = 'deactive' WHERE complaintId = '"+complaintVO.complaintId+"'")

            connection.commit()

            cursor1.close()

            connection.close()

    def replyComplaint(self,complaintVO):

            connection = condb()

            cursor1 = connection.cursor()

            cursor1.execute(
                    "UPDATE complaintmaster SET complaintStatus = '"+complaintVO.complaintStatus+"', complaintTo = '"+str(complaintVO.complaintTo)+"', complaintReply = '"+complaintVO.complaintReply+"' WHERE complaintId = '"+ complaintVO.complaintId +"'")

            connection.commit()

            cursor1.close()

            connection.close()