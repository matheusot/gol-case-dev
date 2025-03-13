from flask import jsonify
from flask_login import login_required
from app.models.market import Market
from . import markets_bp

@markets_bp.route('/markets', methods=['GET'])
@login_required
def markets():
    markets = Market.query.with_entities(Market.id, Market.market)
    markets_list = [{'id': market.id, 'market': market.market} for market in markets]
    return jsonify(markets_list)