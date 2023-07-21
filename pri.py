import mysql.connector
import streamlit as st
# Esatablish a connection to Mysql on server
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="curd"
)
mycursor=mydb.cursor()
print("Connection Established")

# Create Streamlit app
def main():
    st.title("CRUD Operations with Mysql")
    # Dispaly Options for CRUD Operations
    option=st.sidebar.selectbox("Select an Operations",("Create","Read","Update","Delete"))
    if option=="Create":
        st.subheader("Create a record")
        name=st.text_input("Enter Name")
        email=st.text_input("Enter Email")
        if st.button("Create"):
            sql="insert into user(name,email) values(%s,%s)"
            val=(name,email)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record Created Successfully")
    elif option=="Read":
        st.subheader("Read Records")
        mycursor.execute("select * from user")
        result=mycursor.fetchall()
        for row in result:
            st.write(row)
    elif option=="Update":
        st.subheader("Update a record")
        id=st.number_input("Enter ID",min_value=1)
        name=st.text_input("Enter New Name")
        email=st.text_input("Enter New Emails")
        if st.button("Update"):
            sql="update user set name=%s, email=%s where id =%s"
            val=(name,email,id)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record Updated Successfully!!!")

    elif option=="Delete":
        st.subheader("Delete a Record")
        id=st.number_input("Enter ID",min_value=1)
        if st.button("Delete"):
            sql="delete from user where id =%s"
            val=(id,)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record Deleted Successfully!!!")

if __name__=="__main__":
    main()