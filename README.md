<h1 align="center">
  <br>
  <a href="http://www.amitmerchant.com/electron-markdownify"><img src="https://imgur.com/4yYkmW8.png" alt="Ogma app logo" width="200"></a>
  <br>
  Ogma App Backend
  <br>
</h1>

## Summary
This project delivers and API that includes a CRUD type service for users for our app.
 
## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) and [Python 3](https://www.python.org/) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/OgmaCapStone/Backend.git

# Go into the repository
$ cd backend

# Create virtual enviroment
$ python -m venv .env

# Enter the virtual enviroment
$ source .env/bin/activate

# Install dependencies
$ pip install -r requirements.txt

# Don't forget to set up your own .env file

# Run the app
$ uvicorn app.main:app
```

## Credits

This software uses :

- [FastAPI](https://fastapi.tiangolo.com/)
- [Hosted in Heroku](https://id.heroku.com/login)

With the supervision of [Erik Ochoa](https://twitter.com/Elyager), Academic Coach at [Platzi Master](https://platzi.com/master/)

## Collaborators

This app was created with 💚 by:

> Elsa Portilla &nbsp;&middot;&nbsp;
> Frontend Developer &nbsp;&middot;&nbsp;
> LinkedIn [@elsaportilla](https://www.linkedin.com/in/elsaportilla/) &nbsp;&middot;&nbsp;
> GitHub [@elsargentpepper](https://github.com/elsargentpepper) &nbsp;&middot;&nbsp;

> Jorge Delgadillo &nbsp;&middot;&nbsp;
> Backend Developer ([backend repo](https://github.com/OgmaCapStone/Backend)) &nbsp;&middot;&nbsp;
> LinkedIn [@jorge-alberto-delgadillo-alonso-7b58501aa](https://www.linkedin.com/in/jorge-alberto-delgadillo-alonso-7b58501aa/) &nbsp;&middot;&nbsp;
> GitHub [@49122](https://github.com/49122) &nbsp;&middot;&nbsp;

> Juan Camilo Garcés &nbsp;&middot;&nbsp;
> Frontend Developer &nbsp;&middot;&nbsp;
> LinkedIn [@juancamilogarcesviveros](https://www.linkedin.com/in/juancamilogarcesviveros/) &nbsp;&middot;&nbsp;
> GitHub [@camilogarcesv](https://github.com/camilogarcesv) &nbsp;&middot;&nbsp;
> Twitter [@Camilo_GarcesV](https://twitter.com/Camilo_GarcesV) &nbsp;&middot;&nbsp;

> Juan Daniel Martínez &nbsp;&middot;&nbsp;
> Frontend Developer &nbsp;&middot;&nbsp;
> [juanda.dev](https://juanda.dev) &nbsp;&middot;&nbsp;
> GitHub [@juandadev](https://github.com/juandadev) &nbsp;&middot;&nbsp;
> Twitter [@juanda_dev_](https://twitter.com/juanda_dev_)

> Sebastián Ballen &nbsp;&middot;&nbsp;
> Frontend Developer &nbsp;&middot;&nbsp;
> [sebastianbc09.github.io](https://sebastianbc09.github.io/v3/) &nbsp;&middot;&nbsp;
> LinkedIn [@sebastian-ballen-87851518a](https://www.linkedin.com/in/sebastian-ballen-87851518a/) &nbsp;&middot;&nbsp;
> GitHub [@SebastianBC09](https://github.com/SebastianBC09) &nbsp;&middot;&nbsp;
  
## API

### Users
 
### /users/create

-- Post 
-- Expected request body:

```json	
	{
	  "name": str,
	  "email": str,
	  "password": str,
	  "login_type": str,
	  "username": str,
	}
```
-- Expected response:

```json
	{
	  "response": "User created"
	}
```
-- Possible errors:
- 422: If the information given in the request body does not align with what is asked of it.
- 400: If the information given was invalid


### /user

-- GET
-- Expected request param (One or the other):

- username: str
- email: str

-- Expected response:


```json
	{
	  "name": str,
	  "email": str,
	  "password": str,
	  "login_type": str,
	  "username": str,
	}
	{
	  "response": {
	    "id": int,
	    "name": "str,
	    "email": str,
	    "username": str,
	    "password": str,
	    "login_type": str,
	    "badges": [
	      str
	    ],
	    "prefered_technologies": [
	      str
	    ],
	    "profile_pic": str
	  }
	}
```


-- Possible errors:
- 422: If the information given in the param does not align with what is asked of it.
- 400: If the information given was invalid
- 400: If you tried to send both email and username
- 400: If the user does not exist


### /user/edit

-- POST
-- Expected request body:

```json

 {
	    
	    "name": Optional[str],
	    "email": Optional[str],
	    "username": Optional[str],
	    "password": Optional[str],
	    "login_type": Optional[str],
	    "badges": Optional[[
	      str
	    ]],
	    "prefered_technologies": Optional[[
	      str
	    ]],
	    "profile_pic": Optional[str]
	  
	}
```


-- Expected response:

```json

	{
	  "response": "User updated"
	}
```

-- Possible errors:
- 422: If the information given in the param does not align with what is asked of it.
- 400: If the information given was invalid
- 400: If the user does not exist


### /user/delete

-- DELETE
-- Expected request body:

```json

 {
	    
	    "name": MANDATOY[str],
	    "email": Optional[str],
	    "username": Optional[str],
	    "password": Optional[str],
	    "login_type": Optional[str],
	    "badges": Optional[[
	      str
	    ]],
	    "prefered_technologies": Optional[[
	      str
	    ]],
	    "profile_pic": Optional[str]
	  
	}
```


-- Expected response:

```json

	{
	  "response": "User delete"
	}
```

-- Possible errors:
- 422: If the information given in the param does not align with what is asked of it.
- 400: If the information given was invalid
- 400: If the user does not exist

### Questions

### /questions

-- GET
-- Expected request params:
- technology: str
- level: str
- number_of_questions: int

-- Expected response:
```json
	{

	"response": {

		"questions": [

			{

			"question": str,

			"answers": [str],

			"correct_answer_index": int,

			"image": str

			}
		]
	}
```

-- Possible errors:
- 422: If the information given in the param does not align with what is asked of it.
- 400: If the data base does not have enough questions to give a proper response


### /questions/add

-- POST
-- Expected request body:

```json
{

	"question": str,

	"answers": [str],

	"right_answer": str,
	
	"level": int,

	"technology": int,

	"image": str,

	"password": str

}
```
-- Expected response:

```json

	{
	  "response": "Question added"
	}
```
-- Possible errors:
- 422: If the information given in the param does not align with what is asked of it.
- 401: If the credentials are not valid
- 400: If the question already exist

### Technologies

### /user/technology/add

-- POST
-- Expected request body:

```json
{
 "user":{	    
	    "name": MANDATOY[str],
	    "email": Optional[str],
	    "username": Optional[str],
	    "password": Optional[str],
	    "login_type": Optional[str],
	    "badges": Optional[[
	      str
	    ]],
	    "prefered_technologies": Optional[[
	      str
	    ]],
	    "profile_pic": Optional[str]
	  
	},
"technology":{
		"name": str
	}
}
```
-- Expected response:
```json

	{
	  "response": "Technology added"
	}
```
-- Possible errors:
- 422: If the information given in the param does not align with what is asked of it.
- 400: If the credentials user does not exist
- 400: If the user already has the technology added

### /user/technology/remove

-- DELETE
-- Expected request body:

```json
{
 "user":{	    
	    "name": MANDATOY[str],
	    "email": Optional[str],
	    "username": Optional[str],
	    "password": Optional[str],
	    "login_type": Optional[str],
	    "badges": Optional[[
	      str
	    ]],
	    "prefered_technologies": Optional[[
	      str
	    ]],
	    "profile_pic": Optional[str]
	  
	},
"technology":{
		"name": str
	}
}
```
-- Expected response:
```json

	{
	  "response": "Technology removed"
	}
```
-- Possible errors:
- 422: If the information given in the param does not align with what is asked of it.
- 400: If the credentials user does not exist
- 400: If the user already does not have selected technology

### /technologies
-- GET
-- Expected request params: None
-- Expected response:

```json

	{
	  "response": [
		  {
			  "name": str,
			  "image" str,
			  "summary": str
		  }
	  ]
	}
```
-- Possible errors:

### Progress
-- /user/progress/update
-- POST
-- Expected request body:
```json
{
 "user":{	    
	    "name": MANDATOY[str],
	    "email": Optional[str],
	    "username": Optional[str],
	    "password": Optional[str],
	    "login_type": Optional[str],
	    "badges": Optional[[
	      str
	    ]],
	    "prefered_technologies": Optional[[
	      str
	    ]],
	    "profile_pic": Optional[str]
	  
	},
"technology":{
		"name": str
	},
"percentage": int
}
```
-- Expected response:
```json

	{
	  "response": "Progress updated"
	}
```
-- Possible errors:
- 422: If the information given in the param does not align with what is asked of it.
- 400: If the credentials user does not exist

### Levels
-- /levels
-- GET
-- Expected request params: None

-- Expected response:
```json
	{
	  "response": [
		 str
	  ]
	}
```
-- Possible errors: