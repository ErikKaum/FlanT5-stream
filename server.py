import asyncio
from fastapi import FastAPI, Request
from sse_starlette.sse import EventSourceResponse
import app as user_src

user_src.init()

app = FastAPI()

@app.get('/health')
def health():
    return "all good"

@app.post('/')
async def message_stream(request: Request):

    model_inputs = await request.json()
    print(model_inputs)
    
    async def event_generator():
        print("here")
        output = user_src.inference(model_inputs)
        print(output)
        for i in output:
            print(i)
            yield {
                "data": str(i)
            }
            # await asyncio.sleep(1)
        
        yield {
            "data": "[DONE]"
        }

    return EventSourceResponse(event_generator())
