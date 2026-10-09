import os
import fitz

pdf_path = 'C:/Users/Student/Downloads/Phase 3..pdf'
out_dir = 'C:/Users/Student/OneDrive - ADvTECH Ltd/XHAW APP/myapp/assets'

os.makedirs(out_dir, exist_ok=True)
doc = fitz.open(pdf_path)
count = 0

for page_index in range(doc.page_count):
    page = doc[page_index]
    images = page.get_images(full=True)
    for img_index, img in enumerate(images):
        xref = img[0]
        pix = fitz.Pixmap(doc, xref)
        if pix.n == 4:
            pix = fitz.Pixmap(fitz.csRGB, pix)
        name = f'page{page_index + 1}_{img_index}.png'
        target = os.path.join(out_dir, name)
        pix.save(target)
        pix = None
        count += 1

print(f'Extracted {count} images to {out_dir}')
