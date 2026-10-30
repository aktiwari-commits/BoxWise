from django.shortcuts import render, get_object_or_404
from orders.models import Order
from recommendations.services import recommend_box


def dashboard(request):

    orders = Order.objects.all().order_by("-created_at")

    result = None
    selected_order_id = ""

    if request.method == "POST":

        selected_order_id = request.POST.get("order_id")

        if selected_order_id:

            order = get_object_or_404(
                Order,
                id=selected_order_id
            )

            try:
                result = recommend_box(order)

            except ValueError as error:
                result = {"error": str(error)}

    context = {
        "orders": orders,
        "result": result,
        "selected_order_id": selected_order_id,
    }

    return render(
        request,
        "recommendations/dashboard.html",
        context
    )