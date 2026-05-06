from pydantic import BaseModel, EmailStr, Field

class UsuarioSchema(BaseModel):
    nombre: str = Field(
        min_length=3,
        max_length=50,
        description="El nombre debe tener al menos 3 caracteres"
    )

    email: EmailStr

    password: str = Field(
        min_length=4,
        max_length=20,
        description="La contraseña debe tener mínimo 4 caracteres"
    )