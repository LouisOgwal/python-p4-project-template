# Apple Store Manager
Apple Store Manager is a full-stack web application that allows users to manage Apple product inventory, store locations, and pricing. The application is built using React for the frontend and Flask for the backend, with PostgreSQL as the database.

## Features
- **Product Management**: Add, view, and delete Apple products.
- **Store Management**: Add, view, and delete store locations.
- **Store-Product Relations**: Assign products to stores with pricing details.
- **Serialization**: Data is structured and transferred efficiently using Marshmallow.
- **API Endpoints**: RESTful API with CRUD operations for products, stores, and store-product relationships.
- **CORS Handling**: 
# Backend:
- Python
- Flask
- Flask-RESTful
- Flask-SQLAlchemy
- Flask-Marshmallow
- PostgreSQL (or SQLite for development)
- Flask-CORS

# Frontend:
- React
- React Router
- Fetch API for consuming Flask endpoints

 Backend Setup:
  
 Install dependencies:
  
   pip install
Set up the database:
   python seed.py

 Run the Flask application:
   python app.py

### Frontend Setup:
   frontend
Install dependencies:

   npm install
    Start the React
   npm start
  

## API Endpoints

 GET, /products | Get all products |
 POST, /products | Create a new product |
 DELETE, | /products/:id | Delete a product |
 GET, /stores | Get all stores |
 DELETE, | /stores/:id | Delete a store |
 POST,/store_products | Add a product to a store with price |

# Deployment
- Frontend: Deployed on Vercel
- Backend: Deployed on Render

# Future Improvements
- Implement authentication and role-based access for admin users.
- Add product filtering and sorting options in the frontend.
- Implement unit tests for backend endpoints.
- Integrate payment processing for store purchases.

-Louis Ogwal - Developer



