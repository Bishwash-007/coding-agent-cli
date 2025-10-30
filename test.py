from functions.get_files_info import get_file_info
from functions.get_files_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def main():
    working_directory = 'calculator'
    print(run_python_file(working_directory, 'lorem.txt'))
    print(run_python_file(working_directory, 'tests.py'))

main()



def test_get_file_info():
    working_directory = 'calculator'
    root_content = get_file_info(working_directory)
    print(f"Root Content : {root_content}")
    child_content = get_file_info(working_directory, 'pkg')
    print(f"Child Content : {child_content}")
    child_content = get_file_info(working_directory, '/bin')
    print(f"Child Content : {child_content}")
    child_content = get_file_info(working_directory, '../bin')
    print(f"Child Content : {child_content}")
    
    
def test_get_file_content():
    working_directory = 'calculator'
    print(get_file_content(working_directory,'lorem.txt'))
    print(get_file_content(working_directory,'main.py'))
    print(get_file_content(working_directory,'tests.py'))
    print(get_file_content(working_directory,'pkg/calculator.py'))
    print(get_file_content(working_directory,'pkg/hello.py'))
    
    
def test_write_file():
    working_directory = 'calculator'
    print(write_file(working_directory, 'lorem.txt', "This is the new code to be written in the file"))
    print(write_file(working_directory, 'hello.js', "console.log('Hello World!')"))
    print(write_file(working_directory, 'temp/test_case.js', "console.log('Test World!')"))
    print(write_file(working_directory, 'pkg/case.js', "console.log('Test World!')"))