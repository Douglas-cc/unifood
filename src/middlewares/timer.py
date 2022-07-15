from time import time 
from fastapi import Request

async def time_request(request: Request, next):
    start_time = time()
    response = await next(request)
    process_time = time() - start_time
    response.headers['X-Process-Time'] = str(process_time)
    return response 
