from functions.get_files_info import get_file_info

def main():
    working_directory = 'calculator'
    root_content = get_file_info(working_directory)
    print(f"Root Content : {root_content}")
    child_content = get_file_info(working_directory, 'pkg')
    print(f"Child Content : {child_content}")
    child_content = get_file_info(working_directory, '/bin')
    print(f"Child Content : {child_content}")
    child_content = get_file_info(working_directory, '../bin')
    print(f"Child Content : {child_content}")
    
main()