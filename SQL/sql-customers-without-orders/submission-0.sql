-- Write your query below
Select name from customers where id not in (Select customer_id from orders);