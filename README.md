
# Libretto Project Launch Guide
This part provides API for interaction with openAI chat.   

## Installation
pip install -r requirements.txt

## Configuration: 
Application use `OPENAI_API_KEY`. It should be written in `.env`
Model for interation with chatGPT should defind in `.env` too. 
Example of file is provided in `.env.example`

## Run API server: 
```shell 
uvicorn app.main:app --reload --port=8008
```
*Command for API server can be changed (port number). It can depend on environment.* 

## URL for Swagger DOCS: 
```http://127.0.0.1:8008/docs```

If API should be available in the WWW we can use ngrok: 
```ngrok http 8008```


## Technologies Used

 There were used: 
 - python with FastAPI
 - uvicorn as web server

## Design Decision
Architecture solutions: 
 - Services. It should keep service functionality.  
 - DTO. Designed for dividing data level from functionality.  
 - Routes. Should keep routes for each section divided.  
