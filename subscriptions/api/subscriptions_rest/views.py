import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from .encoders import (
    ProductInventoryVoEncoder,
    ProductBoxEncoder,
    ClothingInventoryVOEncoder,
    ClothingBoxEncoder,
    ReceiptEncoder,
    SubscriptionEncoder,
    UserEncoder
)

from subscriptions_rest.models import (
    ProductInventoryVO,
    ClothingInventoryVO,
    ClothingBox,
    ProductsBox,
    Receipt,
    Subscription,
    User
)

# Create your views here.

@require_http_methods(["GET"])
def api_user_token(request):
    if "jwt_access_token" in request.COOKIES:
        token = request.COOKIES["jwt_access_token"]
        if token:
            return JsonResponse({"token": token})
    response = JsonResponse({"token": None})
    return response

@require_http_methods(['GET', 'POST'])
def users_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        return JsonResponse(
            {'users': users},
            encoder=UserEncoder
        )
    else:
        content = json.loads(request.body)
        user = User.objects.create_user(**content)
        return JsonResponse(
            user,
            encoder=UserEncoder,
            safe=False
        )

@require_http_methods(['GET', 'DELETE'])
def user_details(request, pk):
    if request.method == 'GET':
        user = User.objects.get(id=pk)
        return JsonResponse(
            user,
            encoder=UserEncoder,
            safe=False
        )
    else:
        count, _ = User.objects.filter(id=pk).delete()
        return JsonResponse({"deleted": count > 0})

@require_http_methods(['GET'])
def product_inventory_vo_list(request):
    if request.method == "GET":
        product_inventory_vos = ProductInventoryVO.all()
        return JsonResponse(
            {"product_inventory_vos": product_inventory_vos},
            encoder=ProductInventoryVoEncoder
        )

@require_http_methods(['GET', 'POST'])
def product_box_list(request):
    if request.method == "GET":
        product_boxes = ProductsBox.objects.all()
        return JsonResponse(
            {"product_boxes": product_boxes},
            encoder=ProductBoxEncoder
        )
    else:
        try:
            content = json.loads(request.body)
            content = {
                **content,
                'product_box': ProductsBox.objects.get(pk=content['product_box'])
            }
            product_box = ProductsBox.objects.create(**content)
            return JsonResponse(
                product_box,
                encoder=ProductBoxEncoder,
                safe=False
            )
        except:
            response = JsonResponse(
                {"message": 'Could not create product box'}
            )
            return response

@require_http_methods(['GET', 'DELETE'])
def product_boxes_detail(request, pk):
    if request.method == 'GET':
        product_box = ProductsBox.objects.get(id=pk)
        return JsonResponse(
            product_box,
            encoder=ProductBoxEncoder,
            safe=False
        )
    else:
        if request.method == "DELETE":
            count, _ = ProductsBox.objects.filter(id=pk).delete()
            return JsonResponse({"deleted": count > 0})

@require_http_methods(['GET', 'POST'])
def subscriptions_list(request):
    if request.method == 'GET':
        subscriptions = Subscription.objects.all()
        return JsonResponse(
            {"subscriptions": subscriptions},
            encoder=SubscriptionEncoder)
    else:
        content = json.loads(request.body)
        content = {
            **content,
            'user': User.objects.get(pk=content['user']),
            'products': ProductsBox.objects.get(pk=content['product']),
            'clothing': ClothingBox.objects.get(pk=content['clothing'])
        }
        subscription = Subscription.objects.create(**content)
        return JsonResponse(
            {'subscription': subscription},
            encoder=SubscriptionEncoder,
            safe=False
        )

@require_http_methods(['GET'])
def clothing_inventory_vo_list(request):
    if request.method == 'GET':
        clothing_inventory_vos = ClothingInventoryVO.objects.all()
        return JsonResponse(
            {'clothing_inventory_vos' : clothing_inventory_vos},
            encoder=ClothingInventoryVOEncoder
        )

@require_http_methods(['GET','POST'])
def clothing_box_list(request):
    if request.method == 'GET':
        clothing_boxes = ClothingBox.objects.all()
        return JsonResponse(
            {'clothing_box': clothing_boxes},
            encoder=ClothingBoxEncoder
        )
    else:
        content = json.loads(request.body)

        try:
            clothing_box = ClothingBox.objects.get(id=content['clothing_box'])
            content['clothing_box'] = clothing_box
        except ClothingBox.DoesNotExist:
            return JsonResponse(
                {'message': "invalid id"},
                status=400,
            )

        clothing_box = ClothingBox.objects.create(**content)
        return JsonResponse(
            encoder=ClothingBoxEncoder,
            safe=False
        )

@require_http_methods(['GET','DELETE'])
def clothing_box_detail(request, pk):
    if request.method == 'GET':
        try:
            clothing_box = ClothingBox.objects.get(id=pk)
            return JsonResponse(clothing_box, encoder=ClothingBoxEncoder, safe=False)
        except ClothingBox.DoesNotExist(clothing_box):
            response = JsonResponse({"message": "Does not exist"})
            response.status_code = 404
            return response
    else:
        count, _ = ClothingBox.objects.filter(id=pk).delete()
        return JsonResponse({"deleted": count > 0})


@require_http_methods(['GET', 'DELETE'])
def show_receipt(request, pk):
    if request.method == 'GET':
        try:
            receipt = Receipt.objects.get(id=pk)
            return JsonResponse(receipt, encoder=ReceiptEncoder, safe=False)
        except Receipt.DoesNotExist(receipt):
            response = JsonResponse({"message": "Does not exist"})
            response.status_code = 404
            return response
    else:
        count, _ = receipt.objects.filter(id=pk).delete()
        return JsonResponse({"deleted": count > 0})

@require_http_methods(['GET', 'POST'])
def receipts_list(request):
    if request.method == 'GET':
        receipts = Receipt.objects.all()
        return JsonResponse(
            {'receipts': receipts},
            encoder=ReceiptEncoder
        )
    else:
        try:
            content = json.loads(request.body)
            receipt = Receipt.objects.create(**content)
            return JsonResponse(
                receipt,
                encoder=ReceiptEncoder,
                safe=False,
            )
        except:
            response = JsonResponse(
                {"message": "Could not generate receipt"}
            )
            response.status_code = 400
            return response