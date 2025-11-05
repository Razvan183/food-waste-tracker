import streamlit as st
import pandas as pd
from datetime import date, datetime
from db import init_db, add_item, get_all_items, delete_item

# -----------------------------------------------------------
# Initialization
# -----------------------------------------------------------
init_db()

st.set_page_config(page_title="🥦 Food Waste Tracker", layout="centered")
st.title("🥦 Food Waste Tracker")
st.write("Helping you reduce food waste by keeping an eye on expiry dates.")

# -----------------------------------------------------------
# Helper functions
# -----------------------------------------------------------
def days_until_expiry(expiry_date_str: str) -> int:
    """Calculate how many days are left until the expiry date."""
    try:
        expiry = datetime.strptime(expiry_date_str, "%Y-%m-%d").date()
        today = date.today()
        return (expiry - today).days
    except Exception:
        return None

def highlight_expiry(val):
    """Apply background color based on days left until expiry."""
    if val is None:
        return ''
    if val < 0:
        return 'background-color: #ff4d4d; color: white;'  # red
    elif val <= 3:
        return 'background-color: #ab5000;'  # orange
    else:
        return 'background-color: #00611a;'  # green

def load_data():
    """Fetch data from DB and compute days_left column."""
    items = get_all_items()
    if not items:
        return pd.DataFrame(columns=["id", "name", "category", "quantity", "location", "expiry_date", "added_at", "days_left"])
    df = pd.DataFrame(items, columns=["id", "name", "category", "quantity", "location", "expiry_date", "added_at"])
    df["days_left"] = df["expiry_date"].apply(days_until_expiry)
    df.sort_values("days_left", inplace=True)
    return df

# -----------------------------------------------------------
# Add Item Form
# -----------------------------------------------------------
st.subheader("➕ Add a Food Item")

with st.form("add_item_form", clear_on_submit=True):
    name = st.text_input("Food name *")
    category = st.selectbox("Category", ["Dairy", "Meat", "Fruit", "Vegetable", "Grain", "Snack", "Other"])
    quantity = st.text_input("Quantity (e.g. '2 pcs', '500g')")
    location = st.selectbox("Location", ["Fridge", "Freezer", "Pantry"])
    expiry_date = st.date_input("Expiry date", min_value=date.today())
    submitted = st.form_submit_button("Add item")

if submitted:
    if not name:
        st.error("Food name is required.")
    else:
        add_item(name, category, quantity, location, expiry_date.isoformat())
        st.success(f"✅ Added *{name}* (expires {expiry_date.isoformat()})")
        st.rerun()

# -----------------------------------------------------------
# Load Data
# -----------------------------------------------------------
df = load_data()

if df.empty:
    st.info("No items yet. Add something above! 🥗")
else:
    # -------------------------------------------------------
    # Expired Items
    # -------------------------------------------------------
    expired_df = df[df["days_left"] < 0]
    if not expired_df.empty:
        st.subheader("⚠️ Expired Items")
        st.dataframe(
            expired_df[["name", "category", "quantity", "location", "expiry_date", "days_left"]]
            .style.applymap(highlight_expiry, subset=["days_left"])
        )

    # -------------------------------------------------------
    # Expiring Soon
    # -------------------------------------------------------
    soon_df = df[(df["days_left"] >= 0) & (df["days_left"] <= 3)]
    st.subheader("⏰ Items Expiring Soon (≤ 3 days)")
    if not soon_df.empty:
        st.dataframe(
            soon_df[["name", "category", "quantity", "location", "expiry_date", "days_left"]]
            .style.applymap(highlight_expiry, subset=["days_left"])
        )
    else:
        st.success("No items about to expire. Nice job! 🎉")

    # -------------------------------------------------------
    # All Items
    # -------------------------------------------------------
    st.subheader("📦 All Items (sorted by expiry date)")
    st.dataframe(
        df[["id", "name", "category", "quantity", "location", "expiry_date", "days_left"]]
        .style.applymap(highlight_expiry, subset=["days_left"])
    )

# -----------------------------------------------------------
# Manage Items
# -----------------------------------------------------------
st.subheader("🗑 Manage Items")

if not df.empty:
    item_id = st.selectbox("Select an item to delete", options=df["id"], format_func=lambda x: f"ID {x} - {df.loc[df['id'] == x, 'name'].values[0]}")
    if st.button("Delete selected item"):
        delete_item(int(item_id))
        st.success(f"🗑 Deleted item with ID {int(item_id)}")
        st.rerun()
else:
    st.info("No items to manage yet.")
