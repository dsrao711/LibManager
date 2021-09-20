
from flask import (render_template ,Blueprint)

bp = Blueprint('main', __name__)

@bp.route("/")
def dashboard():
    return render_template('dashboard.html')