This is graphql project that will have the following features:
- List of Users and Links
- Users creation and authentication
- Users can create Links and vote on them

## How to Run the Project
1. create a new Virtual Environment
   ```
   python3.10 -m venv venv
   ```

3. Activate environment
   ```
   source venv/bin/activate
   ```

5. Install packages
   ```
   pip install django graphene-django django-filter django-graphql-jwt
   python manage.py migrate
   python manage.py runserver
   ```

6. Run project
   ```
   pyhton3 manage.py runserver
   ```

## Example query and mutation
To use the query you can use [insomnia](https://insomnia.rest/products/insomnia) or [postman](https://www.postman.com/downloads/). This project uses token so you have to set authorization in the header to access mutation.

1. Create user
```
mutation {
    createUser(
        username:"user",
        email:"user@gmail.com",
        password:"12345678A!"
        ) {
        user {
            id
            email
            password
        }
    }
}
```
2. Login to get token
```
mutation {
    tokenAuth(
        username:"user",
        password:"12345678A!"
        ){
            token
        }
}
```

3. To get list of link
```
query {
    links {
        id
        description
        url
    }
}
```

4. To create link
```
mutation {
    createLink(
        url:"http://github.com",
        description:"My Github"
    ) {
        id
        url
        description
    }
}
```
