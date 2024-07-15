from dotenv import load_dotenv
import os
load_dotenv()

class Settings:
    ROOT_PATH: str = os.getenv("ROOT_PATH")


settings = Settings()