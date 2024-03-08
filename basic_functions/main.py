from tests import mergingTestForNineMethods
from pymongo import MongoClient

db = MongoClient('localhost', 27017)['DataTest_Voting']
# mergingTestForNineMethods.runTestAll(r"https://www.preflib.org/static/data/agh/00009-00000001.soc",  db['all_methods_00009-00000001'])

# mergingTestForNineMethods.runTestAll(r"https://www.preflib.org/static/data/agh/00009-00000002.soc",
#                                      db['all_methods_00009-00000002'])

mergingTestForNineMethods.runTestAll(r"https://www.preflib.org/static/data/netflix/00004-00000001.soc",
                                     db['all_methods_00004-00000001'])
# file_path = r"D:\data_collections_preflib\soc_urls_p1_21.txt"

# with open(file_path, 'r') as file:
#     # Iterate through each line in the file
#     for line in file:
#         # Remove leading and trailing whitespace from the line
#         line = line.strip()
#         parts = line.split('/')
#         # Get the last part of the URL (the filename)
#         filename = parts[-1]
#         # Remove the '.soc' extension
#         filename_without_extension = filename.split('.')[0]
#         # Extract the desired substring
#         substring = filename_without_extension.split('-')[1]
#
#         mergingTestForNineMethods.runTestAll(line,db[substring])







mergingTestForNineMethods.runTestAll(r"https://www.preflib.org/static/data/netflix/00004-00000002.soc",
                                     db['all_methods_00004-00000002'])

