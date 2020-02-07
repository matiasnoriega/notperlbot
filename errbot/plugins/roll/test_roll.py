import re
pytest_plugins = ["errbot.backends.test"]

extra_plugin_dir = '.'


def test_roll(testbot):
    testbot.push_message('!roll 2d20')
    test_value = re.compile('^(\\d{1,2}\\s*)+$')
    assert test_value.match(testbot.pop_message())
