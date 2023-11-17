
from flask import request

from src.api.models.base_response import BaseResponse
from src.api.models.dto.watchlist.watchlist_request_dto import WatchlistRequestDto
from src.api.models.dto.watchlist.watchlist_response_dto import WatchlistResponseDto
from src.services.watchlist_service import WatchlistService


def initialize_watchlist_routes(app, socketio):

    @app.route('/api/watchlist', methods=['POST'])
    def create_watchlist():
        watchlist_request_dto: WatchlistRequestDto = WatchlistRequestDto.parse_obj(
            request.get_json()
        )
        watchlist_service = WatchlistService(socketio)

        watchlist = watchlist_service.create_watchlist(watchlist_request_dto)
        watchlist_response_dto = WatchlistResponseDto.create(watchlist)
        return BaseResponse.create_response(message='Watchlist is created', data=watchlist_response_dto)
