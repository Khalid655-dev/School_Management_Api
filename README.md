# School Management RESTful Application

### Scenario
Let’s suppose a School needs an API for their management like Teacher Registration , student registration alongwith other esstentials and will be done by admin. First, the admin will sign up and then Log in to the API, Will create account for student, teacher and will provide the credentials to the Teacher like username (email) and Password. The teacher will use these credentials and will be Logged in. Now the teacher can create the result of a registered student. The Student can view his result of the specific subject.

- Table of Content
[ToC]

### Requirements

#### Functional Requirements
Following are the functions which the application will be able to perform.
* **Admin signup /signin**
Admin shall be able to sign up with his/her credentials for the first time and then can login to use the app features. The admin shall registerd a Teacher by providing his detalis like name, email, password, joining date and specialization
* **Student crud operations**
Admin shall be able to create student , read (Get) all students or one student by providing specific id, Update Student and Delete student.
* **result crud operations**
Teacher shall be able to create result , read (Get) all students result or one student result by providing specific id of the student, Update Student result and Delete student result.


#### Non-functional Requirements
Following are the non-functional requirements;
* **Security**
Admin and Teacher passwords will be encrypted before storing in the database which cannot be understood if retrieved the data from database.
* **Performance**
The application should perform well and provide responsive messages on each operation.

### Detail Design and Architecture
The application include MySQL database.
* **Entity Relationship Digram**
An Admin can add multiple Teachers. But an added Teacher has must one-to-one relation with Admin. Similarly, An Admin can add multiple students. But an added student has must one-to-one relation with Admin.
The Teacher can add multiple results of student. But an added reslut has must one-to-one relation with Teacher.
![School Management ER-Diagram](https://i.imgur.com/kODFqsp.png)

### Implementation
A good framworks help to  develop quality products faster. Developers enjoy and get good development experience using frameworks. FastAPI is modern Python based web framework with high speed compare to Node.js and Go. It has detailed and friendly developer docs. The School Management project includes the following concepts.
* **Model**
Model is used for modelling the application data. It mirrors a database table. An object of these model class is used to send or retrieve data from database with Object Relational Mapper(ORM) tool like SQLALchemy. ORM tool used to translate Python classes into relational database tables and concert function calls to SQL queries.

* **OAuth2 and JSON Web Tokens(JWT)**
JSON Web TOken (JWT) is a token format and OAuth2 is an authorization protocol which can use JWT as a token. OAuth uses client-side and server-side storage. Thus a built-in OAuth2 support in FastAPI for a JSON Web Tokens (JWT) is used for creating a token based login endpoint. Further a 30 minute session is created for a Admin to live and use the School Management application features.

* **Password Hashing**
To secure user password, hashing function is created to encode the password before storing in the database. A password verifier function is used to compare the plain-password with the hashed-password while logging-in. A passlib library and bcrypt package is used to achieve hashing. To provide unicode support passlib is used to encode unicode passwords using utf-8 before running them through bcrypt.

* **Functional Operations**
Different operational functions are created for each operation like login, signup and get_admin, get_result etc with specific well defined routes. Further FastAPI is used which is accessed thorugh REST API to call different routing functions of the application. Further APIRouter is used to organize the path operations related to a specific model like User and Item in our application. APIROuter is also called mini FastAPI and support all the same parameters, responses, dependencies and tags etc.

* **System Specifiction**
The project work is performed on personal system with the following specifications:
    * Intel Core i5-4200U
    * 1.6GHz clock-speed
    * 8 GB RAM
    * Ubuntu 20.04 OS

### Testing
Testing and evaluation of the software system is the most crucial part of the software development life cycle as this phase certifies that either the system is ready to be rolled out to production or it needs some improvements. The testing phase adds value to the software and hence should be carried out with due care. It is a comparison between the expected result to the real results.

During testing of the School Management application, one technique is used FastAPI automatic documentation (provided by Swagger UI) for playing with builted endpoints and Tableplus to check database tables and its instances.
The testing results of the endpoints are given below;

* **Admin Signup/Create Admin**
To register the admin in the School Management application. One need to enter the required data. AdminSignUp schema is used to provide the fields structure.
![](https://i.imgur.com/ZDl7mse.png)

   The admin is successfully created and assured through tableplus to check the registered AdminSignUp data.
![]![](https://i.imgur.com/9mPnwqV.png)

* **Admin Login**
To use the student crud operations and creating Teacher, Admin need to be registered and login. The login API is tested for token generation using builtin SwaggerUI tool.The Token will be vaild for 30 minutes
![](https://i.imgur.com/jBcsWR5.png)

* **Create Student**
To post a student in the application admin need to login into the system.
![](https://i.imgur.com/9r85KG1.png)

  Add details of the student as following: 
![](https://i.imgur.com/evGVs8A.png)

  Here is the successful insertion of the student into the database of the application.
![](https://i.imgur.com/t0XmHEJ.png)

All other functionality of the School Management application can be used accordingly and you will get the desired results.


### School Management application environment setup

#### **Step-1** Cloning repository

```
# clone porject
git clone https://github.com/Khalid655-dev/School_Management_Api.git

#change directory
cd School_Management_Api/
```
#### **Step-2** Python-vitual environment and dependencies installation

```
# create venv python-virtual environment
python3 -m venv venv

# to install the required packages
pip install -r requirements
```

#### **Step-3** Activate python-virtual environment (venv)
```
# activate venv
source venv/bin/activate
```

#### **Step-4**Run the application
```

#run the application
uvicorn main:app --reload

```
Copy the url and paste in the browser with a docs or redoc route like:
[localhost:8000/docs](localhost:8000/docs)
or
[localhost:8000/docs](localhost:8000/redoc)


Congratulations! :partying_face:
