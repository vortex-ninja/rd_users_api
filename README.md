# rd-users-api

### LIVE DEMO
https://rd-users-api.herokuapp.com/

### OVERVIEW
Basic REST API that manages users in a django web application.

### AUTHENTICATION
API uses JWT token authentication and session based authentication.
I've added session authentication so it's easy to access protected endpoints from web browser.

### ENDPOINTS

1. `/`, `/users`
 - returns a list of users in a system,
 - accessible by GET request,
 - available to logged in users.
2. `/users/me`
 - returns information about logged in user
 - accessible by GET request
 - available to logged in users
3. `/login`
 - returns a jwt token which can be used for authenticating requests,
 - accessible by POST request,
 - it requries user credentials (email and password) in POST data,
 - available to anyone.
4. `/register`
 - creates an user account in the system,
 - accessible by POST request,
 - it requires email, username in POST data,
 - available to anyone.
5. `/api-auth/login`
 - login functionality for session based authentication
6. `/api-auth/logout`
 - logout functionality for session based authentication


### HOW TO USE

API is available through browser for easy use by humans.
It can be also accessed programatically by sending requests to the specified endpoints with tools like CURL, Postman or httpie.

### EXAMPLE USING CURL

So let's say we would like to see a list of all users registered in the system.
First we need to create an account. To do that we send a POST request to the `/register` endpoint with required data (username, email and password).

##### CREATING AN ACCOUNT

`curl -X POST -H "Content-Type: application/json" -d '{"username":"test","email":"test@test.pl","password":"password"}' https://rd-users-api.herokuapp.com/register/`

This will create an account and return a jwt token which we can use to get the list.
But let's say we went away to get a cup of coffee. Five minutes passed (that's the lifespan of the tokens) and token expired.

To get a new token we can use credentials of the account we just created.
We're going to send a POST request to `/login` endpoint with email and password.

##### GETTING A TOKEN

`curl -X POST -H "Content-Type: application/json" -d '{"email":"test@test.pl","password":"password"}' https://rd-users-api.herokuapp.com/login/`

With the token ready we can now get the list of users. We send an authenticated GET request to endpoint `/login`.
To authenticate the request we add a header `Authorization: JWT <jwt token we received>`.

##### ACCESSING A PROTECTED RESOURCE

`curl -H "Authorization: JWT <jwt-token>" https://rd-users-api.herokuapp.com/users/`

That's it. We got our list now.
