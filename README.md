# rd-users-api

### Live demo
https://rd-users-api.herokuapp.com/

### Overview
REST API

### Endpoints

1. '/', '/users'
 - a list of users in a system,
 - accessible by GET request
 - available to logged in users
2. '/users/me'
 - information about logged in user
 - accessible by GET request
 - available to logged in users
3. '/login'
 - returns a jwt token which can be used for authenticating requests
 - accessible by POST request
 - it requries user credentials (email and password) in POST data
 - available to anyone
4. '/register'
 - creates an user account in the system
 - accessible by POST request
 - it requires email, username and password to create an account
 - available to anyone

5. '/api-auth/login'
 - login functionality for session based authentication
 
6. '/api-auth/login'
 - logout functionality for session based authentication
