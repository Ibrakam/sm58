from fastapi import APIRouter
from db.postservice import *
from api import result_message

hashtag_router = APIRouter(prefix="/hashtags", tags=["Хэштеги"])
