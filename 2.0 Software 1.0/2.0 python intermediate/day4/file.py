# def read_simple_file():
#     """demonstrate basic file reading"""
#     file = open("sample.txt", "r")
#     print(f"here is the file i want to read: {file}")
#     content=file.read()
#     print(f"Here is the content of the file read: {content}")
#     file.close
#     return content
# read_simple_file()
# def read_simple_text():
#     with open("sample.txt", "r") as file:
#         content=file.read()
#         print(f"content is : {content}")
#     return content    
# # read_simple_text()
# def read_simple_file():
#     try:
#         with open("sample.txt", "r") as file:
#            content=file.read() 
#            return content
#     except FileNotFoundError:
#         return "file not found dude, please try again"    
# def line_by_line():
#     filename="sampletxt"
#     try:
#         with open(filename, "r") as file:
#             print("\n\nreading line by line")
#             for i, line in enumerate(file, 1):
#                 print(f"\n\nline {i}: {line.strip()}")
#     except FileNotFoundError:
#         pass

