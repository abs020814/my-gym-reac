from fastapi import APIRouter, Depends, HTTPException
from ...database import get_db
import aiomysql
from typing import List
from authlib.integrations.starlette_client import OAuth

router = APIRouter()


# Configurar el cliente OAuth (por ejemplo, para Google)
oauth = OAuth()
oauth.register(
    name='google',
    client_id='859314345775-ne6gm0veepa4ntsajkpgm6qaga17e29j.apps.googleusercontent.com',
    client_secret='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',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    refresh_token_url=None,
    redirect_uri='http://localhost:3000/auth',
    client_kwargs={'scope': 'openid profile email'}
)
# Ruta para iniciar la autenticación con Google
@router.get("/login")
async def login_via_google():
    redirect_uri = 'http://localhost:3000/auth'
    return await oauth.google.authorize_redirect(redirect_uri)