import asyncio
from fastapi import FastAPI, Depends, BackgroundTasks, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from typing import List
from contextlib import asynccontextmanager

from database import engine, Base, get_db
import models
import schemas

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(title="Optimized Finalization API", version="1.0", lifespan=lifespan)

# 🌟 SIMULATED HEAVY BACKGROUND TASK
def cpu_heavy_report_generation(department_name: str):
    print(f"[BACKGROUND TASK STARTED] Initiating report card compilation for {department_name}...")
    # Simulate a heavy 5-second database aggregation/file building process
    import time
    time.sleep(5) 
    print(f"[BACKGROUND TASK COMPLETED] Report PDF successfully generated and cached for {department_name}!")

# --- OPTIMIZED EAGER LOADING ROUTE ---
@app.get('/api/departments/optimized', response_model=List[schemas.DepartmentResponse], tags=['Optimization'])
async def get_departments_optimized(db: AsyncSession = Depends(get_db)):
    """
    Fetches all departments and efficiently eager-loads all associated courses 
    in exactly 2 database queries using `selectinload`, solving the N+1 problem.
    """
    result = await db.execute(
        select(models.Department).options(selectinload(models.Department.courses))
    )
    departments = result.scalars().all()
    return departments

# --- BACKGROUND TASKS ROUTE ---
@app.post('/api/departments/{id}/report', status_code=status.HTTP_202_ACCEPTED, tags=['Background Tasks'])
async def trigger_department_report(
    id: int, 
    background_tasks: BackgroundTasks, 
    db: AsyncSession = Depends(get_db)
):
    """
    Accepts the request instantly (202 Accepted) and runs the heavy computation 
    in the background without making the user wait.
    """
    result = await db.execute(select(models.Department).where(models.Department.id == id))
    dept = result.scalar_one_or_none()
    
    dept_name = dept.name if dept else f"Department ID {id}"
    
    # Hand off the task to FastAPI's background worker system
    background_tasks.add_task(cpu_heavy_report_generation, dept_name)
    
    return {"message": f"Report compilation for '{dept_name}' has been offloaded to background workers successfully."}