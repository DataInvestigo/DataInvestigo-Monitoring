from app.database import Base, engine
from app.models import (
    ResourceUtilization,
    SystemHealth,
    Security,
    PerformanceMetrics,
    Backup,
    Logs,
    Management
)

def create_tables():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created.")

if __name__ == "__main__":
    create_tables()
