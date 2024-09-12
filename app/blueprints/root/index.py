from flask import Blueprint, render_template, request, session

name = "index"
bp = Blueprint(name, __name__, static_folder="static", template_folder="templates", static_url_path="/", url_prefix="/")

@bp.route("/", methods=["GET"])
def index_root():
    
    template_name = "/root/index.html"
    return render_template(
        template_name
    )

@bp.route("/support", methods=["GET"])
def support():
     template_name = '/root/support.html'

     return render_template(
          template_name
     )

@bp.route("/create", methods=["GET"])
def create():
     template_name = '/root/create.html'

     return render_template(
          template_name
     )