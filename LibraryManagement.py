import mysql.connector
from mysql.connector import Error

# Connect to the MySQL database
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',          
            password='pixel',  
            database='library_db'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Add a new book
def add_book(title, author, published_year, category):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO books (title, author, published_year, category) VALUES (%s, %s, %s, %s)"
            values = (title, author, published_year, category)
            cursor.execute(query, values)
            connection.commit()
            print("Book added successfully")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()
#search by category
def search_books_by_category(category):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM books WHERE category = %s"
            cursor.execute(query, (category,))
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    print(row)
            else:
                print("No books found in this category.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()


# Add a new member
def add_member(name, email):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO members (name, email) VALUES (%s, %s)"
            values = (name, email)
            cursor.execute(query, values)
            connection.commit()
            print("Member added successfully")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

# Record a transaction
def record_transaction(book_id, member_id, transaction_date, return_date=None):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO transactions (book_id, member_id, transaction_date, return_date) VALUES (%s, %s, %s, %s)"
            values = (book_id, member_id, transaction_date, return_date)
            cursor.execute(query, values)
            connection.commit()
            print("Transaction recorded successfully")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

# Update book details
def update_book(book_id, title=None, author=None, published_year=None):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            updates = []
            values = []
            if title:
                updates.append("title = %s")
                values.append(title)
            if author:
                updates.append("author = %s")
                values.append(author)
            if published_year:
                updates.append("published_year = %s")
                values.append(published_year)
            
            if not updates:
                print("No updates provided")
                return
            
            values.append(book_id)
            query = f"UPDATE books SET {', '.join(updates)} WHERE book_id = %s"
            cursor.execute(query, tuple(values))
            connection.commit()
            print("Book updated successfully")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

# Delete a book
def delete_book(book_id):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "DELETE FROM books WHERE book_id = %s"
            cursor.execute(query, (book_id,))
            connection.commit()
            print("Book deleted successfully")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

# Delete a member
def delete_member(member_id):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "DELETE FROM members WHERE member_id = %s"
            cursor.execute(query, (member_id,))
            connection.commit()
            print("Member deleted successfully")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

# Return a book
def return_book(transaction_id, return_date):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "UPDATE transactions SET return_date = %s WHERE transaction_id = %s"
            cursor.execute(query, (return_date, transaction_id))
            connection.commit()
            print("Book returned successfully")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

# View all transactions
def view_transactions():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM transactions"
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

# Query all books
def query_books():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM books"
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

# Query all members
def query_members():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM members"
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

# Main function to demonstrate functionalities
def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Record Transaction")
        print("4. Update Book Details")
        print("5. Delete Book")
        print("6. Delete Member")
        print("7. Return Book")
        print("8. View Transactions")
        print("9. Query Books")
        print("10. Query Members")
        print("11. Search Books by Category")
        print("12. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            published_year = input("Enter published year: ")
            category = input("Enter book category (e.g., Story, Research): ")
            add_book(title, author, published_year, category)
        elif choice == '2':
            name = input("Enter member name: ")
            email = input("Enter member email: ")
            add_member(name, email)
        elif choice == '3':
            book_id = int(input("Enter book ID: "))
            member_id = int(input("Enter member ID: "))
            transaction_date = input("Enter transaction date (YYYY-MM-DD): ")
            record_transaction(book_id, member_id, transaction_date)
        elif choice == '4':
            book_id = int(input("Enter book ID to update: "))
            title = input("Enter new title (leave blank to keep current): ")
            author = input("Enter new author (leave blank to keep current): ")
            published_year = input("Enter new published year (leave blank to keep current): ")
            category = input("Enter new category (leave blank to keep current): ")
            update_book(book_id, title, author, published_year, category)
        elif choice == '5':
            book_id = int(input("Enter book ID to delete: "))
            delete_book(book_id)
        elif choice == '6':
            member_id = int(input("Enter member ID to delete: "))
            delete_member(member_id)
        elif choice == '7':
            transaction_id = int(input("Enter transaction ID: "))
            return_date = input("Enter return date (YYYY-MM-DD): ")
            return_book(transaction_id, return_date)
        elif choice == '8':
            view_transactions()
        elif choice == '9':
            query_books()
        elif choice == '10':
            query_members()
        elif choice == '11':
            category = input("Enter category to search (e.g., Story, Research): ")
            search_books_by_category(category)
        elif choice == '12':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
