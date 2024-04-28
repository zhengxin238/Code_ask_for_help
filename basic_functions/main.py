from tests import mergingTestForNineMethods
from pymongo import MongoClient
import calcultionScreenshots

db = MongoClient('localhost', 27017)['linux_temp']

file_path = r"D:\TU Clausthal\Masterarbeit\Code\tests\soc_urls_1.txt"

mergingTestForNineMethods.readURL_test_data(db, file_path)



