# wearShop - Online Clothing Store

Welcome to wearShop, a user-friendly online clothing store built with Django and Tailwind CSS. wearShop allows users to browse, search, add items to their cart, and complete purchases with ease.

## Features

- **Browse and Search**: Explore various clothing categories and find items by name or description.
- **Shopping Cart**: Add items to the cart and manage quantities.
- **Order Placement**: Complete purchases with an intuitive checkout process.
- **Responsive Design**: Optimized for both desktop and mobile devices.

## Technologies Used

- **Backend**: [Django](https://www.djangoproject.com/)
- **Frontend**: [Tailwind CSS](https://tailwindcss.com/)
- **Database**: SQLite3

## Installation

### Prerequisites

- Python 3.7 or higher
- Pip (Python package installer)
- Virtualenv (recommended)

### Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/wearshop.git
    cd wearshop
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```sh
    python manage.py migrate
    ```

5. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

6. **Access the application**:
    Open your browser and navigate to `http://127.0.0.1:8000`.

## Usage

1. **Browse products**: Use the search bar or browse through categories to find clothing items.
2. **Add to cart**: Select items and add them to your shopping cart.
3. **Manage cart**: Adjust quantities or remove items from your cart.
4. **Checkout**: Complete the order by providing shipping and payment details.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact us at [lyarov22@gmail.com].

---

Thank you for using wearShop. Happy shopping!
