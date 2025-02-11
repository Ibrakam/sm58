from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from api.photos import photo_router
from api.users import user_router
from api.hashtags import hashtag_router
from api.comments import comment_router
from api.posts import post_router
from db.postservice import get_all_or_exact_post

from db import Base, engine

templates = Jinja2Templates(directory="templates")
# Для создания бд
Base.metadata.create_all(engine)

app = FastAPI(docs_url="/")

app.include_router(photo_router)
app.include_router(user_router)
app.include_router(post_router)
app.include_router(comment_router)
app.include_router(hashtag_router)


@app.get("/user/{post_id}", response_class=HTMLResponse)
async def main(request: Request, post_id: int):
    user_post = get_all_or_exact_post(post_id)
    return templates.TemplateResponse(name="index.html", request=request,
                                      context={"user_post": user_post})

# pip install jinja2
