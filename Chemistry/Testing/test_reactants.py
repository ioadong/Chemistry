# Copyright (c) 2014 Dan Obermiller
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# You should have received a copy of the MIT License along with this program.
# If not, see <http://opensource.org/licenses/MIT>

import unittest

from Chemistry.base.compounds import Compound
from Chemistry.base.reactants import Reactant, Acid, Base
from Chemistry.reactions.base_reactions import Conditions


class TestReactantUtilityMethods(unittest.TestCase):

    def setUp(self):
        self.compound1 = Compound(
                                {"a1":"H", "a2":"O"},
                                {"b1":("a1", "a2", {'order': 1,
                                                    'chirality': None})},
                                {"id":"Hydroxide"})
        self.compound2 = Compound(
                                {"a1":"H", "a2":"H", "a3":"O", "a4":"H"},
                                {"b1":("a1", "a3", {'order': 1,
                                                    'chirality': None}),
                                 "b2":("a2", "a3", {'order': 1,
                                                    'chirality': None}),
                                 "b3":("a3", "a4", {'order': 1,
                                                    'chirality': None})},
                                {"id":"Hydronium"})
        self.acid1 = Acid(self.compound2, 'a1', -1.74)
        self.base1 = Base(self.compound1, 'a2', 16)

    def test_new_key1(self):
        self.assertEqual('a3', Reactant._new_key(self.compound1))

    def test_new_key2(self):
        self.assertEqual('a5', Reactant._new_key(self.acid1))

    def test_new_key3(self):
        self.assertEqual('b2', Reactant._new_key(self.base1, False))

    def test_make_base_1(self):
        self.assertEqual(
            self.base1, Reactant.make_Base(self.compound1, 'a2', 16))

    def test_make_base_2(self):
        self.assertIs(self.base1, Reactant.make_Base(self.base1, 'a2', 16))

    def test_make_acid_1(self):
        self.assertEqual(
            self.acid1, Reactant.make_Acid(self.compound2, 'a1', -1.74))

    def test_make_acid_2(self):
        self.assertIs(self.acid1, Reactant.make_Acid(self.acid1, 'a1', -1.74))


class TestBase(unittest.TestCase):

    def setUp(self):
        self.compound1 = Compound(
                                {"a1":"H", "a2":"O"},
                                {"b1":("a1", "a2", {'order': 1,
                                                    'chirality': None})},
                                {"id":"Hydroxide"})
        self.compound2 = Compound(
                                {"a1":"H", "a2":"H", "a3":"O", "a4":"H"},
                                {"b1":("a1", "a3", {'order': 1,
                                                    'chirality': None}),
                                 "b2":("a2", "a3", {'order': 1,
                                                    'chirality': None}),
                                 "b3":("a3", "a4", {'order': 1,
                                                    'chirality': None})},
                                {"id":"Hydronium"})
        self.compound3 = Compound(
                                {'a1':'H', 'a2':'O', 'a3':'H'},
                                {'b1':('a1', 'a2', {'order':1,
                                                    'chirality':None}),
                                 'b2':('a2', 'a3', {'order':1,
                                                    'chirality':None})},
                                {'id':"Water"})

        self.acid = Acid(self.compound2, 'a1', -1.74)
        self.base = Base(self.compound1, 'a2', 16)
        self.conj_acid = Acid(self.compound3, 'a3', 16)
        self.conditions = Conditions({})

    def test_to_conjugate_Acid(self):
        self.assertEqual(self.base.to_conjugate_acid(), self.conj_acid)


if __name__ == '__main__':
    from . import helper
    helper(globals())