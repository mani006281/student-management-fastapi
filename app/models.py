from sqlalchemy import Column, Integer, String, Boolean
from .database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    email = Column(String(150), unique=True, nullable=False, index=True)
    age = Column(Integer)
    course = Column(String(100))


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)

    # 🔐 ROLE BASED ACCESS
    role = Column(String(20), default="user")   # admin / user

    is_active = Column(Boolean, default=True)

from .database import SessionLocal
from .models import User
from .auth import get_password_hash   # make sure this function exists

# 🔐 Auto create admin in production
db = SessionLocal()

admin_user = db.query(User).filter(User.username == "admin").first()

if not admin_user:
    new_admin = User(
        username="admin",
        password=get_password_hash("admin123"),
        role="admin"
    )
    db.add(new_admin)
    db.commit()
    print("✅ Admin created successfully!")

