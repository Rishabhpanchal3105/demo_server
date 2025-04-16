from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date, time
from fastapi.middleware.cors import CORSMiddleware

import logging
import uvicorn
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_methods=['*'],
    allow_origins=['*']
)


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

if __name__ == "__main__":
    uvicorn.run(port=5000)
