from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import engine, get_db, Base
import models
import ai_service


Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Smart Study & Task Planner API")


class NoteCreateRequest(BaseModel):
    title: str
    raw_content: str

@app.post("/api/notes/analyze")
def create_and_analyze_note(request: NoteCreateRequest, db: Session = Depends(get_db)):
    try:
        
        ai_result = ai_service.generate_study_plan(request.raw_content)

        
        new_note = models.StudyNote(
            title=request.title,
            raw_content=request.raw_content,
            ai_summary=ai_result["summary"]
        )
        db.add(new_note)
        db.commit()
        db.refresh(new_note)

        
        created_tasks = []
        for item in ai_result["tasks"]:
            new_task = models.Task(
                note_id=new_note.id,
                description=item["description"],
                priority=item["priority"],
                estimated_minutes=item["estimated_minutes"]
            )
            db.add(new_task)
            created_tasks.append(new_task)

        db.commit()
        return {
            "id": new_note.id,
            "title": new_note.title,
            "summary": new_note.ai_summary,
            "tasks": ai_result["tasks"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/notes")
def get_all_notes(db: Session = Depends(get_db)):
    notes = db.query(models.StudyNote).order_by(models.StudyNote.created_at.desc()).all()
    result = []
    for n in notes:
        result.append({
            "id": n.id,
            "title": n.title,
            "summary": n.ai_summary,
            "created_at": n.created_at,
            "tasks": [
                {
                    "id": t.id,
                    "description": t.description,
                    "priority": t.priority,
                    "estimated_minutes": t.estimated_minutes,
                    "is_completed": t.is_completed
                }
                for t in n.tasks
            ]
        })
    return result

@app.patch("/api/tasks/{task_id}/toggle")
def toggle_task_status(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.is_completed = not task.is_completed
    db.commit()
    return {"id": task.id, "is_completed": task.is_completed}

@app.delete("/api/notes/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(models.StudyNote).filter(models.StudyNote.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(note)
    db.commit()
    return {"message": "Note and associated tasks deleted"}
