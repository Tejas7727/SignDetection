
from project.com.dao import condb

class LoginDAO:

        def insertLogin(self,loginVO):
                connection = condb()

                cursor1 = connection.cursor()

                cursor1.execute(
                        "INSERT INTO loginmaster(loginEmail, loginPassword, loginRole) VALUES('{}','{}','{}')".format(loginVO.loginEmail,loginVO.loginPassword,loginVO.loginRole))

                connection.commit()

                cursor1.close()

                connection.close()



        def searchLogin(self,loginVO):

                    connection = condb()

                    cursor1 = connection.cursor()

                    cursor1.execute("SELECT  * FROM loginmaster WHERE loginEmail = '"+ loginVO.loginEmail +"'")

                    a=cursor1.fetchall()

                    cursor1.close()

                    connection.close()

                    return a