from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

DUMMY_HASH = "$2b$12$R9h7cIPz0gi.URNNGU3He.OPST9/PgBkqquzi.Ss2JRXb86LJezm"


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
