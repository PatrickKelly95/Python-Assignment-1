# Program Name: test_statistics
# Purpose: Test the functionality of the application with pytest

from pytest import approx

from stats.calculate_statistics import calc_correlation, check_list_all_numbers, calc_mean, calc_variance
from stats.country_or_club_statistics import get_sum_players_team
from stats.player_specific_statistics import get_total_amount_players, get_age_statistics, get_worst_top_players, \
    calculate_weight_stone, calculate_height_feet, get_height_weight, get_correlation_age_pace, \
    get_correlation_age_rating, get_variance_shooting, get_correlation_passing
from dataset.render_charts import web_scrap_country_codes, remove_extra_content


# Test the function get_total_amount_players()
def test_no_players():
    assert get_total_amount_players() == 20943


# Test the function get_age_statistics()
def test_age_statistics():
    assert get_age_statistics() == (27, 18, 90)


# Test the function get_worst_top_players()[0]
def test_top_rated_players():
    assert get_worst_top_players()[0] == ['Pelé', 'Ronaldo', 'Messi', 'Modric', 'Maradona']


# Test the function get_worst_top_players()[1]
def test_worst_rated_players():
    assert get_worst_top_players()[1] == ['Fujikawa', 'Ma Junliang', 'Zhang Yufeng', 'Ehlich', 'Kaltner']


# Test the function get_sum_players_team(value)[1]
def test_no_countries():
    assert get_sum_players_team("country")[1] == 156


# Test the function get_sum_players_team(value)[1]
def test_no_clubs():
    assert get_sum_players_team("club")[1] == 637


# Test the function calculate_weight_stone(value)
def test_convert_to_stone():
    assert calculate_weight_stone(70) == approx(11.018)
    assert calculate_weight_stone(95) == approx(14.953)
    assert calculate_weight_stone(67) == approx(10.5458)


# Test the function calculate_height_feet(value)
def test_convert_to_ft_in():
    assert calculate_height_feet(180) == (5, approx(10.8, 0.1))
    assert calculate_height_feet(85) == (2, approx(9.46, 0.1))
    assert calculate_height_feet(134) == (4, approx(4.75, 0.1))


# Test the function get_height_weight()[0]
def test_average_height():
    assert get_height_weight()[0] == '5ft 11.42inches'


# Test the function test_average_weight()[1]
def test_average_weight():
    assert get_height_weight()[1] == "11.9stone"


# Test the function get_correlation_age_pace()
def test_correlation_age_pace():
    assert get_correlation_age_pace() == -0.1


# Test the function get_correlation_age_rating()
def test_correlation_age_rating():
    assert get_correlation_age_rating() == 0.4


# Test the function get_correlation_passing()
def test_correlation_passing():
    assert get_correlation_passing() == 0.9


# Test the function check_list_all_numbers(values)
def test_check_list_all_numbers():
    assert check_list_all_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
    assert check_list_all_numbers([1, 2, "buckle my shoe"]) == False


# Test the function calc_mean(values)
def test_calc_mean():
    assert calc_mean([12, 13, 15, 16, 24, 15, 22, 10, 23, 24]) == 17.4
    assert calc_mean(['microsoft', 'facebook', 'oracle', 'ericsson']) is None


# Test the function calc_correlation(x_values, y_values)
def test_calc_correlation():
    assert calc_correlation([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == approx(1.0)
    assert calc_correlation(['e', 'b', 'd', 'e', 'b', 'c', 'd', 'c', 'd', 'b'],
                            ['c', 'a', 'c', 'c', 'a', 'c', 'b', 'c', 'c', 'e']) is None


# Test the function web_scrap_country_codes()
def test_world_map_codes_countries():
    assert web_scrap_country_codes() == {'ad': 'Andorra',
                                         'ae': 'United Arab Emirates',
                                         'af': 'Afghanistan',
                                         'al': 'Albania',
                                         'am': 'Armenia',
                                         'ao': 'Angola',
                                         'aq': 'Antarctica',
                                         'ar': 'Argentina',
                                         'at': 'Austria',
                                         'au': 'Australia',
                                         'az': 'Azerbaijan',
                                         'ba': 'Bosnia and Herzegovina',
                                         'bd': 'Bangladesh',
                                         'be': 'Belgium',
                                         'bf': 'Burkina Faso',
                                         'bg': 'Bulgaria',
                                         'bh': 'Bahrain',
                                         'bi': 'Burundi',
                                         'bj': 'Benin',
                                         'bn': 'Brunei Darussalam',
                                         'bo': 'Bolivia, Plurinational State of',
                                         'br': 'Brazil',
                                         'bt': 'Bhutan',
                                         'bw': 'Botswana',
                                         'by': 'Belarus',
                                         'bz': 'Belize',
                                         'ca': 'Canada',
                                         'cd': 'Congo, the Democratic Republic of the',
                                         'cf': 'Central African Republic',
                                         'cg': 'Congo',
                                         'ch': 'Switzerland',
                                         'ci': 'Cote d’Ivoire',
                                         'cl': 'Chile',
                                         'cm': 'Cameroon',
                                         'cn': 'China',
                                         'co': 'Colombia',
                                         'cr': 'Costa Rica',
                                         'cu': 'Cuba',
                                         'cv': 'Cape Verde',
                                         'cy': 'Cyprus',
                                         'cz': 'Czech Republic',
                                         'de': 'Germany',
                                         'dj': 'Djibouti',
                                         'dk': 'Denmark',
                                         'do': 'Dominican Republic',
                                         'dz': 'Algeria',
                                         'ec': 'Ecuador',
                                         'ee': 'Estonia',
                                         'eg': 'Egypt',
                                         'eh': 'Western Sahara',
                                         'er': 'Eritrea',
                                         'es': 'Spain',
                                         'et': 'Ethiopia',
                                         'fi': 'Finland',
                                         'fr': 'France',
                                         'ga': 'Gabon',
                                         'gb': 'United Kingdom',
                                         'ge': 'Georgia',
                                         'gf': 'French Guiana',
                                         'gh': 'Ghana',
                                         'gl': 'Greenland',
                                         'gm': 'Gambia',
                                         'gn': 'Guinea',
                                         'gq': 'Equatorial Guinea',
                                         'gr': 'Greece',
                                         'gt': 'Guatemala',
                                         'gu': 'Guam',
                                         'gw': 'Guinea-Bissau',
                                         'gy': 'Guyana',
                                         'hk': 'Hong Kong',
                                         'hn': 'Honduras',
                                         'hr': 'Croatia',
                                         'ht': 'Haiti',
                                         'hu': 'Hungary',
                                         'id': 'Indonesia',
                                         'ie': 'Ireland',
                                         'il': 'Israel',
                                         'in': 'India',
                                         'iq': 'Iraq',
                                         'ir': 'Iran, Islamic Republic of',
                                         'is': 'Iceland',
                                         'it': 'Italy',
                                         'jm': 'Jamaica',
                                         'jo': 'Jordan',
                                         'jp': 'Japan',
                                         'ke': 'Kenya',
                                         'kg': 'Kyrgyzstan',
                                         'kh': 'Cambodia',
                                         'kp': 'Korea, Democratic People’s Republic of',
                                         'kr': 'Korea, Republic of',
                                         'kw': 'Kuwait',
                                         'kz': 'Kazakhstan',
                                         'la': 'Lao People’s Democratic Republic',
                                         'lb': 'Lebanon',
                                         'li': 'Liechtenstein',
                                         'lk': 'Sri Lanka',
                                         'lr': 'Liberia',
                                         'ls': 'Lesotho',
                                         'lt': 'Lithuania',
                                         'lu': 'Luxembourg',
                                         'lv': 'Latvia',
                                         'ly': 'Libyan Arab Jamahiriya',
                                         'ma': 'Morocco',
                                         'mc': 'Monaco',
                                         'md': 'Moldova, Republic of',
                                         'me': 'Montenegro',
                                         'mg': 'Madagascar',
                                         'mk': 'Macedonia, the former Yugoslav Republic of',
                                         'ml': 'Mali',
                                         'mm': 'Myanmar',
                                         'mn': 'Mongolia',
                                         'mo': 'Macao',
                                         'mr': 'Mauritania',
                                         'mt': 'Malta',
                                         'mu': 'Mauritius',
                                         'mv': 'Maldives',
                                         'mw': 'Malawi',
                                         'mx': 'Mexico',
                                         'my': 'Malaysia',
                                         'mz': 'Mozambique',
                                         'na': 'Namibia',
                                         'ne': 'Niger',
                                         'ng': 'Nigeria',
                                         'ni': 'Nicaragua',
                                         'nl': 'Netherlands',
                                         'no': 'Norway',
                                         'np': 'Nepal',
                                         'nz': 'New Zealand',
                                         'om': 'Oman',
                                         'pa': 'Panama',
                                         'pe': 'Peru',
                                         'pg': 'Papua New Guinea',
                                         'ph': 'Philippines',
                                         'pk': 'Pakistan',
                                         'pl': 'Poland',
                                         'pr': 'Puerto Rico',
                                         'ps': 'Palestine, State of',
                                         'pt': 'Portugal',
                                         'py': 'Paraguay',
                                         're': 'Reunion',
                                         'ro': 'Romania',
                                         'rs': 'Serbia',
                                         'ru': 'Russian Federation',
                                         'rw': 'Rwanda',
                                         'sa': 'Saudi Arabia',
                                         'sc': 'Seychelles',
                                         'sd': 'Sudan',
                                         'se': 'Sweden',
                                         'sg': 'Singapore',
                                         'sh': 'Saint Helena, Ascension and Tristan da Cunha',
                                         'si': 'Slovenia',
                                         'sk': 'Slovakia',
                                         'sl': 'Sierra Leone',
                                         'sm': 'San Marino',
                                         'sn': 'Senegal',
                                         'so': 'Somalia',
                                         'sr': 'Suriname',
                                         'st': 'Sao Tome and Principe',
                                         'sv': 'El Salvador',
                                         'sy': 'Syrian Arab Republic',
                                         'sz': 'Swaziland',
                                         'td': 'Chad',
                                         'tg': 'Togo',
                                         'th': 'Thailand',
                                         'tj': 'Tajikistan',
                                         'tl': 'Timor-Leste',
                                         'tm': 'Turkmenistan',
                                         'tn': 'Tunisia',
                                         'tr': 'Turkey',
                                         'tw': 'Taiwan (Republic of China)',
                                         'tz': 'Tanzania, United Republic of',
                                         'ua': 'Ukraine',
                                         'ug': 'Uganda',
                                         'us': 'United States',
                                         'uy': 'Uruguay',
                                         'uz': 'Uzbekistan',
                                         'va': 'Holy See (Vatican City State)',
                                         've': 'Venezuela, Bolivarian Republic of',
                                         'vn': 'Viet Nam',
                                         'ye': 'Yemen',
                                         'yt': 'Mayotte',
                                         'za': 'South Africa',
                                         'zm': 'Zambia',
                                         'zw': 'Zimbabwe'}


# Test the function remove_extra_content(x_values)
def test_remove_extra_content():
    example_with_continents = ['Andorra', 'United Arab Emirates', 'Afghanistan', 'Albania', 'Armenia', 'Angola',
                               'Antarctica', 'Argentina', 'Austria', 'Australia', 'Azerbaijan',
                               'Bosnia and Herzegovina', 'Bangladesh', 'Belgium', 'Burkina Faso', 'Bulgaria', 'Bahrain',
                               'Burundi', 'Benin', 'Brunei Darussalam', 'Bolivia, Plurinational State of', 'Brazil',
                               'Bhutan', 'Botswana', 'Belarus', 'Belize', 'Canada',
                               'Congo, the Democratic Republic of the', 'Central African Republic', 'Congo',
                               'Switzerland', 'Cote d’Ivoire', 'Chile', 'Cameroon', 'China', 'Colombia', 'Costa Rica',
                               'Cuba', 'Cape Verde', 'Cyprus', 'Czech Republic', 'Germany', 'Djibouti', 'Denmark',
                               'Dominican Republic', 'Algeria', 'Ecuador', 'Estonia', 'Egypt', 'Western Sahara',
                               'Eritrea', 'Spain', 'Ethiopia', 'Finland', 'France', 'Gabon', 'United Kingdom',
                               'Georgia', 'French Guiana', 'Ghana', 'Greenland', 'Gambia', 'Guinea',
                               'Equatorial Guinea', 'Greece', 'Guatemala', 'Guam', 'Guinea-Bissau', 'Guyana',
                               'Hong Kong', 'Honduras', 'Croatia', 'Haiti', 'Hungary', 'Indonesia', 'Ireland', 'Israel',
                               'India', 'Iraq', 'Iran, Islamic Republic of', 'Iceland', 'Italy', 'Jamaica', 'Jordan',
                               'Japan', 'Kenya', 'Kyrgyzstan', 'Cambodia', 'Korea, Democratic People’s Republic of',
                               'Korea, Republic of', 'Kuwait', 'Kazakhstan', 'Lao People’s Democratic Republic',
                               'Lebanon', 'Liechtenstein', 'Sri Lanka', 'Liberia', 'Lesotho', 'Lithuania', 'Luxembourg',
                               'Latvia', 'Libyan Arab Jamahiriya', 'Morocco', 'Monaco', 'Moldova, Republic of',
                               'Montenegro', 'Madagascar', 'Macedonia, the former Yugoslav Republic of', 'Mali',
                               'Myanmar', 'Mongolia', 'Macao', 'Mauritania', 'Malta', 'Mauritius', 'Maldives', 'Malawi',
                               'Mexico', 'Malaysia', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Nicaragua',
                               'Netherlands', 'Norway', 'Nepal', 'New Zealand', 'Oman', 'Panama', 'Peru',
                               'Papua New Guinea', 'Philippines', 'Pakistan', 'Poland', 'Puerto Rico',
                               'Palestine, State of', 'Portugal', 'Paraguay', 'Reunion', 'Romania', 'Serbia',
                               'Russian Federation', 'Rwanda', 'Saudi Arabia', 'Seychelles', 'Sudan', 'Sweden',
                               'Singapore', 'Saint Helena, Ascension and Tristan da Cunha', 'Slovenia', 'Slovakia',
                               'Sierra Leone', 'San Marino', 'Senegal', 'Somalia', 'Suriname', 'Sao Tome and Principe',
                               'El Salvador', 'Syrian Arab Republic', 'Swaziland', 'Chad', 'Togo', 'Thailand',
                               'Tajikistan', 'Timor-Leste', 'Turkmenistan', 'Tunisia', 'Turkey',
                               'Taiwan (Republic of China)', 'Tanzania, United Republic of', 'Ukraine', 'Uganda',
                               'United States', 'Uruguay', 'Uzbekistan', 'Holy See (Vatican City State)',
                               'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Yemen', 'Mayotte', 'South Africa',
                               'Zambia', 'Zimbabwe', 'Asia', 'Europe', 'Africa', 'North America', 'South America',
                               'Oceania', 'Antartica']
    example_without_continents = ['Andorra', 'United Arab Emirates', 'Afghanistan', 'Albania', 'Armenia', 'Angola',
                                  'Antarctica', 'Argentina', 'Austria', 'Australia', 'Azerbaijan',
                                  'Bosnia and Herzegovina', 'Bangladesh', 'Belgium', 'Burkina Faso', 'Bulgaria',
                                  'Bahrain', 'Burundi', 'Benin', 'Brunei Darussalam', 'Bolivia, Plurinational State of',
                                  'Brazil', 'Bhutan', 'Botswana', 'Belarus', 'Belize', 'Canada',
                                  'Congo, the Democratic Republic of the', 'Central African Republic', 'Congo',
                                  'Switzerland', 'Cote d’Ivoire', 'Chile', 'Cameroon', 'China', 'Colombia',
                                  'Costa Rica', 'Cuba', 'Cape Verde', 'Cyprus', 'Czech Republic', 'Germany', 'Djibouti',
                                  'Denmark', 'Dominican Republic', 'Algeria', 'Ecuador', 'Estonia', 'Egypt',
                                  'Western Sahara', 'Eritrea', 'Spain', 'Ethiopia', 'Finland', 'France', 'Gabon',
                                  'United Kingdom', 'Georgia', 'French Guiana', 'Ghana', 'Greenland', 'Gambia',
                                  'Guinea', 'Equatorial Guinea', 'Greece', 'Guatemala', 'Guam', 'Guinea-Bissau',
                                  'Guyana', 'Hong Kong', 'Honduras', 'Croatia', 'Haiti', 'Hungary', 'Indonesia',
                                  'Ireland', 'Israel', 'India', 'Iraq', 'Iran, Islamic Republic of', 'Iceland', 'Italy',
                                  'Jamaica', 'Jordan', 'Japan', 'Kenya', 'Kyrgyzstan', 'Cambodia',
                                  'Korea, Democratic People’s Republic of', 'Korea, Republic of', 'Kuwait',
                                  'Kazakhstan', 'Lao People’s Democratic Republic', 'Lebanon', 'Liechtenstein',
                                  'Sri Lanka', 'Liberia', 'Lesotho', 'Lithuania', 'Luxembourg', 'Latvia',
                                  'Libyan Arab Jamahiriya', 'Morocco', 'Monaco', 'Moldova, Republic of', 'Montenegro',
                                  'Madagascar', 'Macedonia, the former Yugoslav Republic of', 'Mali', 'Myanmar',
                                  'Mongolia', 'Macao', 'Mauritania', 'Malta', 'Mauritius', 'Maldives', 'Malawi',
                                  'Mexico', 'Malaysia', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Nicaragua',
                                  'Netherlands', 'Norway', 'Nepal', 'New Zealand', 'Oman', 'Panama', 'Peru',
                                  'Papua New Guinea', 'Philippines', 'Pakistan', 'Poland', 'Puerto Rico',
                                  'Palestine, State of', 'Portugal', 'Paraguay', 'Reunion', 'Romania', 'Serbia',
                                  'Russian Federation', 'Rwanda', 'Saudi Arabia', 'Seychelles', 'Sudan', 'Sweden',
                                  'Singapore', 'Saint Helena, Ascension and Tristan da Cunha', 'Slovenia', 'Slovakia',
                                  'Sierra Leone', 'San Marino', 'Senegal', 'Somalia', 'Suriname',
                                  'Sao Tome and Principe', 'El Salvador', 'Syrian Arab Republic', 'Swaziland', 'Chad',
                                  'Togo', 'Thailand', 'Tajikistan', 'Timor-Leste', 'Turkmenistan', 'Tunisia', 'Turkey',
                                  'Taiwan (Republic of China)', 'Tanzania, United Republic of', 'Ukraine', 'Uganda',
                                  'United States', 'Uruguay', 'Uzbekistan', 'Holy See (Vatican City State)',
                                  'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Yemen', 'Mayotte', 'South Africa',
                                  'Zambia', 'Zimbabwe']
    assert remove_extra_content(example_with_continents) == example_without_continents


# Test the function calc_variance(x_values)
def test_calc_variance():
    assert calc_variance([6, 3, 8, 5, 3]) == (3.6, approx(1.89, 0.1))
    assert calc_variance([1, 3, 5, 7, 14]) == (20.0, approx(4.47, 0.1))
    assert calc_variance([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == (8.25, approx(2.87, 0.1))
    assert calc_variance(['e', 'b', 'd', 'e', 'b', 'c', 'd', 'c', 'd', 'b']) is None


# Test the function get_variance_shooting()
def test_variance_shooting_ability():
    assert get_variance_shooting() == ('518.7', '22.8')
