from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")




@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="item.html", context={"id": id}
    )

@app.get("/calculate", response_class=HTMLResponse)
async def calculate(request: Request):
    print("cal")
    print(request.query_params)
    print(request.base_url)
    return templates.TemplateResponse(
        request=request, name="answer.html", context={}
    )
@app.get("/", response_class=HTMLResponse)
async def pg1(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={}
    )