from tests import mergingTestForNineMethods
from pymongo import MongoClient
import calcultionScreenshots

db = MongoClient('localhost', 27017)['DataTest_Voting_10']
# mergingTestForNineMethods.runTestAll(r"https://www.preflib.org/static/data/agh/00009-00000001.soc",  db['all_methods_00009-00000001'])

# mergingTestForNineMethods.runTestAll(r"https://www.preflib.org/static/data/agh/00009-00000002.soc",
#                                      db['all_methods_00009-00000002'])

# mergingTestForNineMethods.runTestAll(r"https://www.preflib.org/static/data/netflix/00004-00000001.soc",
#                                      db['all_methods_00004-00000001'])


# mergingTestForNineMethods.runTestAll(r"https://www.preflib.org/static/data/agh/00009-00000001.soc",
#                                      db['all_methods_00009-00000001_2'])



# file_path = r"D:\TU Clausthal\Masterarbeit\Code\tests\soc_urls_p1_21.txt"

file_path = r"D:\TU Clausthal\Masterarbeit\Code\tests\soc_urls_1.txt"

mergingTestForNineMethods.readURL_test_data(db, file_path)






# mergingTestForNineMethods.runTestAll(r"https://www.preflib.org/static/data/netflix/00004-00000002.soc",
#                                      db['all_methods_00004-00000002'])

