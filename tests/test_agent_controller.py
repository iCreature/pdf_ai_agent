import pytest
from unittest.mock import patch, MagicMock
from agent_controller import AgentController

@pytest.fixture
def agent_controller():
    return AgentController()

@patch('agent_controller.generate_pdf')
async def test_process_request_success(mock_generate_pdf, agent_controller):
    # Arrange
    mock_generate_pdf.return_value = b"pdf_bytes"

    prompt = "Test prompt"
    title = "Test Title"

    # Act
    pdf_bytes = await agent_controller.process_request(prompt, title)

    # Assert
    assert pdf_bytes == b"pdf_bytes"
    mock_generate_pdf.assert_called_once()
    call_args = mock_generate_pdf.call_args[0][0]
    assert call_args['title'] == title
    assert len(call_args['sections']) == 1
    assert call_args['sections'][0]['type'] == 'paragraph'
    assert call_args['sections'][0]['text'] == prompt

def test_prompt_ingestor_sanitize(agent_controller):
    # Arrange
    prompt = "  Test prompt  "
    
    # Act
    sanitized_prompt = agent_controller.prompt_ingestor.sanitize(prompt)
    
    # Assert
    assert sanitized_prompt == "Test prompt"

def test_prompt_ingestor_validate_empty(agent_controller):
    # Arrange
    prompt = ""
    
    # Act & Assert
    with pytest.raises(ValueError, match="Prompt cannot be empty."):
        agent_controller.prompt_ingestor.validate(prompt)
