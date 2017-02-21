class Submission:

    entity_name = ''
    zip_name = False
    folder_name = False
    txt_inside_folder = False
    pdf_inside_folder = False

    def __init__(self, entity_name, zip_name, folder_name, txt_inside_folder, pdf_inside_folder):

        self.entity_name = entity_name
        self.zip_name = zip_name
        self.folder_name = folder_name
        self.txt_inside_folder = txt_inside_folder
        self.pdf_inside_folder = pdf_inside_folder
