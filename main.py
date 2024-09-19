from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader

app = FastAPI()


# Создаем Jinja2 Environment
templates = Environment(loader=FileSystemLoader('templates'))

@app.get("/", response_class=HTMLResponse)
async def read_root():
    template = templates.get_template('index.html')
    rendered_template = template.render()
    return HTMLResponse(content=rendered_template)

@app.get("/")
async def root():
    return {"message": "Hello my"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
