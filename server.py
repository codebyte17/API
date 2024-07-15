import sys
import os

# Add the 'app' directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))

from app.main import app  # Assuming your FastAPI app instance is named `app`


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
