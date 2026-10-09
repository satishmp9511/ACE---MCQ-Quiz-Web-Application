from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()
templates = Jinja2Templates(directory=".")
app.mount("/static", StaticFiles(directory="."), name="static")

op_Q = {}

w = 1

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "QW.txt")

with open(FILE_PATH, "r", encoding="utf-8") as f:
    t = 1
    for i in f:
        l = i.strip()
        p = l.split("-")   
        if len(p) == 6:
            q_ = p[0].strip()
            ans_ = p[1].strip()
            o1_ = p[2].strip()
            o2_ = p[3].strip()
            o3_ = p[4].strip()
            o4_ = p[5].strip()
            
            op_Q[t] = [q_, ans_, o1_, o2_, o3_, o4_]
            t += 1

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    global w
    w = 1
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "q": op_Q[w][0],
            "n1": op_Q[w][2],
            "n2": op_Q[w][3],
            "n3": op_Q[w][4],
            "n4": op_Q[w][5]
        }
    )

@app.post("/ch", response_class=HTMLResponse)
def ch_(request: Request, an: int = Form(...)):
    if w not in op_Q:
        current_q = op_Q[1]
    else:
        current_q = op_Q[w]

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "q": current_q[0],
            "n1": current_q[2],
            "n2": current_q[3],
            "n3": current_q[4],
            "n4": current_q[5],
            "c": ("correct" if str(an) == str(current_q[1]) else "wrong")
        }
    )

@app.post("/next", response_class=HTMLResponse)   
def ne(request: Request, nan: int = Form(...)):
    global w
    if nan in op_Q:
        w = nan
    else:
        w = 1
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "q": op_Q[w][0],
            "n1": op_Q[w][2],
            "n2": op_Q[w][3],
            "n3": op_Q[w][4],
            "n4": op_Q[w][5],
            "c": ''
        }
    )
