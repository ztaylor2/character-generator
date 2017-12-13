"""Test character."""


def test_init_race():
    """Test init."""
    from character import Character
    char = Character()
    char._init_race('elf')
    assert char.magica == 10
    assert char.destruction == 10
    assert char.alteration == 10


def test_init_attr():
    """Test."""
    from character import Character
    char = Character()
    char._init_attribute('health')
    assert char.health == 10
