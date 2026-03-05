from fastapi import APIRouter, Depends, Query, status
from src.schemas.locations import Location
from src.domain.locations.use_cases.get_locations import GetLocationsUseCase

router = APIRouter(prefix="/locations", tags=["Locations"])


@router.get("/", response_model=list[Location], status_code=status.HTTP_200_OK)
async def get_locations(
    published_only: bool = Query(False, description="Только опубликованные"),
    use_case: GetLocationsUseCase = Depends()
) -> list[Location]:
    """Получить все локации"""
    return await use_case.execute(published_only=published_only)