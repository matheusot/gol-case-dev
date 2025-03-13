from flask import request, jsonify
from flask_login import login_required
from app.models.flight import Flight
from . import flights_bp

@flights_bp.route('/flights', methods=['GET'])
@login_required
def flights():
    market_id = request.args.get('market_id')
    start_month = request.args.get('start_month')
    start_year = request.args.get('start_year')
    end_month = request.args.get('end_month')
    end_year = request.args.get('end_year')

    if not market_id:
        return {'error': 'Missing market_id'}, 400

    if start_month and start_year and end_month and end_year:
        try:
            start_month = int(start_month)
            start_year = int(start_year)
            end_month = int(end_month)
            end_year = int(end_year)
        except ValueError:
            return {'error': 'Invalid date filter params'}, 400

        flights = Flight.query.filter(
            Flight.market == market_id,
            ((Flight.year == start_year) & (Flight.month >= start_month)) |
            ((Flight.year == end_year) & (Flight.month <= end_month)) |
            ((Flight.year > start_year) & (Flight.year < end_year))
        ).with_entities(
            Flight.year, Flight.month, Flight.market, Flight.rpk
        )
    else:
        flights = Flight.query.filter(Flight.market == market_id).with_entities(
            Flight.year, Flight.month, Flight.market, Flight.rpk
        )
   
    flights_list = [{'year': flight.year, 'month': flight.month, 'market': flight.market, 'rpk': flight.rpk} for flight in flights]
    return jsonify(flights_list)