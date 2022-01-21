
import os
import base64

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<center><a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}"><i class="fas fa-download"></i> {file_label}</a></center>'
    return href