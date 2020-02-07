pytest_plugins = ["errbot.backends.test"]

extra_plugin_dir = '.'


def test_tryme(testbot):
    testbot.push_message('!tryme')
    assert 'It works !' in testbot.pop_message()