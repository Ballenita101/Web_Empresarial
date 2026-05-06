from werkzeug.utils import secure_filename # pyright: ignore[reportMissingImports]

ALLOWED_EXTENSIONS = {'pdf', 'docx', 'txt' , 'xlsx' , 'txt'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    