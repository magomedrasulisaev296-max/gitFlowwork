from typing import Any
from src.decorators import log


@log()
def test_func() -> str:
    return "ok"


def test_log_works(capsys: Any) -> None:
    """Просто проверяем что декоратор вообще работает"""
    result = test_func()
    captured = capsys.readouterr()

    assert "test_func started" in captured.out
    assert "test_func finished" in captured.out
    assert result == "ok"