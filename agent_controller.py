import hashlib
import time
from loguru import logger
from docuforge import generate_pdf

class PromptIngestor:
    def sanitize(self, prompt: str) -> str:
        """
        Sanitizes the input prompt.
        For this MVP, we'll just do basic stripping of whitespace.
        """
        return prompt.strip()

    def validate(self, prompt: str):
        """
        Validates the prompt.
        Raises ValueError if the prompt is invalid.
        """
        if not prompt:
            raise ValueError("Prompt cannot be empty.")

class DocGenAgent:
    async def generate(self, prompt: str, title: str) -> bytes:
        """
        Generates a PDF from the prompt using DocuForge.
        """
        logger.info(f"Generating PDF for prompt: {prompt[:50]}...")
        doc_data = {
            "title": title,
            "sections": [{"type": "paragraph", "text": prompt}],
        }
        return generate_pdf(doc_data)

class AgentController:
    def __init__(self):
        self.prompt_ingestor = PromptIngestor()
        self.doc_gen_agent = DocGenAgent()

    async def process_request(self, prompt: str, title: str) -> bytes:
        """
        Processes the request to generate a PDF.
        """
        start_time = time.time()
        prompt_hash = hashlib.sha256(prompt.encode()).hexdigest()
        logger.info(f"Processing request with prompt_hash: {prompt_hash}")

        try:
            sanitized_prompt = self.prompt_ingestor.sanitize(prompt)
            self.prompt_ingestor.validate(sanitized_prompt)

            pdf_bytes = await self.doc_gen_agent.generate(sanitized_prompt, title)

            end_time = time.time()
            execution_time = end_time - start_time
            logger.info(
                f"Successfully processed request with prompt_hash: {prompt_hash}. "
                f"Execution time: {execution_time:.2f}s"
            )
            return pdf_bytes

        except Exception as e:
            logger.error(f"Error processing request with prompt_hash: {prompt_hash}. Error: {e}")
            raise
