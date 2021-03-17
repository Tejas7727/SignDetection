from project.com.dao import condb

class RegisterDAO:
    def insertRegister(self,registerVO):


                connection = condb()

                cursor1 = connection.cursor()

                cursor1.execute(
                        "INSERT INTO registermaster(registerFirstName, registerLastName, registerContact, registerAddress, register_loginId) VALUES ('{}','{}','{}','{}','{}')".format(
                            registerVO.registerFirstName,registerVO.registerLastName,registerVO.registerContact,registerVO.registerAddress,registerVO.register_loginId))

                connection.commit()

                cursor1.close()

                connection.close()

    def getmaxId(self):
        connection = condb()

        cursor1 = connection.cursor()

        cursor1.execute(
            "SELECT  MAX(loginId) FROM loginmaster ")

        a = cursor1.fetchall()

        cursor1.close()

        connection.close()

        return a

    def selectUser(self):
        connection = condb()

        cursor1 = connection.cursor()

        cursor1.execute(
            "SELECT  registermaster.*,loginmaster.loginId, loginmaster.loginEmail, loginmaster.loginActiveStatus, loginmaster.loginRole FROM registermaster INNER JOIN loginmaster on registermaster.register_loginId = loginmaster.loginId WHERE loginmaster.loginActiveStatus='active' AND loginmaster.loginRole = 'user'")

        a = cursor1.fetchall()

        cursor1.close()

        connection.close()

        return a

    def deleteUser(self, registerVO):
        connection = condb()

        cursor1 = connection.cursor()

        cursor1.execute(
            "UPDATE loginmaster SET loginActiveStatus = 'deactive' WHERE loginId = '" + registerVO.register_loginId + "'")

        connection.commit()

        cursor1.close()

        connection.close()
