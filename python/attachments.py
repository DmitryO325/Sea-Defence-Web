import mimetypes
import os
from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.base import MIMEBase


def process_attachments(msg, attachments):
    for file in attachments:
        if os.path.isfile(file):
            attach_file(msg, file)
        elif os.path.exists(file):
            dir = os.listdir(file)
            for attached_file in dir:
                attach_file(msg, file + '/' + attached_file)


def attach_file(msg, file):
    attach_types = {
        'text': MIMEText,
        'image': MIMEImage,
        'audio': MIMEAudio,
    }
    filename = os.path.basename(file)
    ftype, encoding = mimetypes.guess_type(file)
    if ftype is None or encoding is not None:
        ftype = 'appliction/octet-stream'
    main_type, sub_type = ftype.split('/', 1)
    with open(file, mode='rb' if main_type != 'text' else 'r') as rec_file:
        if main_type in attach_types:
            file = attach_types[main_type](rec_file.read(), _subtype=sub_type)
        else:
            file = MIMEBase(main_type, sub_type)
            file.set_payload(rec_file.read())
            encoders.encode_base64(file)
    file.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(file)