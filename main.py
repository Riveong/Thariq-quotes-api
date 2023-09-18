from fastapi import FastAPI
import random
quotes = ["[REDACTED] gw gatel","orang pintar has small [REDACTED]","jika [REDACTED] gatal maka garuklah","hmm...","I love your mom","call me D because mine itch","WOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA","IAM ANJURNAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"]



app = FastAPI()


@app.get("/")
def getItems():
    quote = random.choice(quotes)
    return quote


    if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=port, timeout_keep_alive=1200)