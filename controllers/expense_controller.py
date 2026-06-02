from database.connection import get_db

def add_expense(user_id, data):
    category_id = data.get("category_id")
    amount      = data.get("amount")
    description = data.get("description", "")
    date        = data.get("date")

    if not category_id or not amount or not date:
        return {"message": "category_id, amount, and date are required"}, 400

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO expenses (user_id, category_id, amount, description, date) VALUES (?, ?, ?, ?, ?)",
        (user_id, category_id, amount, description, date)
    )
    conn.commit()
    conn.close()

    return {"message": "Expense added successfully"}, 201


def get_expenses(user_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT expenses.id, categories.name AS category, expenses.amount,
               expenses.description, expenses.date
        FROM expenses
        JOIN categories ON expenses.category_id = categories.id
        WHERE expenses.user_id = ?
    """, (user_id,))
    expenses = cursor.fetchall()
    conn.close()

    result = []
    for exp in expenses:
        result.append({
            "id":          exp["id"],
            "category":    exp["category"],
            "amount":      exp["amount"],
            "description": exp["description"],
            "date":        exp["date"]
        })

    return result, 200


def delete_expense(user_id, expense_id):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM expenses WHERE id = ? AND user_id = ?",
        (expense_id, user_id)
    )
    expense = cursor.fetchone()

    if expense is None:
        conn.close()
        return {"message": "Expense not found"}, 404

    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()

    return {"message": "Expense deleted successfully"}, 200
