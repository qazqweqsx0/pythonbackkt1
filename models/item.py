from pydantic import BaseModel, field_validator
from pydantic_extra_types.color import Color

class Category(BaseModel):
    name: str
    color: Color

class Task(BaseModel):
    id: int
    title: str
    @field_validator("title")
    @classmethod
    def validate_title_length(cls, value: str) -> str:
        if len(value) < 3:
            raise ValueError("Длина названия задачи должна быть не менее 3 символов")
        return value
    description: str
    is_completed: bool = False
    category: Category
    internal_note: str

class TaskOut(BaseModel):
    id: int
    title: str
    @field_validator("title")
    @classmethod
    def validate_title_length(cls, value: str) -> str:
        if len(value) < 3:
            raise ValueError("Длина названия задачи должна быть не менее 3 символов")
        return value
    description: str
    is_completed: bool = False
    category: Category