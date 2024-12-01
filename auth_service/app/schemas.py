from pydantic import BaseModel, EmailStr

# Schema for User Registration
class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    role: str

    class Config:
        orm_mode = True


# Schema for Login
class Login(BaseModel):
    email: EmailStr
    password: str

# Schema for Token Response
class Token(BaseModel):
    access_token: str
    token_type: str
