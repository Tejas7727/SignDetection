from project.com.dao import condb

class FeedbackDAO:
    def insertFeedback(self,feedbackVO):
        connection = condb()

        cursor1 = connection.cursor()

        cursor1.execute(
            "INSERT INTO feedbackmaster(feedbackRating, feedbackDescription, feedbackDate, feedbackTime, feedbackActiveStatus, feedbackFrom) VALUES('{}','{}','{}','{}','{}','{}')".format(feedbackVO.feedbackRating, feedbackVO.feedbackDescription, feedbackVO.feedbackDate, feedbackVO.feedbackTime, feedbackVO.feedbackActiveStatus, feedbackVO.feedbackFrom))

        connection.commit()

        cursor1.close()

        connection.close()

    def selectFeedbackUser(self,feedbackVO):

            connection = condb()
            cursor1 = connection.cursor()

            cursor1.execute("SELECT *,loginEmail FROM feedbackmaster INNER JOIN loginmaster ON feedbackmaster.feedbackTo = loginmaster.loginId  WHERE feedbackActiveStatus = 'active' AND feedbackFrom = '"+str(feedbackVO.feedbackFrom)+"'")

            a=cursor1.fetchall()

            cursor1.close()

            connection.close()

            return a

    def selectFeedback(self,feedbackVO):

            connection = condb()
            cursor1 = connection.cursor()

            cursor1.execute("SELECT *, loginEmail FROM feedbackmaster INNER JOIN loginmaster ON feedbackmaster.feedbackFrom = loginmaster.loginId WHERE feedbackActiveStatus = 'active'" )

            a=cursor1.fetchall()

            cursor1.close()

            connection.close()

            return a

    def deleteFeedback(self,feedbackVO):

            connection = condb()

            cursor1 = connection.cursor()

            cursor1.execute("UPDATE feedbackmaster SET feedbackActiveStatus = 'deactive' WHERE feedbackId = '"+feedbackVO.feedbackID+"'")

            connection.commit()

            cursor1.close()

            connection.close()

    def viewFeedback(self,feedbackVO):

            connection = condb()

            cursor1 = connection.cursor()

            cursor1.execute("UPDATE feedbackmaster SET feedbackTo = '"+str(feedbackVO.feedbackTo)+"' WHERE feedbackId = '"+feedbackVO.feedbackID+"'")

            connection.commit()

            cursor1.close()

            connection.close()