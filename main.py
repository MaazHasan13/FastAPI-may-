from fastapi import FastAPI , HTTPException,Depends,Header
from jose import jwt
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from datetime import datetime,timedelta,timezone
from passlib.context import CryptContext
from jose import JWTError
app = FastAPI()

##secreate key

SECREAT_KEY = "mysecret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES =30

#PASSWORD HASING SETUP
pwd_context = CryptContext(schemes = ["bcrypt"])

#oauthsetup
oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

#dummy user db
fake_user_db = {
    "admin":{
        "username" : "admin",
        "hashed_password" : pwd_context.hash("1234")
    }
}

#hash password
def hash_password(password:str):
    return pwd_context.hash(password)

#verify password
def varify_password(plain_password,hased_password):
    return pwd_context.verify(plain_password,hased_password)



def create_token(data:dict):
    to_encode = data.copy()
    expire  = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({
        "exp":expire
    })

    token = jwt.encode(to_encode,SECREAT_KEY,algorithm=ALGORITHM)

    return token

#login api(token genrate oauth2from)
f
@app.post("/login")
def login(username:str,password:str):
    if username != "admin" or password != "1234":
        raise HTTPException(
            status_code=401,
            detail="invalid username and password"
        )
    token = create_token({
        "sub" : username
    })
    return{
        "access_token":token

   }
#token veryfy
def varify_token(token:str=Header(None)):
    try:
        payload = jwt.decode(token,SECREAT_KEY,algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(
            status_code=401,
            detail="invalid username and password"
        )
    
#protected rpute
@app.get("/secure")
def secure_data(user = Depends(varify_token)):
    return{
        "message" : "secure Data Accesssed",
        "user" : user
    }