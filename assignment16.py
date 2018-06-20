#Basic establish a connection
import pymysql
try:
  connection = pymysql.connect(host='localhost', database='yello', user='helpme')
  print(connection)
finally:
     connection.close()
     print('Done!!')

#Create
import pymysql as pm
try:
     con = pm.connect(host='localhost', database='yello', user='helpme')
     cursor = con.cursor()
     query = 'create table Books(Book ID  int(5) primary key, Title ID int(5) foriegn key,location varchar )'
     query ='create table Titles(Title ID int(3)primary key,Title varchar,ISBN varchar,Publisher ID int(5)foreign key,Publisher year)'
     query ='create table Publisher(Publisher ID int(3)primary key,Street number int(4),Zip codes ID int(4)foriegn key)'
     query='create table Zip codes(Zip codes ID int(3)primary key,State varchar,City varchar,Zip code int(3))'
     query='create table Author Titles(Author Title ID int(4)primary key,Author Id int(3)foreign key,Title ID int(3)foreign key)'
     query='create table Authors(Author ID int(3)primary key,first name varchar,middle name varchar,Last name varchar)'

     cursor.execute(query)
     print('Table created successfully!!')
except pm.DatabaseError as e:
  if con:
    con.rollback()
    print('Problem occured: ', e)
finally:
     if cursor:
         cursor.close()
     if con:
         con.close()
     print('Done!!')

#Insert
import pymysql as pm
try:
     con = pm.connect(host='localhost', database='yello', user='helpme')
     cursor = con.cursor()
     query = "insert into Author(Author ID,first name,middle name,last name ) \
     values(%s, %s, %s, %s)"
     records = [(50,'man','preet','kaur'),
                (51,'gur','deep','singh'),
                (52,'har','deep','singh')]
     query = "insert into Zip codes(Zip codes,State,City,Zip codes) \ values(%s,%s,%s,%s)"
     records=[(23,'punjab','tanda',24),
              (42,'ludhiana','begowal',45)
              (55,'jalandhar','bogpur',78)]
     cursor.executemany(query, records)
     con.commit()
except pm.DatabaseError as e:
  if con:
     con.rollback()
     print('Problem occured: ', e)
finally:
     if cursor:
         cursor.close()
     if con:
         con.close()
     print('Done!!')

#Read
import pymysql as pm
try:
     con = pm.connect(host='localhost', database='yello', user='helpme')
     cursor = con.cursor()
     query = 'select * from Author'
     query='select *from Zip codes'
     cursor.execute(query)
     data = cursor.fetchall()
     for row in data:
         print('Auther ID: {},first name: {},middle name: {},last name : {}' \
               .format(row[0], row[1], row[2], row[3]))
     for row in data:
         print('Zip codes ID:{},State:{},City:{},Zip codes:{}' \
               .format(row[0],row[1],row[2],row[3]))
except pm.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)
finally:
     if cursor:
         cursor.close()
     if con:
         con.close()
     print('Done!!')

#Update
import pymysql as pm
try:
     con = pm.connect(host='localhost', database='yello', \
                      user='helpme')
     cursor = con.cursor()
     query = "update Author set first name='love' where Author ID = 51"
     query = "update Zip codes set State='haryana'where Zip codes ID=55"
     cursor.execute(query)
     con.commit()
except pm.DatabaseError as e:
     if con:
         con.rollback()
         print('Problem occured: ', e)
finally:
     if cursor:
         cursor.close()
     if con:
         con.close()
     print('Done!!')


