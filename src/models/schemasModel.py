from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date, time

class UsuarioSchema(BaseModel):
    nombre: str = Field(min_length=3, max_length=100)
    email : EmailStr
    password: str = Field(min_length=8)
    
    class LoginSchema(BaseModel):
        email : EmailStr
        password: str = Field(min_length=8)
    class TareaSchema(BaseModel):
        titulo: str = Field(min_length=1, max_length=200)
        descripcion: Optional[str] = None
        prioridad: str = "media"
        clasificacion: str = "personal"
        
    class usuarioAlta(BaseModel):
        
        nombre: str =Field(min_legth=2,max_legth=10)
        apellido: str =Field(min_legth=2,max_legth=10)
        email: EmailStr
        password:str =Field(min_legth=8),
        telefono :Optional[str] = Field( None,min_legth=10,max_legth=15)
        foto= Optional[str] = Field( None,min_legth=10,max_legth=15)
        ##campos que no pide en el  formulario pero son necesario a la hora de agregar el usuario
        #base de datos
        activo: bool= True
        fecha_registro: datetime = Field(default_factory=datetime.now)
        ultimo_acceso : datetime = Field(default_factory=datetime.now)