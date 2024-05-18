from fastapi import FastAPI , Query
import uvicorn
from pydantic import BaseModel,Field
from typing import Annotated

app=FastAPI()
#for body parameter
class Item(BaseModel):
    id :int
    title:str
    description:str
#field for valadation in body parameter
class User(BaseModel):
    id :int
    name:str =Field(max_length=10,min_length=2)
    description:str   


#path and quary parameters 
@app.get("/students/{id}")
def mainroute(id:int,data:str | int =None): #if =none ni kara ga to wo error da ga agar frontend sa information ni ati to because ya query parameter ha "data"
    return {"message":"Hello",
            "output":id,
            "data":data
            }
    
#body parameter
@app.get("/students")
def mainroute(item:Item ,user:User):
    return item ,user


 #for valadition    
#@app.get("/students")
#def route(item_sf:Annotated(str,Query(alias="item-test",max_length=10,min_length=4,pattern="^fix[a-zA-Z0-9]"))):
#    return item_sf





def start():
    uvicorn.run("api_routes.main:app",host="127.0.0.1",port=8080,reload=True)