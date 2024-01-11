My Real estate management project is a comprehensive Python Django application with PostgreSQL as the database. It comprises three main apps: AuthenticationApp, SellerApp, and UserApp.

AuthenticationApp:

- Handles user signup, login, and verification.
- - Collects necessary documents during signup to streamline future verifications.
- Ensures secure authentication for users.

SellerApp:

- Enables admin operations through Django admin.
- - Manages property listing and updates.
- Property profiles include details like name, address, location, features, rates, and availability.
- - Each property has multiple units categorized by type (1BHK, 2BHK, etc.).
- Admin can view property profiles , assigned tenants, and unit details through the different models , all it is registered in the admin site

UserApp:

- - Manages user-related functionalities, including property booking.
- Implements a booking management module for assigning tenants to units.
- - Allows searching based on unit and property features like rate, location, and type.

Overall, my project exhibits strong features for user authentication, property listing, and booking management. The modular structure with distinct apps enhances the maintainability and scalability of the system.
