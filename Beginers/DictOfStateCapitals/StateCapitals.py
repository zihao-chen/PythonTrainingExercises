"""We have an existing dictionary that maps US states to their capitals.

1. Print the state capital of Idaho
2. Print all states.
3. Print all capitals.
4. Create a single string 'Alabama -> Montgomery, Alaska -> Juneau, ...'
5. Ensure the string you created in 4. is alphabetically sorted by state
7. Now we want to add the reverse look up, given the name of a capital what state
is it in?

Implement the function def get_state(capital): below so it returns the state.

GOTCHAS: What happens if two states have the same capital name, how do you
handle that?

Created on 3 Mar 2015

@author: paulross
"""
import unittest

import pytest

STATES_CAPITALS = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'Saint Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne',
}

CAPITALS_STATES = {c: s for s, c in STATES_CAPITALS.items()}


def capital_of_Idaho():
    return STATES_CAPITALS['Idaho']


def all_states():
    return list(STATES_CAPITALS.keys())


def all_capitals():
    # Your code here
    return [v for _, v in STATES_CAPITALS.items()]


def states_capitals_string():
    # Your code here
    return ", ".join([s + ' -> ' + c for s, c in STATES_CAPITALS.items()])


def get_state(capital):
    return CAPITALS_STATES[capital]


class TestDictOfStateCapitals(unittest.TestCase):
    def test_basic(self):
        print(all_states())
        print(all_capitals())
        print(states_capitals_string())

    def test_state_to_capital(self):
        assert 'Cheyenne' == STATES_CAPITALS['Wyoming']

    def test_state_to_capital_unknown(self):
        with pytest.raises(KeyError) as err:
            _ = STATES_CAPITALS['']
        assert err

    def test_capital_to_state(self):
        assert 'Wyoming' == get_state('Cheyenne')

    def test_capital_to_state_unknown(self):
        with pytest.raises(KeyError) as err:
            get_state('')
        assert err
