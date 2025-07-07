import streamlit as st

# In-memory storage
wallets = {}

# Create User
def create_user(name):
    if name in wallets:
        return False
    wallets[name] = 0.0
    return True

# Add Money
def add_money(name, amount):
    if name in wallets:
        wallets[name] += amount
        return True
    return False

# Get Balance
def get_balance(name):
    return wallets.get(name, None)

# Transfer Money
def transfer_money(sender, receiver, amount):
    if sender in wallets and receiver in wallets:
        if wallets[sender] >= amount:
            wallets[sender] -= amount
            wallets[receiver] += amount
            return True
    return False

# Streamlit UI
st.title("💰 E-Wallet App")

menu = st.sidebar.selectbox("Menu", ["Create User", "Add Money", "Check Balance", "Transfer"])

if menu == "Create User":
    username = st.text_input("Enter username")
    if st.button("Create"):
        if create_user(username):
            st.success(f"User {username} created!")
        else:
            st.error("User already exists!")

elif menu == "Add Money":
    username = st.text_input("Username")
    amount = st.number_input("Amount", min_value=0.0, step=0.5)
    if st.button("Add"):
        if add_money(username, amount):
            st.success(f"{amount} added to {username}")
        else:
            st.error("User not found")

elif menu == "Check Balance":
    username = st.text_input("Username to check balance")
    if st.button("Check"):
        balance = get_balance(username)
        if balance is not None:
            st.info(f"Balance: {balance}")
        else:
            st.error("User not found")

elif menu == "Transfer":
    sender = st.text_input("Sender")
    receiver = st.text_input("Receiver")
    amount = st.number_input("Amount", min_value=0.0, step=0.5)
    if st.button("Transfer"):
        if transfer_money(sender, receiver, amount):
            st.success(f"Transferred {amount} from {sender} to {receiver}")
        else:
            st.error("Transfer failed. Check users or balance.")

