from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from datetime import date , time
import logging
import uvicorn
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_methods=['*'],
    allow_origins=['*']
)

class QueryModel(BaseModel):
    name: str
    date: date
    time: time

class BookAppointmentRequest(BaseModel):
    query: QueryModel

@app.post('/book_appointment')
async def book_appointment(appointment: BookAppointmentRequest):
    # In a real app, you would save this to a database
    
    logger.info({"message": "Appointment is booked", "appointment_details": {
        "name": appointment.query.name,
        "date": appointment.query.date,
        "time": appointment.query.time
    }})
    return {
        "message": "Appointment is booked",
        "appointment_details": {
            "name": appointment.query.name,
            "date": appointment.query.date,
            "time": appointment.query.time
        }
    }

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000)
