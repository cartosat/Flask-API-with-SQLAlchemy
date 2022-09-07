# RESTful APIs for CRUD, file upload and JWT token based Authentication using Flask and SqlAlchemy ORM
Flask_SqlAlchemy_APIs is a backend application which serve API's for basic `CRUD` operation, uploading file and JWT token based user authentication. It is built using most lightweight framework `flask` and one of popular Object Relation Mapper `SqlAlchemy`. I have used `mysql` as database in this app.

# High Level Diagram:- 
![Flask_SqlAlchemyHLD](https://user-images.githubusercontent.com/34335127/188938548-9939b8aa-eb37-46a8-bc61-2dc33aa285df.jpg)

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
6. Upload file.
7. User Authentication using `JWT` token.

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

## 6. Upload file
- This will be `POST` request and in postman under body section pass appropriate parameters as shown in below image.
- Example :- [http://127.0.0.1:5000/upload_file](http://127.0.0.1:5000/upload_file) .
- Image for reference :- ![upload_file](https://user-images.githubusercontent.com/34335127/188316322-10466154-66a4-47a2-b9c7-38f68c374726.png)

## 7. User Authentication using `JWT` token.
- In this case we will perform two operations:-
    - Getting `JWT token`.
    - View all admins list with token.
### A. Getting `JWT token`.
- This will be `POST` request and in postman under body section pass credential payload as shown in below image.
- Example :-  [http://127.0.0.1:5000/admin_login](http://127.0.0.1:5000/admin_login) .
- Image :- ![get_jwt_token](https://user-images.githubusercontent.com/34335127/188940046-6e62c82d-b79d-441f-a623-68be26ef6a14.png)
- Now you got `JWT token` by calling this endpoint.

### B. View all admins list with token.
- This will be get request, But you need to provide `Bearer token` in `Authorization` section. Which you got from above step.
- Example :-  [http://127.0.0.1:5000/all_admin](http://127.0.0.1:5000/all_admin) .
- Image :- ![all_admin_with_token](https://user-images.githubusercontent.com/34335127/188940067-1f5daa52-22d4-43b0-83d3-35e92dd1de2c.png)
- You will get JSON data of all admin, if everything goes well.
 

# How to start Backend server
- Clone Repo [https://github.com/cartosat/Flask_SqlAlchemy_APIs](https://github.com/cartosat/Flask_SqlAlchemy_APIs).
- Database Setup :-
  - Install [MySQL Community (GPL)](https://www.mysql.com/downloads/) version for mysql database.
  - execute `virtual_studio.sql` to automatically create database.
- Postman Setup :-
  - Install [PostMan](https://www.postman.com/downloads/).
  - Import `AppBackend.postman_collection,json` collection.
- Python Setup :-
  - Install [Python](https://www.python.org/downloads/).
  - Install `requirement.txt` with `pip install -r requirement.txt`.
- Call API's using postman.
