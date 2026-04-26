from django.shortcuts import render
from catalog.service.catalog_service import get_inventory_stats

def catalog(request):
    return render(request, 'catalog/catalog_page.html')

def catalog_page(request):
    stats = get_inventory_stats()

    return render(request, "catalog/catalog_page.html", {
        "total_ingredients": stats["total"],
        "out_of_stock_count": stats["out_of_stock"],
        "low_stock_count": stats["low_stock"],
    })