import datetime as dt

from flask import jsonify

from app.core.cfg import cfg
from app.routes.route_blueprints import api_liveness_blueprint

__author__ = 'kclark'

bp = api_liveness_blueprint

@bp.route('/liveness', methods=['GET'])
def handle_liveness_get_req():
    result = {
        'app_env': cfg.app_env,
        'app_start_time': cfg.app_start_time.isoformat(),
        'response_time': dt.datetime.utcnow().isoformat()
    }

    return jsonify(result)
