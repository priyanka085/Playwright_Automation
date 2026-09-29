from utils.config import access_token, book_url

def test_books_api(playwright):
    request = playwright.request.new_context(base_url=book_url)

    response = request.get("/status")
    assert response.status == 200
    print(f"Response status: {response.status}")

            
    response = request.post(f"/orders/", headers={"Authorization": f"Bearer {access_token}"}, data={"bookId": 1, "customerName": "Priy Sahoo"})
    assert response.status == 201

    response = request.get("/orders", headers={"Authorization": f"Bearer {access_token}"})
    order_id = 0
    for order in response.json():
        print(f"Book ID: {order['bookId']}, Customer Name: {order['customerName']}")
        order_id = order['id']
     
    UpdatedCustName = "Tony Stark"
    response = request.patch(f"/orders/{order_id}", headers={"Authorization": f"Bearer {access_token}"}, data={"customerName": UpdatedCustName})
    assert response.status == 204
    print("Customer name updated successfully.")

    response = request.get(f"/orders/{order_id}", headers={"Authorization": f"Bearer {access_token}"})
    assert response.status == 200
    print("Order details:", response.json())

    response = request.delete(f"/orders/{order_id}", headers = {"Authorization" : f"Bearer {access_token}"})
    assert response.status == 204
    print("Order deleted successfully.")

    response = request.get(f"/orders/{order_id}", headers={"Authorization": f"Bearer {access_token}"})
    if response.status == 404:
        print("Order not found")

    request.dispose()