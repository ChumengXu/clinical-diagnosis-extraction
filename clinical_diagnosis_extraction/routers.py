from typing import List, Dict
from clinical_diagnosis_extraction import inference
from fastapi import APIRouter, HTTPException, Response

router = APIRouter(prefix="")


@app.get("/")
def index():
    return {"message": "Hello, World!"}


@router.post("/extract-diagnoses", response_model=Dict[str, List])
async def extract_clinical_diagnoses(
    request_data: Dict[str, str],
) -> list[Dict[str, List]]:
    clinical_note = request_data.get("clinical_note")
    if not clinical_note:
        raise HTTPException(status_code=400, detail="clinical_note is required")
    result = inference(clinical_note)

    return result
