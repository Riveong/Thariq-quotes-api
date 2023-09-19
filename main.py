from fastapi import FastAPI
import random
quotes = [
    {
        "id":"1",
        "en":"[REDACTED] gw gatel"
    },
    {
        "id":"2",
        "en":"orang pintar has small [REDACTED]"
    },
    {
        "id":"3",
        "en":"jika [REDACTED] gatal maka garuklah"
    },
    {
        "id":"4",
        "en":"hmm..."
    },
    {
        "id":"5",
        "en":"I love your mom"
    },
    {
        "id":"6",
        "en":"call me D because mine itch"
    },
    {
        "id":"7",
        "en":"WOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    }
    
    ]



app = FastAPI()


@app.get("/")
def getItems():
    quote = random.choice(quotes)
    return quote


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=port, timeout_keep_alive=1200)