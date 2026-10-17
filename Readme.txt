Little Lemon Capstone Project - API Endpoints

1. Home Page (Static HTML):
   http://127.0.0.1:8000/restaurant/

2. User Registration & Authentication (Djoser):
   - User Registration (POST): http://127.0.0.1:8000/auth/users/
   - Login & Obtain Token (POST): http://127.0.0.1:8000/auth/token/login/
   - Obtain Auth Token Alternate (POST): http://127.0.0.1:8000/restaurant/api-token-auth/

3. Menu Items API:
   - List & Create Menu Items (GET, POST): http://127.0.0.1:8000/restaurant/menu/
   - Single Menu Item (GET, PUT, PATCH, DELETE): http://127.0.0.1:8000/restaurant/menu/<int:pk>/

4. Table Booking API (Requires Token Authentication Header: "Token <YOUR_TOKEN>"):
   - List & Create Bookings (GET, POST): http://127.0.0.1:8000/restaurant/booking/tables/
   - Single Booking (GET, PUT, PATCH, DELETE): http://127.0.0.1:8000/restaurant/booking/tables/<int:pk>/

5. Admin Panel:
   http://127.0.0.1:8000/admin/