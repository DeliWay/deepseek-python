import json
import markdown
import autopep8

def format_json(raw_json: str) -> str:
    """Форматирует JSON с отступами."""
    try:
        parsed = json.loads(raw_json)
        return json.dumps(parsed, indent=4, ensure_ascii=False)
    except json.JSONDecodeError:
        return "Ошибка: Невалидный JSON!"

def format_markdown(text: str) -> str:
    """Конвертирует Markdown в HTML."""
    return markdown.markdown(text)

def format_python_code(code: str) -> str:
    """Форматирует Python-код по PEP8."""
    return autopep8.fix_code(code)