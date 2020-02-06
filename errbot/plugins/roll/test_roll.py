pytest_plugins = ["errbot.backends.test"]

extra_plugin_dir = '.'

def test_roll(testbot):
    testbot.push_message('!roll 2d20')
    assert '^(\\d{1,2}\\s)+$' in testbot.pop_message()
    #testbot.assertInCommand('!roll 1d20','^(\\d{2}\\s)+$')
    #assert re.match('^(\\d{1,2}\\s)+$', testbot.pop_message())
