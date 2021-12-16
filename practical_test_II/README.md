# API service and report interface

This is a test requested by the company Triduum for the development of an API to present a report acording to the wikipedia API searches.

Project carried out using Django, rest framework and the MySQL database engine.

## How to Run

To run it make sure of the following:

* Clone this repository
* Activate your virtual enviroment
* Install the packages contents in the
 ```requierments.txt``` file
* Run the sql script ```mysql_setup.sql``` to create the database and make sure you have a user with access to it
* Finally, perform the migrations through ```manage.py```

Once you have the server running you should see something like this

```
System check identified no issues (0 silenced).
December 15, 2021 - 19:27:01
Django version 4.0, using settings 'tbl_search_db.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C
```

## About the Service

The service is just a simple Searches REST service. It uses a mySQL database to store the data.  If your database connection properties work, you can call some REST endpoints through localhost on **port 8000**.

Here is the endpoint you can call:

```
http://localhost:8000/api/v1/
```

### Get all searches

```
GET
http://localhost:8000/search
Response: HTTP 200 (OK)
```
Response:
```
[
    {
        "id": "a44f7ad8-7059-4472-ba41-2cc5d3fd4e16",
        "keyword": "Avocado",
        "created_at": "2021-12-15T17:40:52.421949-05:00",
        "results": 10
    },
    {
        "id": "50f5bcc5-8362-409d-8994-f2c3e276c339",
        "keyword": "AWS",
        "created_at": "2021-12-15T17:41:04.652308-05:00",
        "results": 10
    },
    {
        "id": "72e1df40-cbce-43b9-b71a-2abb65ed5bd3",
        "keyword": "Avocado",
        "created_at": "2021-12-15T17:41:17.521629-05:00",
        "results": 10
    }
]
```

### Create a search

```
POST
http://localhost:8080/search/inform
Response: HTTP 201 (Created)
```
Request:
```
{
    "keyword": "Javascript",
    "results": 10
}
```
### Get a search report

```
GET
http://localhost:8080/search/info
Response: HTTP 200 (OK)
```
Respose:
```
[
    {
        "item": 0,
        "keyword": "Avocado",
        "search_number": 3,
        "last_date": "Wed Dec 15 22:41:41 2021",
        "first_date": "Wed Dec 15 22:40:52 2021",
        "results": 10
    },
    {
        "item": 1,
        "keyword": "Javascript",
        "search_number": 2,
        "last_date": "Wed Dec 15 22:41:52 2021",
        "first_date": "Wed Dec 15 22:41:28 2021",
        "results": 10
    },
    {
        "item": 2,
        "keyword": "AWS",
        "search_number": 1,
        "last_date": "Wed Dec 15 22:41:04 2021",
        "first_date": "Wed Dec 15 22:41:04 2021",
        "results": 10
    }
]
```


# Questions and Comments: mateolondono.u@gmail.com
