def get_filename(filename, request):
    filename = str(datetime.now().strftime("%Y%m%d%H%M%S"))+filename
    return filename.upper()