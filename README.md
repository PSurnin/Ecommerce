# The scheme
Main models are:
Items - options of what can be ordered, can be picked to be an OrderItem, can be created by User
OrderItem - num of Item_id belonging to new Order
Order - Choice of items by User

User - user
Payment - payment info for stripe?

# The models
Item has:
  - name
  - description
  - price
  - image
  - category_id
  - owner_id
  - quantity (available)
  - created_at

Category has:
    - id
    - name
    - created_at(?)

Order has: 
    - id
    - status
    - user_id
    - created_at

OrderItem has:
    - product_id
    - amount
    - order_id


User has:
    - login
    - password
    - email
    - username
    - is_active
    - last_login
    - is_superuser
    - is_staff
    - date_joined


## Interactions

Item
ItemCategory
OrderItem
Order


Item and ItemCategory:
1. Created
2. Updated
3. Deleted
4. Loaded

OrderItem:
1. Pick
    - if currentOrder is None - create new currentOrder
    - if currentOrder - add to currentOrder
2. Remove
    - if currentOrder and it has OrderItem - change amount
    - if no currentOrder - no OrderItem, cant remove
    
Order:
1. Get all OrderItems in Order
2. Go to payment
3. Remove Order


OrderItem is created -> It checks for existing order_id? Creates new Order if not get_object
When orderItem is validated -> checks for Item quantity -> does