import json
import Config as Config

from Connection.Token import Token
from Connection.Postgresql import InsertUsuarios, PostgreSql_Con, UpdateJobs
from Log import get_logger
from Models.Usuarios import Usuarios
from Utils import DatabaseUtils
from Utils.HttpUtils import HttpUtils


class UsuariosRequest(object):

    area_request_object = None

    def __init__(self):
        self.logger = get_logger(__name__)
        self.http_utils = HttpUtils.get_instance()
        self.token = Token(config.PROTECTOR_USERNAME, config.PROTECTOR_PASSWORD)

    @staticmethod
    def get_instance():
        if not UsuariosRequest.usuarios_request_object:
            UsuariosRequest.usuarios_request_object = usuariosRequest()

        return usuariosRequest.area_request_object

    @staticmethod
    def get_url_all_area(page, size):
        return f"{config.PROTECTOR_API_URL}/api/v1/area?page={str(page)}&size={str(size)}"

    def get_all_area(self, page):
        url = self.get_url_all_area(page, config.MAX_PAGE_SIZE)

        headers = {
            'authorization': "Bearer " + self.token,
            'accept-language': 'en'
        }

        return self.http_utils.get(url, headers)

    def area_request(self):
        property_ids = DatabaseUtils.get_properties_ids_from_database()

        page = 0
        total_pages = 2
        try:
            while page <= total_pages:
                response = self.get_all_area(page)

                total_pages = response['total_pages']
                self.logger.info(f"Progress {page}/{total_pages}")
                page = page + 1

                areas = response.get("content")
                self.logger.info(f"Found: {len(areas)} areas")

                if not areas:
                    continue

                data_list = list()
                for r in areas:
                    if r['property_id'] not in property_ids:
                        continue

                    coordinates = json.loads(r['geometry'])
                    data_list.append(
                        Area(
                            str(coordinates['geometry']['coordinates']), round(r['declared_area'], 2),
                            r['property_id'],
                            r['id'],
                            r['name'],
                            r['parent_region_id'],
                            r['created_at'],
                            r['deleted_at']
                        )
                    )

                if not data_list:
                    continue

                InsertArea(PostgreSql_Con('staging_v4'), objeto=data_list)

            UpdateJobs(PostgreSql_Con('dw_v4'), 'dm_area')
        except Exception as e:
            self.logger.exception(e)


if __name__ == '__main__':
    requester = AreaRequest.get_instance()
    requester.area_request()
