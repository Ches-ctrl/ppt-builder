import shutil
from pptx import Presentation

source_file = 'templates/Consulting_Template_2.pptx'
destination_file = 'outputs/Copied_File.pptx'

shutil.copy(source_file, destination_file)

presentation = Presentation('outputs/Copied_File.pptx')

layout_names = []

for slide_master in presentation.slide_masters:
    for slide_layout in slide_master.slide_layouts:
        layout_names.append(slide_layout.name)

for layout_name in layout_names:
    print(layout_name)
