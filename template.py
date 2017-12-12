class Template:
    zip_name = ''
    folder_inside_zip = ''
    count_of_files_in_folder = ''
    pdf_inside_zip = ''
    txt_inside_zip = ''

    def __init__(self, zip_name, folder_inside_zip, count_of_files_in_folder, pdf_inside_zip, txt_inside_zip):
        self.zip_name = zip_name
        self.folder_inside_zip = folder_inside_zip
        self.count_of_files_in_folder = count_of_files_in_folder
        self.pdf_inside_zip = pdf_inside_zip
        self.txt_inside_zip = txt_inside_zip
