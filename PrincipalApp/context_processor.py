def total_carrito(request):
    total = 0
    con = 0
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                total += int(value["acumulado"])
                con += 1 
    return {"total_carrito": total,"total_items": con}