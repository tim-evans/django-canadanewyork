import StringIO

from PIL import Image
from reportlab.pdfgen import canvas

from django.core.files.uploadedfile import InMemoryUploadedFile


def django_image(name, size=10):
    thumb = Image.new('RGB', size=(size, size,))
    # Create a file-like object to write thumb data (thumb data previously created
    # using PIL, and stored in variable 'thumb')
    thumb_io = StringIO.StringIO()
    thumb.save(thumb_io, format='JPEG')

    # Create a new Django file-like object to be used in models as ImageField using
    # InMemoryUploadedFile.  If you look at the source in Django, a
    # SimpleUploadedFile is essentially instantiated similarly to what is shown here
    return InMemoryUploadedFile(thumb_io, None, name + '.jpg', 'image/jpeg',
                                thumb_io.len, None)


def django_pdf(name, text='hello world'):
    # Create a file-like object to write pdf data (pdf data previously created
    # using reportlab, and stored in variable 'pdf')
    pdf_io = StringIO.StringIO()

    pdf = canvas.Canvas(pdf_io)
    pdf.drawString(100, 100, text)

    # Create a new Django file-like object to be used in models as FileField using
    # InMemoryUploadedFile.  If you look at the source in Django, a
    # SimpleUploadedFile is essentially instantiated similarly to what is shown here
    return InMemoryUploadedFile(pdf_io, None, name + '.pdf', 'image/jpeg',
                                pdf_io.len, None)