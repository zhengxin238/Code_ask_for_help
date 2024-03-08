from tests import mergingTestForNineMethods
from pymongo import MongoClient





# with open(file_path, 'r') as file:
#     # Iterate through each line in the file
#     for line in file:
#         # Remove leading and trailing whitespace from the line
#         line = line.strip()
#
#         # Process the line (e.g., print it)
#         print(line)


def getUrl(file_path):

    with open(file_path, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Remove leading and trailing whitespace from the line
            line = line.strip()

            # Process the line (e.g., print it)
            print(line)
    return None


# file_path = r"D:\data_collections_preflib\soc_urls_p1_21.txt"
# # getUrl(file_path)
#
# # Input file path
# input_file = r"D:\data_collections_preflib\soc_urls_p1_21.txt"
# # Output file path
# output_file = r"D:\data_collections_preflib\soc_urls_p1_21r.txt"
#
# # Read input file and process URLs
# with open(input_file, "r") as f:
#     urls = [line.strip() for line in f]
#
# # Process URLs and write to output file
# with open(output_file, "w") as f:
#     for url in urls:
#         # Add 'r' prefix and double quotes to the URL
#         modified_url = f'r"{url}"\n'
#         # Write modified URL to output file
#         f.write(modified_url)