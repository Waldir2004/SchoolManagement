from fastapi import FastAPI
from routes.user_routes import router as user_router
from routes.parameter_value_routes import router as parameter_value_router
from routes.parameter_routes import router as parameter_router
from routes.info_school_routes import router as info_school_router
from routes.school_user_routes import router as school_user_router
from routes.participant_activity_routes import router as participant_activity_router
from routes.participant_meeting_routes import router as participant_meeting_router
from routes.school_routes import router as school_routes
from routes.roles_routes import router as roles_routes
from routes.activities_routes import router as activities_routes
from routes.comments_activities_routers import router as comments_activities_routes
from routes.evidence_activities_routers import router as evidence_activities_routers
from routes.meetings_routers import router as meetings_routers
from routes.reports_routes import router as reports_router
from routes.reports_evidencies_routers import router as reports_evidencies_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    #"http://localhost.tiangolo.com",
    #"https://localhost.tiangolo.com",
    "http://localhost"
    #"http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(parameter_value_router)
app.include_router(parameter_router)
app.include_router(info_school_router)
app.include_router(school_user_router)
app.include_router(participant_activity_router)
app.include_router(participant_meeting_router)
app.include_router(school_routes)
app.include_router(roles_routes)
app.include_router(activities_routes)
app.include_router(comments_activities_routes)
app.include_router(evidence_activities_routers)
app.include_router(meetings_routers)
app.include_router(reports_router)
app.include_router(reports_evidencies_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)