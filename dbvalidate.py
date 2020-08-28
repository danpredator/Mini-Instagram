import mysql.connector
from mysql.connector import Error

hostt = 'localhost'
dbname = 'insta'
admintorname = 'root'
passwordu = 'mysqlpassword'
def logvalidate(username,password):
    try:
        conn = mysql.connector.connect(host=hostt,
                                         database=dbname,
                                         user=admintorname,
                                         password=passwordu)

        cursor = conn.cursor()
        #print(username,password)
        msql = ("SELECT user_id,pass FROM USERS where user_id=%s")

        cursor.execute(msql,(username,))
        
        return cursor.fetchone()

        #print("You're connected to database: ", record)
        
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (conn.is_connected()):
            cursor.close()
            conn.close()
            
def newsignup(user_id,passz,fullname,dp_url,bio):
    try:
        conn = mysql.connector.connect(host=hostt,
                                         database=dbname,
                                         user=admintorname,
                                         password=passwordu)

        cursor = conn.cursor()
        sql = ("SELECT user_id FROM USERS where user_id='%s'")

        cursor.execute(sql,user_id)
        if(cursor.fetchone() is None):
            sql = ("INSERT INTO users VALUES(%s,%s,%s,%s,%s)")
            cursor.execute(sql,(user_id,passz,fullname,dp_url,bio))
            conn.commit()
            return True

        return False

        #print("You're connected to database: ", record)
        
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (conn.is_connected()):
            cursor.close()
            conn.close()

def profile(user_id):
    try:
        conn = mysql.connector.connect(host=hostt,
                                         database=dbname,
                                         user=admintorname,
                                         password=passwordu)
        cursor = conn.cursor()
        sql1 = ("SELECT user_id,fullname,dp_url,bio FROM USERS where user_id = %s")
        sql2 = ("select count(*) from followers where user_id = %s")
        sql3 = ("select count(*) from following where user_id = %s")
        sql4 = ("select photo_id,image_url from photos natural join photo_of where user_id = %s")
        sql5 = ("select user_id, count(*) from photo_of group by user_id having user_id = %s")


        cursor.execute(sql1,(user_id,))
        r1 = cursor.fetchone()
        cursor.execute(sql2,(user_id,))
        r2 = cursor.fetchone()
        cursor.execute(sql3,(user_id,))
        r3 = cursor.fetchone()
        cursor.execute(sql4,(user_id,))
        r4 = cursor.fetchall()
        cursor.execute(sql5,(user_id,))
        r5 = cursor.fetchall()
        #print(r4)
        return r1,r2,r3,r4,r5

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (conn.is_connected()):
            cursor.close()
            conn.close()


def uploadpic(user_id,image_url,caption):
    try:
        conn = mysql.connector.connect(host=hostt,
                                         database=dbname,
                                         user=admintorname,
                                         password=passwordu)

        cursor = conn.cursor()
        sql1 = ("insert into photos(image_url,caption) values(%s,%s)")
        sql2 = ("call storefor_p(%s);")
        cursor.execute(sql1,(image_url,caption))
        cursor.execute(sql2,(user_id,))
        conn.commit()
        return True


    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (conn.is_connected()):
            cursor.close()
            conn.close()

def searchck(user_id):
    try:
        conn = mysql.connector.connect(host=hostt,
                                         database=dbname,
                                         user=admintorname,
                                         password=passwordu)

        cursor = conn.cursor()
        sql1 = ("SELECT user_id FROM USERS where user_id = %s")
        cursor.execute(sql1,(user_id,))
        if( cursor.fetchone() is None ):
            return False
        else:
            return True
            


    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (conn.is_connected()):
            cursor.close()
            conn.close()


def followingotp(user_id,following_id):
    try:
        conn = mysql.connector.connect(host=hostt,
                                         database=dbname,
                                         user=admintorname,
                                         password=passwordu)

        cursor = conn.cursor()
        sql1 = ("insert into following values(%s,%s);")
        sql2 = ("call followerupdate(%s,%s);")
        cursor.execute(sql1,(user_id,following_id))
        cursor.execute(sql2,(following_id,user_id))
        conn.commit()
        
        sql3 = ("select count(*) from followers where user_id = %s")
        
        cursor.execute(sql3,(following_id,))
        r1 = cursor.fetchone()
        # cursor.execute(sql4,(user_id,))
        # r2 = cursor.fetchone()
        return r1

    except Error as e:
        #print("Error while connecting to MySQL1", str(e))
        
        try:

            if('Duplicate entry' in str(e)):
                sql1 = ("delete from following where user_id = %s and following_id = %s;")
                
                sql2 = ("call followerdelete(%s,%s);")
                cursor.execute(sql1,(user_id,following_id))
                cursor.execute(sql2,(following_id,user_id))
                conn.commit()

                sql4 = ("select count(*) from followers where user_id = %s;")
                cursor.execute(sql4,(following_id,))
                r2 = cursor.fetchone()
                return r2
        except Error as e:
            print("Error while connecting to MySQL2", str(e))


    finally:
        if (conn.is_connected()):
            cursor.close()
            conn.close()


def newsfeed(user_id):
    try:
        conn = mysql.connector.connect(host=hostt,
                                         database=dbname,
                                         user=admintorname,
                                         password=passwordu)

        cursor = conn.cursor()
        sql1 = ('''select photo_id,image_url
                    from photos natural join photo_of
                    where user_id in ( select following_id
                    from following
                    where user_id = %s
                    );''')
        cursor.execute(sql1,(user_id,))
        return cursor.fetchall()

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (conn.is_connected()):
            cursor.close()
            conn.close()


def captlike(user_id,pic_id,flag=False):
    try:
        conn = mysql.connector.connect(host=hostt,
                                         database=dbname,
                                         user=admintorname,
                                         password=passwordu)

        cursor = conn.cursor()
        if(flag):
            sql1 = ("insert into likes values(%s,%s);")
            cursor.execute(sql1,(pic_id,user_id))
            conn.commit()
            sql2 = ("select count(*) from likes where photo_id = %s;")
            cursor.execute(sql2,(pic_id,))
            return cursor.fetchone()

        else:
            sql1 = ("select user_id from photo_of where photo_id = %s;")
            sql2 = ("select count(*) from likes where photo_id = %s;")
            sql3 = ("select caption from photos where photo_id = %s;")

            cursor.execute(sql1,(pic_id,))
            r1 = cursor.fetchone()
            cursor.execute(sql2,(pic_id,))
            r2 = cursor.fetchone()
            cursor.execute(sql3,(pic_id,))
            r3 = cursor.fetchone()

            return r1,r2,r3

    except Error as e:
        #print("Error while connecting to MySQL", e)
        if('Duplicate entry' in str(e)):
            
            sql1 = ("delete from likes where photo_id = %s and liker_id = %s ;")
            cursor.execute(sql1,(pic_id,user_id))
            conn.commit()
            
            sql2 = ("select count(*) from likes where photo_id = %s;")
            cursor.execute(sql2,(pic_id,))
        
            return cursor.fetchone()
            
        #print("Error while connecting to MySQL", e)
    finally:
        if (conn.is_connected()):
            cursor.close()
            conn.close()


def getliker(user_id):
    try:
        conn = mysql.connector.connect(host=hostt,
                                         database=dbname,
                                         user=admintorname,
                                         password=passwordu)

        cursor = conn.cursor()

        sql1 = ('''select fullname,substring_index(image_url , '/' , -1) as  imgg 
                    from (users join likes on user_id = liker_id) natural join photos
                    where photo_id in 
                    ( select photo_id from
                    photos natural join photo_of
                    where user_id = %s );''')

        cursor.execute(sql1,(user_id,))
        return cursor.fetchall() 

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (conn.is_connected()):
            cursor.close()
            conn.close()


def getallpics():
    try:
        conn = mysql.connector.connect(host=hostt,
                                         database=dbname,
                                         user=admintorname,
                                         password=passwordu)

        cursor = conn.cursor()
        sql1 = ("select photo_id,image_url from photos")
        cursor.execute(sql1)
        return cursor.fetchall()

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (conn.is_connected()):
            cursor.close()
            conn.close()


def deactivateuser(user_id):
    try:
        conn = mysql.connector.connect(host=hostt,
                                         database=dbname,
                                         user=admintorname,
                                         password=passwordu)

        cursor = conn.cursor()
        sql1 = ("delete from users where user_id = %s;")
        cursor.execute(sql1,(user_id,))
        conn.commit()
        
        
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (conn.is_connected()):
            cursor.close()
            conn.close()



if __name__ == "__main__":
    pass
    #followingotp("hoii","ramzzz")
    #print(profile("nawazuddin._siddiqui"))
    