
import xml.etree.ElementTree as parse
import sqlite3

#this will creat a new database called pythonxml.db
connection = sqlite3.connect("pythonxml.db")
# this command will allow us to execute sql commands line 
cursor = connection.cursor()


#if we run this code it will creat a table in SQLITE 
"""
cursor.execute("CREATE TABLE xmlfile (author nvarchar(30), title nvarchar(30), genre nvarchar(30), price int, publish_date date, description nvarchar(128) )")
"""

root = parse.parse('samplexml.xml')
doc = root.getroot()

#this loop will bring every row in the xml file but sorted 
for c in root.iterfind('book'):

    author = c.find('author').text
    title = c.find('title').text
    genre = c.find('genre').text
    price = c.find('price').text
    publish_date = c.find('publish_date').text
    description = c.find('description').text
    #this command below shows the data in the xml file and brings it sorted 
    """
    print(' * {}  ({}) {} [{}] [{}] "{}" '.format(
       author, title, genre, price, publish_date, description
    ))
    """
    
    #this comant in line 37 will insert the data of the xml file into certin columns that we created before
    """
    cursor.execute( "INSERT INTO xmlfile (author, title, genre, price, publish_date, description ) VALUES (?, ?, ?, ?, ?, ?)",
                   (author,title,genre,price,publish_date,description))
    """
    
#this will retreive all the data from the table "xmlfile" sorted
cursor.execute("SELECT * FROM xmlfile") 
print("fetchall:")
result = cursor.fetchall() 
for r in result:
    print("\n",r,"\n")
   
# this command will save all the work
connection.commit()

