# APIs for CRUD operation using Flask and SqlAlchemy ORM
Flask_SqlAlchemy_APIs is a backend application which serve API's for basic `CRUD` operation. It is built using most lightweight framework `flask` and one of popular Object Relation 
Mapper `SqlAlchemy`. I have used `mysql` as database in this app.

# High Level Diagram:- 
![HLD](https://user-images.githubusercontent.com/34335127/188273605-6274ea28-42cb-4dd9-842d-7e4f052e297e.jpg)

# Technology Stack
- Python
- Flask
- SqlAlchemy
- Postman

## We have APIs for :-
1. Add Admin.
2. Get information for all Admins in database.
3. Get information for admin with specific id.
4. Update Admin Information.
5. Delete Admin from Database.

## Application logs for all 5 operations :-
![App Log](https://user-images.githubusercontent.com/34335127/188273685-66e3f06f-5593-40e2-892d-abed2a280e26.png)

# Screenshots of Postman tool:- 
## 1) Add Admin :-
- We need to send `POST` request through postman and provide payload in Body section.
```javascript
{
    "email": "sakangupt@gmail.com",
    "phone": " 7788990011",
    "full_name": "Sakshi Gupta",
    "password" : "Pass@123",
    "role": "Admin",
    "status": "Active"
}
```
- Image :- ![add_Admin](https://user-images.githubusercontent.com/34335127/188273776-8d3ce3e3-c0a0-4802-92b5-df1d3e66c433.png)

## 2) Get information for all Admins in database.
- We simply need to call [http://127.0.0.1:5000/all_admin/](http://127.0.0.1:5000/all_admin/) this endpoint with `GET` request to get JSON data.
- Image for reference :- ![All_Admins](https://user-images.githubusercontent.com/34335127/188273797-f6d93065-3648-4b2a-83b3-c008158757c9.png)

## 3. Get information for admin with specific id.
- We need to pass `id` at end of URL with `PUT` request.
- Example :- [http://127.0.0.1:5000/admin/101](http://127.0.0.1:5000/admin/101) . Here `101` is `id` of `Super Admin`.
- Image for reference :- ![Admin_with_id](https://user-images.githubusercontent.com/34335127/188273784-a4621391-443e-4d61-8f0c-7c93bbfab7b4.png)

## 4. Update Admin Information.
- We need to pass `id` at end of URL and payload along with `PUT` request.
- Example :- [http://127.0.0.1:5000/admin/104](http://127.0.0.1:5000/admin/104) .
- Payload will be :- 
```javascript
{
    "full_name": "Swaraj Gore",
    "email": "swarajgo@gmail.com",
    "password" : "Pass@1234",
    "phone": "49857243857",
    "role": "Admin",
    "status": "Active"
}
```
- Image for reference :- ![update_admin](https://user-images.githubusercontent.com/34335127/188274556-f4a35308-9146-4495-ac3c-344418ca5bde.png)

## 5. Delete Admin from Database.
- We need to pass `id` at end of URL `DELETE` request.
- Example :- [http://127.0.0.1:5000/admin/3](http://127.0.0.1:5000/admin/3) .
- Image for reference :- ![delete_admin](https://user-images.githubusercontent.com/34335127/188273806-de04b435-031f-4035-9499-de90d77e6cd1.png)

# How to start Backend server
- Clone Repo [https://github.com/cartosat/Flask_SqlAlchemy_APIs](https://github.com/cartosat/Flask_SqlAlchemy_APIs).
- Database Setup :-
  - Install [MySQL Community (GPL)](https://www.mysql.com/downloads/) version for mysql database.
  - execute `virtual_studio.sql` to automatically create database.
- Postman Setuo :-
  - Install [PostMan](https://www.postman.com/downloads/).
  - Import `AppBackend.postman_collection,json` collection.
- Python Setup :-
  - Install [Python](https://www.python.org/downloads/).
  - Install `requirement.txt` with `pip install -r requirement.txt`.
- Call API's using postman.
