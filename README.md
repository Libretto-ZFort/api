Install required packages: 
pip install -r requirements.txt

Run API server: 
uvicorn app.main:app --reload --port=8008

Command for API server can be changed (port number). It can depend on environment. 

URL for Swagger DOCS: 
http://127.0.0.1:8008/docs

If API should be available in the WWW we can use ngrok: 
ngrok http 8008
