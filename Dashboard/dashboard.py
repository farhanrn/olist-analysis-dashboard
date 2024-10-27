import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Olist Dashboard", 
    page_icon="src/favicon.ico",
    layout="wide")

# Initialize session state for the selected page
if 'selected_page' not in st.session_state:
    st.session_state.selected_page = "Introduction"

# Custom CSS to style the sidebar
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #f0f2f5;  /* Light gray background */
        padding: 20px;              /* Padding around the sidebar */
        border-radius: 10px;        /* Rounded corners */
    }
    .sidebar .sidebar-content h1 {
        font-size: 24px;            /* Larger font size for titles */
    }
    .sidebar .sidebar-content button {
        font-size: 16px;            /* Button font size */
        padding: 10px;              /* Button padding */
        width: 100%;                /* Full width buttons */
        margin-bottom: 10px;        /* Space between buttons */
        background-color: #4CAF50;  /* Green background */
        color: white;               /* White text */
        border: none;               /* No border */
        border-radius: 5px;        /* Rounded corners */
        cursor: pointer;            /* Pointer cursor on hover */
    }
    .sidebar .sidebar-content button:hover {
        background-color: #45a049;  /* Darker green on hover */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create a sidebar for navigation
#st.sidebar.title("Navigation")
st.sidebar.image("/src/olist.png", use_column_width=True)  # Add logo image
st.sidebar.markdown("### 📊 Dashboard Sections")

# Create a list of pages for easier management
pages = {
    "🏠 Introduction": "Introduction",
    "📈 Revenue Analysis" : "Revenue Analysis",
    "🛒 Order Analysis" : "Order Analysis",
    "🛍️ Product Analysis":"Product Analysis",
    "🧑‍💼 Seller Analysis": "Seller Analysis",
    "⭐ Review Analysis": "Review Analysis",
    "👥 Customer Segmentation Analysis": "Customer Segmentation Analysis",
}

# Create buttons dynamically from the pages dictionary
for page_name, page in pages.items():
    if st.sidebar.button(page_name):
        st.session_state.selected_page = page

# Load the selected page based on session state
if st.session_state.selected_page == "Introduction":
    from dashboard_pages import intro
    intro.main()
elif st.session_state.selected_page == "Revenue Analysis":
    from dashboard_pages import revenue
    revenue.main()
elif st.session_state.selected_page == "Order Analysis":
    from dashboard_pages import order
    order.main()
elif st.session_state.selected_page == "Product Analysis":
    from dashboard_pages import product
    product.main()
elif st.session_state.selected_page == "Seller Analysis":
    from dashboard_pages import seller
    seller.main()
elif st.session_state.selected_page == "Review Analysis":
    from dashboard_pages import review
    review.main()
elif st.session_state.selected_page == "Customer Segmentation Analysis":
    from dashboard_pages import customer
    customer.main()

# footer 
st.sidebar.markdown("---")
st.sidebar.write("© Farhan Rahman")
