from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="OnCall API",
    description="Simple API demonstrating MCP tool use cases",
    version="1.0.0"
)


class Message(BaseModel):
    text: str


@app.get("/")
def root():
    return {"message": "OnCall API Running"}


@app.get("/status")
def status():
    return {"status": "ok"}


@app.post("/echo")
def echo(msg: Message):
    return {"echo": msg.text}


@app.get("/prompts/templates", summary="Returns vetted system prompt templates by agent role")
def get_prompt_templates():
    """
    Returns a curated list of system prompt templates for common agent roles.
    """
    return {
        "templates": [
            {
                "role": "judge",
                "description": "Evaluates agent outputs for quality and accuracy",
                "system_prompt": (
                    "You are an impartial evaluator. Given an agent's output, assess it on "
                    "clarity, accuracy, and relevance. Return a score from 1-10 with a brief justification."
                )
            },
            {
                "role": "refiner",
                "description": "Rewrites and improves system prompts based on judge feedback",
                "system_prompt": (
                    "You are a prompt engineer. Given a system prompt and a critique, rewrite "
                    "the prompt to address the weaknesses identified. Preserve the original intent."
                )
            },
            {
                "role": "coordinator",
                "description": "Orchestrates the judge-refine loop between agents",
                "system_prompt": (
                    "You are a workflow coordinator. Route tasks between the judge and refiner agents "
                    "until the judge score meets the acceptance threshold. Report the final prompt when done."
                )
            }
        ]
    }
