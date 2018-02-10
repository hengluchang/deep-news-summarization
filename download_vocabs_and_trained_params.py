import requests

def download_file_from_google_drive(id, destination):
    """
    code based on
    https://stackoverflow.com/questions/25010369/wget-curl-large-file-from-google-drive/39225039#39225039
    """
    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value

        return None

    def save_response_content(response, destination):
        CHUNK_SIZE = 32768

        with open(destination, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)

    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)


if __name__ == "__main__":
    import sys
    if len(sys.argv) is not 2:
        print ("Usage: python download_vocabs_and_trained_params.py destination_folder")
    else:
        # TAKE ID FROM SHAREABLE LINK
        file_ids = {'checkpoint': '10QMbXbnT3w7sbIu2CEQ8UtTFBlEaPpnH',
                    'seq2seq.ckpt-75600': '1or3xvDhHXh3ZkZ-WY13VNA0gzm0vEjDR',
                    'vocab80000_dec.txt': '1ZuSVrkHlb33CdgxAhPO-p_8rw2fS6Qzk',
                    'vocab80000_enc.txt': '1HeVaFax6dJbiTY0FV55g4oKowjv10q4O'}

        # DESTINATION FILE ON YOUR DISK
        destination_folder = sys.argv[1]
        for file_name, file_id in file_ids.items():
            destination = destination_folder + '/' + file_name
            print ('Downloading {} ...'.format(file_name))
            download_file_from_google_drive(file_id, destination)

        print ('Finished downloading vocabs and trained parameters to {}.'.format(destination_folder))
