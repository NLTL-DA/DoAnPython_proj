from catalog.models import Category, Ingredient, MenuItem, Inventory

def get_inventory_stats():
    total = Ingredient.objects.count()
    out_of_stock = Ingredient.objects.filter(quantity=0).count()
    low_stock = Ingredient.objects.filter(
        quantity__lte=3,
        quantity__gt=0
    ).count()

    return {
        "total": total,
        "out_of_stock": out_of_stock,
        "low_stock": low_stock,
    }