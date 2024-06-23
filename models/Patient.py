import uuid
import datetime
from app import db
from sqlalchemy.orm import Mapped, mapped_column


class Patient(db.Model):
  __tablename__ = 'patients'

  patient_id: Mapped[str] = mapped_column(db.String(36), primary_key=True, default= lambda : str(uuid.uuid4))
  first_name: Mapped[str]
  last_name: Mapped[str]
  birth_date: Mapped[datetime.date]

  def __repr__(self) -> str:
    return f"<Patient(id = {self.patient_id}, name = {self.first_name} {self.last_name}, birth_date = {self.birth_date})>"