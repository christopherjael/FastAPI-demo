from fastapi import FastAPI
import uvicorn

import requests

app = FastAPI()


@app.get('/v1/')
async def root():
    return {'status': 200, 'message': 'Welcome to FastAPI'}

@app.get('/v1/people')
async def get_ramdon_user():
    url = 'https://randomuser.me/api/'
    res = requests.get(url)

    if res.status_code != 200:
        return {'message': 'Error to get data from ramdomuserAPI'}

    result  = res.json()
    return {'data': result}


@app.get('*')
async def page_not_found():
    return {
        "detail": "Not Found"
    }

if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=5000, log_level="info")
    server = uvicorn.Server(config)
    server.run()
