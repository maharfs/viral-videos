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


# Simulated in-memory DB
wallets = {}

st.button("/create", methods=["POST"])
def create_user():
    data = request.get_json()
    username = data.get("username")

    if username in wallets:
        return jsonify({"status": "fail", "message": "User already exists"}), 400
    
    wallets[username] = 0.0
    return jsonify({"status": "success", "message": f"User '{username}' created!"})

st.button("/add", methods=["POST"])
def add_money():
    data = request.get_json()
    username = data.get("username")
    amount = data.get("amount", 0.0)

    if username not in wallets:
        return jsonify({"status": "fail", "message": "User not found"}), 404
    
    wallets[username] += amount
    return jsonify({"status": "success", "balance": wallets[username]})

st.button("/balance/<username>", methods=["GET"])
def get_balance(username):
    if username not in wallets:
        return jsonify({"status": "fail", "message": "User not found"}), 404
    
    return jsonify({"status": "success", "balance": wallets[username]})

st.button("/transfer", methods=["POST"])
def transfer():
    data = request.get_json()
    sender = data.get("from")
    receiver = data.get("to")
    amount = data.get("amount", 0.0)

    if sender not in wallets or receiver not in wallets:
        return jsonify({"status": "fail", "message": "Sender or receiver not found"}), 404

    if wallets[sender] < amount:
        return jsonify({"status": "fail", "message": "Insufficient funds"}), 400

    wallets[sender] -= amount
    wallets[receiver] += amount
    return jsonify({"status": "success", "message": f"{amount} transferred from {sender} to {receiver}"})


if __name__ == "__main__":
    streamlit run your_script.py


