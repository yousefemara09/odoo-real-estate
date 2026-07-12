import json
import math
from urllib.parse import parse_qs
from odoo import http
from odoo.http import request


def valid_response(data , pagination_info, status):
    data_comeback = {
        'data' : data
    }
    if pagination_info:
        data_comeback['pagination_info'] = pagination_info
    return request.make_json_response(data_comeback ,status=status)


def invalid_reject_response(error , status):
    data_comeback_error = {
        'Error' : error
    }
    return request.make_json_response(data_comeback_error, status=status)

print("Controller Loaded")
class PropertyApi(http.Controller):

    @http.route(['/v1/property'], methods=['POST'] ,  auth='none' ,  type='http' ,csrf=False)
    def property_create_api_post(self):
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        if not vals.get('name'):
               return request.make_json_response({
                   "message":"Name is required",
               }, status=400)
        try:
           result = request.env['property'].sudo().create(vals)
           if result:
               return request.make_json_response({
                   "message": "Property added successfully",
                   "property_id": result.id,
               }, status=200)
        except Exception as error:
            return request.make_json_response({
                "message": str(error)
            }, status=500)
#######################################################################################################
#######################################Create Data Bu SQL##############################################
    # @http.route(['/v1/property'], methods=['POST'], auth='none', type='http', csrf=False)
    # def property_create_api_post(self):
    #     args = request.httprequest.data.decode()
    #     vals = json.loads(args)
    #     if not vals.get('name'):
    #         return request.make_json_response({
    #             "message": "Name is required",
    #         }, status=400)
    #     try:
    #         cr = request.env.cr
    #         columes = ', ' .join((vals.keys()))
    #         values =', ' .join(['%s'] * len(vals))
    #         query = f"""
    #                     INSERT INTO property ({columes})
    #                     VALUES ({values})
    #                     RETURNING id, postcode;
    #                  """
    #         cr.execute(query, tuple(vals.values()))
    #         result = cr.fetchone()
    #         print(result)
    #         if result:
    #             return request.make_json_response({
    #                 "message": "Property added successfully",
    #                 "property_id": result[0],
    #                 "postcode": result[1],
    #             }, status=200)
    #     except Exception as error:
    #         return request.make_json_response({
    #             "message": str(error)
    #         }, status=500)

################################################################################################
################################################################################################

    # @http.route(['/v1'], methods=['POST'] ,  auth='none' ,  type='json' ,csrf=False)
    # def property_create_api_post_http(self):
    #     args = request.httprequest.data.decode()
    #     vals = json.loads(args)# بحول من json ل dec
    #     result = request.env['property'].sudo().create(vals)
    #     if result:
    #         return {
    #             "message": "Property added successfully",
    #         }
######################################################################################################################
    # @http.route(['/v1/property/<int:property_id>'], methods=['PUT'], auth='public', type='http', csrf=False)
    # def property_api_update(self, property_id):
    #     try:
    #         property_rec = request.env['property'].sudo().search([('id', '=', property_id)])
    #         if not property_rec:
    #             return request.make_json_response({
    #                 "message": "Property Id Not Found",
    #             }, status=404)
    #         args = request.httprequest.data.decode()
    #         vals = json.loads(args)
    #         if not vals.get('bedrooms'):
    #             return request.make_json_response({
    #                 "message": "Property Don't Have Bedrooms",
    #             }, status=400)
    #         property_rec.write(vals)
    #         return request.make_json_response({
    #             "message": "Property Updated",
    #             "name": property_rec.name
    #         })
    #     except Exception as e:
    #         return request.make_json_response({
    #             "message": str(e),
    #         }, status=400)
######################################################################################################################
    @http.route(['/v1/property/<int:property_id>'], methods=['GET'], auth='public', type='http', csrf=False)
    def property_read_api(self, property_id):
        try:
            property_rec = request.env['property'].sudo().browse(property_id)

            if not property_rec.exists():
                return request.make_json_response({
                    "message": "Property ID not found",
                }, status=404)

            return valid_response(
                {
                    "message": "Property Retrieved Successfully",
                    "name": property_rec.name,
                    "postcode": property_rec.postcode,
                    "bedrooms": property_rec.bedrooms,
                },
                status=200,
                pagination_info=None
            )

        except Exception as e:
            return invalid_reject_response(
                str(e),
                status=400
            )
######################################################################################################################
    # @http.route(['/v1/property/<int:property_id>'], methods=['DELETE'], auth='public', type='http', csrf=False)
    # def property_delete_api(self, property_id):
    #     try:
    #         property_id = request.env['property'].sudo().search([('id', '=', property_id)])
    #         if not property_id:
    #             return request.make_json_response({
    #                     "message": "Property ID not found",
    #             }, status=400)
    #         property_id.unlink()
    #         return request.make_json_response({
    #             "message": "Property Deleted Successfully",
    #         } , status=200)
    #     except Exception as error:
    #         return request.make_json_response({
    #                     "message": error,
    #                 }, status=400)
######################################################################################################################
    # @http.route(['/v1/properties'], methods=['GET'], auth='public', type='http', csrf=False)
    # def property_read_all_api(self):
    #     try:
    #         params = parse_qs(request.httprequest.query_string.decode('utf-8'))
    #         domain_filters =[]
    #         if params.get('state'):
    #             domain_filters += (['state', '=' , params.get('state')[0]])
    #         property_ids = request.env['property'].sudo().search([domain_filters] )
    #         print(property_ids)
    #         if not property_ids:
    #             return request.make_json_response({
    #                     "message": "There are no properties available.",
    #             }, status=400)
    #         return request.make_json_response([{
    #             "message": "Property Updated",
    #             "name": property_id.name,
    #             "postcode": property_id.postcode,
    #             "bedrooms": property_id.bedrooms,
    #        } for property_id in property_ids ], status=200)
    #
    #     except Exception as error:
    #         return request.make_json_response({
    #                     "message": error,
    #                 }, status=400)

    # @http.route(['/v1/properties'], methods=['GET'], auth='public', type='http', csrf=False)
    # def property_read_all_api(self):
    #     try:
    #         params = parse_qs(request.httprequest.query_string.decode('utf-8'))
    #         page = offset = None
    #         limit = 3
    #         if params:
    #             if params.get('limit'):
    #                 limit = int(params.get('limit')[0])
    #             if  params.get('page') :
    #                 page = int(params.get('page')[0])
    #             if page :
    #                 offset = (limit *  page) - limit
    #         property_ids = request.env['property'].sudo().search([], offset=offset, limit=limit, order='id DESC')
    #         property_ids_count = request.env['property'].sudo().search_count([])
    #         print(property_ids)
    #         print(property_ids_count)
    #         if not property_ids:
    #             return request.make_json_response({
    #                 "message": "There are no properties available.",
    #             }, status=400)
    #         return valid_response([{
    #             "message": "Property Updated",
    #             "name": property_id.name,
    #             "postcode": property_id.postcode,
    #             "bedrooms": property_id.bedrooms,
    #         } for property_id in property_ids], pagination_info={
    #             'page': page if page else 1,
    #             'limit': limit,
    #             'pages': math.ceil(property_ids_count/limit) if limit else 1,
    #             'counts': property_ids_count,
    #         }, status=200)
    #
    #     except Exception as error:
    #         return request.make_json_response({
    #             "message": error,
    #         }, status=400)
######################################################################################################################

