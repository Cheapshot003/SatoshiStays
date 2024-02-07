from fastapi import FastAPI, Request
import uvicorn
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import satDB

app = FastAPI()
satDB.create_table()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root(request: Request):
  return templates.TemplateResponse("index.html", {"request": request})


@app.get("/search")
async def search(request: Request):
  listings = satDB.getListings(request.query_params.get("name"))

  # Render the search results using a Jinja2 template
  return templates.TemplateResponse("search_results.html", {
      "request": request,
      "listings": listings
  })


uvicorn.run(app, host="0.0.0.0", port=8080)
