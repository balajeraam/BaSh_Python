from fastapi import FastAPI, Request , File, UploadFile , Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from requests import request

app = FastAPI()

templates = Jinja2Templates(directory="htmldirectory")
app.mount("/static",StaticFiles(directory="static"), name="static")

@app.get("/")
async def hello_world():
    return {"message": "Hello World"}


@app.get("/rp",response_class=HTMLResponse)
async def read(request: Request):
    
    return templates.TemplateResponse("RightPrint_home.html",{"request": request})

@app.post("/rp",response_class= HTMLResponse)
async def handle_form(request: Request, indicator: str = Form(...), presentationcode: str = Form(...), packlevel: str = Form(...), sitecode: str=Form(...) ):
   
    image_filename ="MB.PNG"
    
    return templates.TemplateResponse("RightPrint_output.html",{"request": request , "id_ind":indicator, "id_pcode":presentationcode, "id_plevel":packlevel, "id_site": sitecode , "image_filename": image_filename})
    





