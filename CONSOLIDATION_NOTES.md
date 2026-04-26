# Django App Consolidation Summary

## What was consolidated:

### ✅ **Orders + Tables → Operations** (COMPLETED)

Combined two related apps into a single `operations` app because:
- Orders heavily depend on Tables (ForeignKey relationship)
- Reservations are also table-related
- Both manage restaurant operations (floor management + ordering)

**Files consolidated:**
```
operations/
├── models.py (combined Order, OrderItem, Table, Reservation)
├── serializers.py (combined Order, OrderItem, Table, Reservation serializers)
├── views.py (combined all ViewSets)
├── urls.py (combined all routes)
├── admin.py (combined admin configs)
├── apps.py
├── __init__.py
└── migrations/ (will be generated fresh)
```

**URL Changes:**
- `/api/orders/*` → `/api/operations/orders/*`
- `/api/order-items/*` → `/api/operations/order-items/*`
- `/api/tables/*` → `/api/operations/tables/*`
- `/api/reservations/*` → `/api/operations/reservations/*`

**Import changes made:**
- `config/settings.py`: Replaced 'orders' and 'tables' with 'operations'
- `config/urls.py`: Updated to use single 'operations.urls'
- `menu/management/commands/seed_data.py`: Updated imports to use operations

**Old apps to delete:**
- ❌ `/orders/` directory
- ❌ `/tables/` directory

---

## Optional Future Consolidations:

### ✅ **Menu + Inventory → Catalog** (COMPLETED)

Combined menu and inventory apps into a single `catalog` app because:
- MenuItem depends on Category and Ingredient
- Both manage restaurant catalog/offerings
- Reduced 2 apps into 1

**Files consolidated:**
```
catalog/
├── models.py (combined MenuItem, Category, Ingredient, Inventory)
├── serializers.py (combined MenuItemSerializer, CategorySerializer, IngredientSerializer, InventorySerializer)
├── views.py (combined MenuItemViewSet, CategoryViewSet, IngredientViewSet, InventoryViewSet)
├── urls.py (combined all routes)
├── admin.py (combined admin configs)
├── apps.py
├── __init__.py
├── management/commands/seed_data.py
└── migrations/
```

**URL Changes:**
- `/api/menu/items/*` → `/api/catalog/items/*`
- `/api/inventory/categories/*` → `/api/catalog/categories/*`
- `/api/inventory/ingredients/*` → `/api/catalog/ingredients/*`
- `/api/inventory/inventory/*` → `/api/catalog/inventory/*`

**Import changes made:**
- `config/settings.py`: Replaced 'inventory' and 'menu' with 'catalog'
- `config/urls.py`: Updated to use single 'catalog.urls'
- `operations/models.py`: Updated import from `menu.models` to `catalog.models`
- `catalog/management/commands/seed_data.py`: Updated imports to use catalog

**Old apps deleted:**
- ✅ `/menu/` directory
- ✅ `/inventory/` directory

---

### 3️⃣ **Customers + Staff → People** (or keep separate)
- Could combine into a "users" management app
- Currently less coupled, probably better kept separate

---

## Consolidation Summary:

✅ **Consolidation 1: Orders + Tables → Operations** (COMPLETED)
✅ **Consolidation 2: Menu + Inventory → Catalog** (COMPLETED)

**Current App Structure:**
- `catalog/` - Menu items, categories, ingredients, inventory
- `operations/` - Orders, tables, reservations
- `customer/` - Customer management
- `staff/` - Staff management

**Current API Endpoints:**
- `/api/catalog/categories/`
- `/api/catalog/ingredients/`
- `/api/catalog/items/`
- `/api/catalog/inventory/`
- `/api/operations/tables/`
- `/api/operations/orders/`
- `/api/operations/order-items/`
- `/api/operations/reservations/`
- `/api/customers/`
- `/api/staff/`

---

## Migration Steps (Completed):

1. ✅ New `operations` app structure created
2. ✅ All imports updated in dependent files
3. ✅ Delete old directories (orders/, tables/)
4. ✅ Run `python manage.py makemigrations`
5. ✅ Run `python manage.py migrate`
6. ✅ New `catalog` app structure created
7. ✅ All imports updated in dependent files
8. ✅ Delete old directories (menu/, inventory/)
9. ✅ Run `python manage.py makemigrations catalog`
10. ✅ Run `python manage.py migrate`
11. ✅ Test all API endpoints work correctly

---

## Files Modified:
- `config/settings.py` - Updated INSTALLED_APPS
- `config/urls.py` - Updated URL patterns
- `menu/management/commands/seed_data.py` - Updated imports

## Files Created:
- `operations/models.py`
- `operations/serializers.py`
- `operations/views.py`
- `operations/urls.py`
- `operations/admin.py`
- `operations/apps.py`
- `operations/__init__.py`
