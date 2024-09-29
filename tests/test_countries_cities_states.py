from amnemone.data.countries_states_cities import Cities, Countries


def test_decode_city_names_to_ints():
    test_input = ['Prozor', 'Ştefan Cel Mare', 'Burk', 'Villalonso', 'Daganzo de Arriba']
    expected_output = [9980, 93928, 35488, 117349, 114034]

    mn = Cities()
    assert mn._decode(test_input) == expected_output


def test_encode_ints_to_city_names():
    test_input = [9980, 93928, 35488, 117349, 114034]
    expected_output = ['Prozor', 'Ştefan Cel Mare', 'Burk', 'Villalonso', 'Daganzo de Arriba']

    mn = Cities()
    assert mn._encode(test_input) == expected_output


def test_decode_country_emojis_to_ints():
    test_input = ['🇬🇦', '🇲🇼', '🇨🇻', '🇲🇾', '🇧🇮']
    expected_output = [79, 128, 39, 129, 35]

    mn = Countries(key='emoji')
    assert mn._decode(test_input) == expected_output


