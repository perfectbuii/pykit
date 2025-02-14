# Target to run the FastAPI application
run:
	poetry run uvicorn cmd.main:app --host 0.0.0.0 --port 8000