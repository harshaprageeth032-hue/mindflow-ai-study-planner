from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class StudyNote(Base):
    __tablename__ = "study_notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    raw_content = Column(Text, nullable=False)
    ai_summary = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    tasks = relationship("Task", back_populates="note", cascade="all, delete")

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    note_id = Column(Integer, ForeignKey("study_notes.id"), nullable=True)
    description = Column(String(300), nullable=False)
    priority = Column(String(20), default="Medium")
    estimated_minutes = Column(Integer, default=30)
    is_completed = Column(Boolean, default=False)

    note = relationship("StudyNote", back_populates="tasks")
