from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from agent_controller import AgentController
from loguru import logger
import io

app = FastAPI()
agent_controller = AgentController()

@app.get("/render")
async def render_pdf(prompt: str, title: str = "doc"):
    """
    Renders a PDF document from a prompt.
    """
    if not prompt:
        raise HTTPException(status_code=400, detail="Prompt cannot be empty.")

    try:
        pdf_bytes = await agent_controller.process_request(prompt, title)
        
        return StreamingResponse(
            io.BytesIO(pdf_bytes),
            media_type="application/pdf",
            headers={"Content-Disposition": f"attachment; filename={title}.pdf"}
        )
    except ValueError as e:
        logger.warning(f"Validation error: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        raise HTTPException(status_code=500, detail="An internal error occurred while generating the PDF.")

@app.on_event("startup")
async def startup_event():
    logger.add("file_{time}.log", rotation="500 MB")
    logger.info("Application startup complete.")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application shutting down.")
