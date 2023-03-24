from dotenv import load_dotenv
from pydantic import BaseModel
from fastapi import FastAPI
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class Request(BaseModel):
     prompt: str


@app.get("/")
def read_root():
	return {"Hello": "World"}


@app.post("/")
async def create_image(request: Request):
	response = openai.Image.create(
		prompt=request.prompt,
		n=2,
		size="1024x1024"
	)

	return response
