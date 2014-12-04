"""
Copyright (c) 2014 Dan Obermiller

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

You should have received a copy of the MIT License along with this program.
If not, see <http://opensource.org/licenses/MIT>
"""

import itertools
import os
import tempfile
import unittest

from Chemistry import compounds
from Chemistry.parsing.mol import molv3000


class test_MolV3000(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls): pass
    
    @classmethod
    def tearDownClass(cls): pass    
    
    def setUp(self): pass
    
    def tearDown(self): pass


class test_MolV3000Parser(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls): pass
    
    @classmethod
    def tearDownClass(cls): pass    
    
    def setUp(self): pass
    
    def tearDown(self): pass
    
    
class test_MolV3000Builder(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls): pass
    
    @classmethod
    def tearDownClass(cls): pass    
    
    def setUp(self): pass
    
    def tearDown(self): pass
    
    
if __name__ == '__main__':
    import types
    import sys
    
                          
    test_classes_to_run = [value for key, value in globals().items()
                           if (isinstance(value, (type, types.ClassType)) and
                               issubclass(value, unittest.TestCase))]
                               
    loader = unittest.TestLoader()
    big_suite = unittest.TestSuite(loader.loadTestsFromTestCase(test_class) 
                                   for test_class in test_classes_to_run)
                                   
    runner = unittest.TextTestRunner(sys.stdout, verbosity=1)
    runner.run(big_suite)
