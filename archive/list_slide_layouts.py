from pptx import Presentation

presentation = Presentation('templates/Consulting_Template.pptx')
layout_names = []

for slide_master in presentation.slide_masters:
    for slide_layout in slide_master.slide_layouts:
        layout_names.append(slide_layout.name)

for layout_name in layout_names:
    print(layout_name)
