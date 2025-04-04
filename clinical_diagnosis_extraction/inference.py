from textwrap import dedent
from vllm import LLM


def inference(clinical_note: str) -> str:

    with open("prompts/extract_diagnoses.txt", "r") as file:
        prompt_template = file.read()
    prompt = dedent(
        f"""
    {prompt_template}
    data to extract: {clinical_note}
    Please extract the clinical diagnoses from the above data
    and based on the above guidelines.
                """
    )

    llm = LLM(model="ClinicalBERT", task="generate")
    output = llm.generate(prompt)
    return output
