import pytest
from telegram import User, Message
from telegram.ext import ContextTypes
from main import start, button_handler, send_message  # Імпортуйте ваші функції
from datetime import datetime
@pytest.fixture
def mock_context():
    class MockContext:
        bot = None
    return MockContext()

@pytest.fixture
def mock_update():
    class MockUpdate:
        message = None
        callback_query = None
    return MockUpdate()

# Тест для функції /start
def test_start(mock_update, mock_context):
    mock_update.message = Message(
        message_id=1,
        chat=None,
        text='/start',
        from_user=User(id=1, first_name='TestUser', is_bot=False),
        date=datetime.now()  # Додано date
    )

# Тест для функції send_message
def test_send_message(mock_update, mock_context):
    mock_update.message = Message(
        message_id=1,
        chat=None,
        text='/send 1 Hello',
        from_user=User(id=2, first_name='Tester', is_bot=False),
        date=datetime.now()  # Додано date
    )
