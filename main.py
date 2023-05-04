import time

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from Translator import Translator

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)


@app.post("/v1/translator/python")
async def translate_realtime(request: Request):
    # Measure the start time
    start_time = time.perf_counter()

    request_body = await request.json()
    input_text = request_body["input-text"]

    if input_text == '':
        return JSONResponse({'output_text': '',
                             'backend_time': 0})

    try:
        output_text = Translator(input_text)
    except:
        pass

    # Measure the end time
    end_time = time.perf_counter()

    # Calculate the elapsed time in milliseconds
    elapsed_time_ms = (end_time - start_time) * 1000

    # Round the elapsed time to two decimal places
    elapsed_time_ms = round(elapsed_time_ms, 2)

    print(elapsed_time_ms)

    return JSONResponse({'output_text': output_text.__str__(),
                         'backend_time': elapsed_time_ms})
