from typing import Optional, List
from fastapi import APIRouter, Header
from fastapi.responses import Response, HTMLResponse, PlainTextResponse

router = APIRouter(prefix='/product', tags=['Product'])

products = ["watch", "camera", "laptop"]

# By default pydantic will convert the response to json
# By using the Response object we can return custom responses
# This allows us to return custom types of responses as well as attaching headers and cookies to the response
# This is useful when we want to return a file or a stream of data, html, xml, etc.
# We might also want to condtionally return a response type based on the request (xml or json)
@router.get('/all')
def get_all_products():
    data = " ".join(products)
    
    return Response(content=data, media_type="text/plain")

# custom_header is automatically converted to custom-header in the request header
@router.get('/withheader')
def get_products(response: Response, custom_header: Optional[List[str]] = Header(None)):
    response.headers['custom-response-header'] = ", ".join(custom_header)
    return products

@router.get('/{product_id}', responses={
    200: {
        "content": {
            "text/html": {
                "example": "<div>Product</div>" # This is the example response
            }
        }, 
        "description": "Returns the HTML for an object"
        }, 
    404: {
        "content": {
            "text/plain": {
                "example": "Product not available" # This is the example response
            }
        }, 
        "description": "A clear text error message"
        }}) # This is the documentation for the response
def get_product(product_id: int):
    if product_id >= len(products):
        return PlainTextResponse(content="Product not found", media_type="text/plain", status_code=404)
    else:
        product = products[product_id]
        output = f"""
        <head>
            <style>
            .product {{
                width: 500px;
                height: 500px;
                border: 2px solid red;
                background-color: #blue;
                text-align: center;
                }}
            </style>
        </head>
        <div class="product">{product}</div>
        """
        return HTMLResponse(content=output, media_type="text/html")