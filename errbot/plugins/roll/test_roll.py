import re
pytest_plugins = ["errbot.backends.test"]

extra_plugin_dir = '.'


def test_roll(testbot):
    testbot.push_message('!roll 2d20')
    test_value = re.compile('^(\\d{1,2}\\s*)+$')
    assert test_value.match(testbot.pop_message())


def test_roll_string_validation1(testbot):
    testbot.push_message('!roll 2a20')
    assert "el formato es '!roll XdY', donde X es la cantidad de dados e Y la cantidad de caras" in testbot.pop_message()


def test_roll_string_validation2(testbot):
    testbot.push_message('!roll 2')
    assert "el formato es '!roll XdY', donde X es la cantidad de dados e Y la cantidad de caras" in testbot.pop_message()


def test_roll_string_validation3(testbot):
    testbot.push_message('!roll ad2')
    assert "el formato es '!roll XdY', donde X es la cantidad de dados e Y la cantidad de caras" in testbot.pop_message()


def test_roll_string_validation4(testbot):
    testbot.push_message('!roll 2da')
    assert "el formato es '!roll XdY', donde X es la cantidad de dados e Y la cantidad de caras" in testbot.pop_message()


def test_roll_caras_cero(testbot):
    testbot.push_message('!roll 2d0')
    assert "la cantidad de caras debe ser un numero distinto de 0" in testbot.pop_message()
