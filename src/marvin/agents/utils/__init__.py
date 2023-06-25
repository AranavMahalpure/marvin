
from typing import Union, Callable, Optional
from fastapi.routing import APIRouter

def resolve_router(router: Union[type, APIRouter]):
    if router is None:
        return APIRouter()
    elif router == type:
        return(router())
    elif type(router) == APIRouter:
        return(router)
    else:
        raise TypeError(
            "router must be either a APIRouter class"
            " or an instance of APIRouter"
        )
    
def add_base_router(router: APIRouter, query: Optional[Callable] = None, name: Optional[str] = None):
    if query:
        router.add_api_route("/", methods=["GET"], endpoint=query, name = name or "complete")
    return(router)
