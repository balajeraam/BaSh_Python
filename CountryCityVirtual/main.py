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


@app.get("/rr",response_class=HTMLResponse)
async def read(request: Request):
    
    return templates.TemplateResponse("RightPrint_home.html",{"request": request})

@app.post("/rr",response_class= HTMLResponse)
async def handle_form(request: Request, country: str = Form(...), city: str = Form(...)):
    if country == "USA" and city == "ARKANSAS" :
        image_file1 = "Arkansas1.JPG"
        image_file2 = "Arkansas2.JPG"
    elif country == "INDIA" and city == "TRICHY":
        image_file1 = "Trichy1.JPG"
        image_file2 = "Trichy2.JPG"
    else:
        image_file1 ="BaselSBB.JPG"
        image_file2 ="MB.PNG"
    
    image_file3 = "swissflag.jpg"

    
    return templates.TemplateResponse("RightPrint_output.html",{"request": request , "id_country":country, "id_city":city, "image_file1": image_file1, "image_file2": image_file2, "image_file3":image_file3}) 
    





