from fastapi import APIRouter, Depends, status
from src.schemas.users import User
from src.domain.users.use_cases.get_users import GetUsersUseCase
from src.domain.users.use_cases.get_user_by_id import GetUserByIdUseCase
from src.domain.users.use_cases.get_user_by_username import GetUserByUsernameUseCase

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=list[User], status_code=status.HTTP_200_OK)
async def get_users(
    use_case: GetUsersUseCase = Depends()
) -> list[User]:
    """Получить всех пользователей"""
    return await use_case.execute()


@router.get("/by-username/{username}", response_model=User, status_code=status.HTTP_200_OK)
async def get_user_by_username(
    username: str,
    use_case: GetUserByUsernameUseCase = Depends()
) -> User:
    """Получить пользователя по username"""
    return await use_case.execute(username=username)


@router.get("/{user_id}", response_model=User, status_code=status.HTTP_200_OK)
async def get_user_by_id(
    user_id: int,
    use_case: GetUserByIdUseCase = Depends()
) -> User:
    """Получить пользователя по ID"""
    return await use_case.execute(user_id=user_id)