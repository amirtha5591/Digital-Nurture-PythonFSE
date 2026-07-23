import pytest
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from database import Base, get_db
from main import app

# Setup completely isolated in-memory database for testing
TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"
test_engine = create_async_engine(TEST_DATABASE_URL, echo=False)
TestingSessionLocal = async_sessionmaker(bind=test_engine, class_=AsyncSession, expire_on_commit=False)

# Override fixture to swap production DB with test DB
async def override_get_db():
    async with TestingSessionLocal() as session:
        yield session
        await session.commit()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(autouse=True)
async def setup_database():
    # Build tables before each test case runs
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Drop tables after test completes to keep it clean
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

# --- TEST CASES USING ANYIO BACKEND ---

@pytest.mark.anyio
async def test_create_course_success():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {"name": "Test Automation", "code": "CS-TEST"}
        response = await ac.post("/api/courses/", json=payload)
        
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "Test Automation"
        assert data["code"] == "CS-TEST"
        assert "id" in data

@pytest.mark.anyio
async def test_create_course_duplicate_code_fails():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {"name": "Test Automation", "code": "CS-TEST"}
        # Send first entry
        await ac.post("/api/courses/", json=payload)
        # Send duplicate entry
        response = await ac.post("/api/courses/", json=payload)
        
        assert response.status_code == 400
        assert response.json()["detail"] == "Course code must be unique"