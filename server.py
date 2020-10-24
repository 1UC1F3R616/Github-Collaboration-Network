from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/media", StaticFiles(directory="media/"), name="media")
templates = Jinja2Templates(directory="templates/")

############################################## utils #########################################
from utils.util_imp_users import imp_users
from utils.util_largest_community import largest_community
from utils.util_recommended_networking import recommended_networking
from utils.util_commit_here import commit_here
from utils.util_similarity_index import similarity_index
############################################## utils #########################################

############################################## utils #########################################

@app.get('/')
# @app.get("/home")
# @app.get("/index")
async def home(request: Request):
    result = {}
    return templates.TemplateResponse('index.html', context={'request': request, 'result': result})

@app.get('/documentation')
async def documentation(request: Request):
    result = {'message': 'will be updated sooner, 24-10-2020 22:50pm'}
    return templates.TemplateResponse('documentation.html', context={'request': request, 'result': result})

@app.post('/profiling')
async def profiling(request: Request, username: str = Form(...)):
    result = {}
    # print(imp_users(username))
    # print(largest_community(username))
    # print(recommended_networking(username))
    # print(commit_here(username))
    # print(similarity_index(username))
    return templates.TemplateResponse('index.html', context={'request': request, 'result': result})

@app.post('/impUsers')
async def impUsers(request: Request, username: str = Form(...)):
    result = {'imp_users': imp_users(username)}
    print(result)
    return result
    # return templates.TemplateResponse('index.html', context={'request': request, 'result': result})

@app.post('/nextHack')
async def nextHack(request: Request, username: str = Form(...)):
    print(username)
    result = {'largest_community': largest_community(username)}
    print(result)
    return result

@app.post('/recommendNet')
async def recommendNet(request: Request, username: str = Form(...)):
    result = {'recommended_networking': recommended_networking(username)}
    print(result)
    return result

@app.post('/commitHere')
async def commitHere(request: Request, username: str = Form(...)):
    result = {'commit_here': commit_here(username)}
    print(result)
    return result

@app.post('/similarityIndex')
async def similarityIndex(request: Request, username: str = Form(...)):
    print(username)
    result = {'similarity_index': similarity_index(username)}
    print(result)
    return result
