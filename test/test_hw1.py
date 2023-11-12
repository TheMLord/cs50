import unittest

from hw_1.task_1 import get_count_character_string
from hw_1.task_2 import get_uniq_char
from hw_1.task_3 import get_count_odd_position_five
from hw_1.task_4 import is_valid_list
from hw_1.task_5 import find_special_element


class TestHw1(unittest.TestCase):
    def test_task_1(self):
        s_1 = "abaca"
        ch_1 = "a"
        self.assertEqual(get_count_character_string(s_1, ch_1), 3)

        s_2 = "abhfjfkdddkfsdkkdlsfllfk"
        ch_2 = "m"
        self.assertEqual(get_count_character_string(s_2, ch_2), "такого элемента нет")

        s_3 = "uibyyfgwvgwyunsolmcaxhpgrstblvomwbrywdeqpccocqrapsdnamftxouwqhchouaoulttvrlkqfsynmzsozbdkvniemxlfwxrugzdmttqellrwdnlnmripllotumueuinxodvhqobnzbuatfgfuylxnsrnbwwswnavhdycsqiqtvhpuddvuepkrspwfoighkivhybqrwoeadhnzsfqbnsattpwntqxloewxbrodutgwlomgqqeupplncplycymbguuxqmlnzfqblmdgsnoqnmrnkndirsixusigftehgalzwensdkvafvsgkluqibzupzuxlofbdryefotavspeyrigscctqkofuklbeebswdroqfvcafptbnxtenkdhyzxshtgrtnpxqgotoxthtyzyqzfmodrtgltavkyfyzvoriuiobgqplgxbtpiotzmyhwyacpkhyrixubbliqyztehdrzswstlqqodpusbaarkmowsdqnwndevpribevxbeuexpfqwwmafmqzvzayzwsvizfxmvorurrnruunvdxfccbptsuevwpowgovxntlxarovlxspqemzfxfkdtunnotssqmmgmwamlqzylkozvktfefkarsuzqktrwmmgvdodofwkybylvhagtfawcuelpxovvpmspnrynhmiokhxxtblcuhzuwquxtbcvprtpemcqzaqtiimkuiyxwbmvxhypnutbypyaxqkropbfwkheggwgfiqiobbvngurugepgllgfihfbiocyglmbepfhoyuqafvnvbrmlzgfgodfruitcgmiuolnahbmvpmzcwxkokvenonuzuirxdnbbbfhflitmsbfysuklgegxeykxbmnlxyppsiksypmesxkgigwwiqaxxekkounzmixhnnqqduloyphuknctzfygkwceyalrmvhwoibgxmyngepummwbnvvrxaiebidupyushszpvgmsagempfhbvbiskewwr"
        ch_3 = "j"
        self.assertEqual(get_count_character_string(s_3, ch_3), "такого элемента нет")

        s_4 = "uibyyfgwvgwyunsolmcaxhpgrstblvomwbrywdeqpccocqrapsdnamftxouwqhchouaoulttvrlkqfsynmzsozbdkvniemxlfwxrugzdmttqellrwdnlnmripllotumueuinxodvhqobnzbuatfgfuylxnsrnbwwswnavhdycsqiqtvhpuddvuepkrspwfoighkivhybqrwoeadhnzsfqbnsattpwntqxloewxbrodutgwlomgqqeupplncplycymbguuxqmlnzfqblmdgsnoqnmrnkndirsixusigftehgalzwensdkvafvsgkluqibzupzuxlofbdryefotavspeyrigscctqkofuklbeebswdroqfvcafptbnxtenkdhyzxshtgrtnpxqgotoxthtyzyqzfmodrtgltavkyfyzvoriuiobgqplgxbtpiotzmyhwyacpkhyrixubbliqyztehdrzswstlqqodpusbaarkmowsdqnwndevpribevxbeuexpfqwwmafmqzvzayzwsvizfxmvorurrnruunvdxfccbptsuevwpowgovxntlxarovlxspqemzfxfkdtunnotssqmmgmwamlqzylkozvktfefkarsuzqktrwmmgvdodofwkybylvhagtfawcuelpxovvpmspnrynhmiokhxxtblcuhzuwquxtbcvprtpemcqzaqtiimkuiyxwbmvxhypnutbypyaxqkropbfwkheggwgfiqiobbvngurugepgllgfihfbiocyglmbepfhoyuqafvnvbrmlzgfgodfruitcgmiuolnahbmvpmzcwxkokvenonuzuirxdnbbbfhflitmsbfysuklgegxeykxbmnlxyppsiksypmesxkgigwwiqaxxekkounzmixhnnqqduloyphuknctzfygkwceyalrmvhwoibgxmyngepummwbnvvrxaiebidupyushszpvgmsagempfhbvbiskewwr"
        ch_4 = "u"
        self.assertEqual(get_count_character_string(s_4, ch_4), 52)

    def test_task_2(self):
        s_1 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabggggggggggghjj"
        self.assertEqual(get_uniq_char(s_1), 5)

        s_2 = ""
        self.assertEqual(get_uniq_char(s_2), 0)

    def test_task_3(self):
        n_1 = 52
        self.assertEqual(get_count_odd_position_five(n_1), 1)

        n_2 = 254
        self.assertEqual(get_count_odd_position_five(n_2), 0)

        n_3 = -555552
        self.assertEqual(get_count_odd_position_five(n_3), -1)

        n_4 = 557
        self.assertEqual(get_count_odd_position_five(n_4), -1)

        n_5 = 5268555572
        self.assertEqual(get_count_odd_position_five(n_5), 3)

    def test_task_4(self):
        l_1 = ["ggg", "gggg", "ll", "fds", ""]
        self.assertTrue(is_valid_list(l_1))

        l_2 = ["55", "555"]
        self.assertTrue(is_valid_list(l_2))

        l_3 = ["55", 555, "3", "fdsf"]
        self.assertFalse(is_valid_list(l_3))

        l_4 = ["gg", "gh", "12", "", "88", "fdsasdf", "dfds"]
        self.assertFalse(is_valid_list(l_4))

    def test_task_5(self):
        l_1 = [1, 1441, "8778", 1331]
        self.assertEqual(find_special_element(l_1), (2, "8778"))

        l_2 = [1, 1441, 8778, 1331]
        self.assertEqual(find_special_element(l_2), ())

        l_3 = ["ака", "каак"]
        self.assertEqual(find_special_element(l_3), (1, "каак"))
