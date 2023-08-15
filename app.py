from flask_ckeditor import CKEditor
from flask import Flask
from main import main_bp
app=Flask("app")
app.register_blueprint(main_bp,url_prefix="/")
ckeditor=CKEditor(app)
import os
import json
with open(".json") as secret:
    secrets=json.load(secret)
app.config["UPLOAD_PATH"]=os.path.join(app.root_path,"uploads")
app.config["WTF_I18N_ENABLED"]=False
app.config["MAX_CONTENT_LENGTH"]=5*1024*1024
app.config['CKEDITOR_ENABLE_CODESNIPPET'] = True
app.secret_key=secrets["secret key"]


app.run("0.0.0.0",10086,False)
