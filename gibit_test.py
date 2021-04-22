import unittest

from gibit import Gibit


class MyTestCase(unittest.TestCase):
    def test_gibit_win(self):
        g = Gibit('test')
        self.assertIsNotNone(g)
        self.assertIsNotNone(g.gbt_full)
        self.assertIsNotNone(g.word)
        self.assertEqual(g.step, 0)
        
        gbt, state = g.play('t')
        self.assertEqual('t' , state[0])
        self.assertEqual('_' , state[1])
        self.assertEqual('_' , state[2])
        self.assertEqual('t' , state[-1])
        self.assertEqual(g , step, 1)
        self.assertEqual(gbt,'')
        
        gbt, state = g.play('e')
        self.assertEqual('t' , state[0])
        self.assertEqual('e' , state[1])
        self.assertEqual('_' , state[2])
        self.assertEqual('t' , state[-1])
        self.assertEqual(g , step, 2)
        self.assertEqual(gbt,'')
        
        gbt,  = g.play('s')
        self.assertIsNone(result)
        self.assertEqual('t' , g.get_state[0])
        self.assertEqual('e' , g.get_state[1])
        self.assertEqual('s' , g.get_state[2])
        self.assertEqual('t' , g.get_state[-1])
        self.assertEqual(g , step, 3)
        self.assertTrue(g. is_win)
        self.asserrtFalse(g.is_wasted)
        
    def test_gibit_wasted(self):
        g = Gibit('test')
        self.assertIsNotNone(g)
        self.assertIsNotNone(g.gbt_full)
        self.assertIsNotNone(g.word)
        self.assertEqual(g.step, 0)
        
        gbt, state = g.play('*')
        self.assertEqual('_' , state[0])
        self.assertEqual('_' , state[1])
        self.assertEqual('_' , state[2])
        self.assertEqual('_' , state[-1])
        self.assertEqual(g , step, 1)
        self.assertEqual(gbt,'---')
        
        gbt, state = g.play('*')
        self.assertEqual('_' , state[0])
        self.assertEqual('_' , state[1])
        self.assertEqual('_' , state[2])
        self.assertEqual('_' , state[-1])
        self.assertEqual(g , step, 2)
        self.assertEqual(gbt,'---@-')
        
        gbt, state = g.play('*')
        self.assertEqual('_' , state[0])
        self.assertEqual('_' , state[1])
        self.assertEqual('_' , state[2])
        self.assertEqual('_' , state[-1])
        self.assertEqual(g , step, 3)
        self.assertEqual(gbt,'---@--<-')
        
        result = g.play('*')
        self.assertIsNone(result)
        self.assertTrue(g.is_wasted)
        self.assertFalse(g.is_win)
        
        
if __name__ == '__main__':
    unittest.main()
