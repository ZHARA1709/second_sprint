try:
    import guess_number
except ImportError:
    raise AssertionError('Модуль `guess_number` не обнаружен.')

EXPECTED_FUNC_NAME = 'say_hello'

def test_say_hello_exists():
    assert hasattr(guess_number, EXPECTED_FUNC_NAME), (
        f'Функция `{EXPECTED_FUNC_NAME}` не обнаружена в модуле `practicum`')

def test_say_hello_run_without_exceptions():
    try:
        guess_number.say_hello()
    except Exception as error:
        raise AssertionError(
            f'При запуске функции `{EXPECTED_FUNC_NAME}` возникло '
            f'исключение: {type(error).__name__}: {error}`'
        )