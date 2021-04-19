import os
import shutil

working_directory_path = "D:\\"
working_directory_files_list = os.listdir(working_directory_path)
categories = {
    "Images": ["jpg", "jpeg", "jiff", "png", "tif", "tiff", "gif", "eps", "bmp", "raw", "cr2", "nef", "orf", "sr2", "ai", "ico", "psd", "svg"],
    "Documents": ["doc", "docx", "tex", "wpd", "odt", "pdf", "txt", "rtf"],
    "Videos": ["3g2", "3gp", "avi", "flv", "h264", "m4v", "mov", "mp4", "mpg", "mpeg", "rm", "swf", "vob", "wmv", "mkv", "webm"],
    "Audio": ["aif", "cda", "mid", "midi", "mp3", "mpa", "ogg", "wav", "wma", "wpl"],
    "Applications": ["apk", "bat", "bin", "cgi", "pl", "com", "exe", "gadget", "jar", "msi", "wsf"],
    "Spreadsheets": ["ods", "xls", "xlsm", "xlsx"],
    "Presentation": ["key", "odp", "pps", "ppt", "pptx"],
    "Compressed": ["7z", "arj", "deb", "pkg", "rar", "rpm", "gz", "z", "zip"]
}


def get_file_category(file_ext):
    for category in categories:
        if file_ext in categories[category]:
            return category
    return None


for file_name in working_directory_files_list:
    if not os.path.isfile(os.path.join(working_directory_path, file_name)):
        print(f"Found a folder: {file_name}, continuing anyway")
        continue
    file_extension = file_name.split('.')[-1]
    category_type = get_file_category(file_extension)
    if not category_type:
        print(f"Invalid file type found for file: {file_name}")
        continue
    category_path = os.path.join(working_directory_path, category_type)
    if not os.path.exists(category_path):
        os.mkdir(category_path)
    source_file_path = os.path.join(working_directory_path, file_name)
    destination_file_path = os.path.join(category_path, file_name)
    """
    Possible ways to do this:
        destination_file_path = os.path.join(category_path, file_name)
        destination_file_path = os.path.join(working_directory_path, category_path).join(file_name)
        destination_file_path = os.path.join(working_directory_path).join(category_path).join(file_name)
        destination_file_path = f"{working_directory_path}\\{category_path}\\{file_name}"
    """
    shutil.move(source_file_path, destination_file_path)
