from UI_Tests.Test_Homepage import Test_Homepage
from UI_Tests.Test_Homepage_2 import Test_Homepage_2


class Cases:
    def first_test(self):
        test = Test_Homepage()
        test.tests()

    def second_test(self):
        test = Test_Homepage_2()
        test.tests()
