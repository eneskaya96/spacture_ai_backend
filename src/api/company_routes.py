from flask import request

from src.api.models.base_response import BaseResponse
from src.api.models.dto.company.company_request_dto import CompanyRequestDto
from src.api.models.dto.company.company_response_dto import CompanyResponseDto
from src.services.company_service import CompanyService


def initialize_company_routes(app):

    @app.route('/api/company', methods=['POST'])
    def create_company():
        company_request_dto: CompanyRequestDto = CompanyRequestDto.parse_obj(
            request.get_json()
        )
        company_service = CompanyService()

        company = company_service.create_company(company_request_dto)
        company_response_dto = CompanyResponseDto.create(company)
        return BaseResponse.create_response(message='Company created.', data=company_response_dto)

    @app.route('/api/company/<string:company_id>', methods=['GET'])
    def get_company(company_id: str):
        company_service = CompanyService()

        company = company_service.get_company_by_id(company_id)
        company_response_dto = CompanyResponseDto.create(company)
        return BaseResponse.create_response(message='Company Obtained.', data=company_response_dto)
