
# Libretto Project Launch Guide
This part provides API for interaction with openAI chat.   

## Configuration: 
Application use `OPENAI_API_KEY`. It should be written in `.env`
Model for interation with chatGPT should defined in `.env` too. 
Example of file is provided in `.env.default`
Should be written values for: 
SUPABASE__URL
SUPABASE__API_KEY

```sh
cp .env.default .env
```

### Run project in Docker

```sh
docker-compose up
```

API swagger: 
```http://localhost:8000/docs```

If API should be available in the WWW we can use ngrok: 
```ngrok http 8000```


## Technologies Used

 There were used: 
 - python with FastAPI
 - uvicorn as web server
 - Supabase as database. 

## Design Decision
- Modular Structure: The project is structured into modules, promoting separation of concerns and making the codebase more maintainable and scalable.
- Domain-Driven Design: The presence of a 'domain' module suggests that the application is built with domain-driven design principles, focusing on the core business logic and rules.
- Infrastructure Isolation: By placing infrastructure-related code in its own module, the project ensures that changes to infrastructure implementations do not affect the domain logic, facilitating easier updates and maintenance.
- Configuration Management: A separate configuration module indicates a strategy to manage different environments and settings, centralizing the configuration for ease of access and control.
- Entry Point Separation: The existence of a 'main.py' file at the root of the infrastructure suggests a clear entry point for the application, making deployment and execution straightforward.
- Operational Tasks: The operational module indicates forethought into the day-to-day and administrative tasks that will be necessary to keep the application running smoothly.
- Virtual Environment: The use of a virtual environment shows a commitment to dependency management and reproducible builds, which is crucial for collaborative development and production stability.
