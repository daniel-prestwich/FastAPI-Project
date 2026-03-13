from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def root():
    return {"please": "work"}


app = FastAPI(
    title="MCP Server please work",
    description="Simple MCP server with 3 endpoints",
    version="1.0.0"
)

class Message(BaseModel): #need to import this.
    text: str



@app.get("/")
def root():
    return {"message": "MCP Server Running"}



@app.get("/status")
def status():
    return {"status": "ok"}



@app.post("/echo")
def echo(msg: Message):
    return {"echo": msg.text}