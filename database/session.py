from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL ='postgresql://neondb_owner:npg_6ROUVWtp2ufL@ep-raspy-violet-a4xfnnec-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)