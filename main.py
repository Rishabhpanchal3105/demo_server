from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date, time
import logging

logger = logging.getLogger(__name__)

app = FastAPI()


class BookAppointmentRequest(BaseModel):
    name: str
    date: date
    time: time


@app.post('/book_appointment')
async def book_appointment(appointment: BookAppointmentRequest):
    # In a real app, you would save this to a database

    logger.info({"message": "Appointment is booked", "appointment_details": {
        "name": appointment.name,
        "date": appointment.date,
        "time": appointment.time
    }})
    return {
        "message": "Appointment is booked",
        "appointment_details": {
            "name": appointment.name,
            "date": appointment.date,
            "time": appointment.time
        }
    }
