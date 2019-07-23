Customer: </br>
//-id PK,</br>
-Firstname</br>
-Lastname,</br>
-store_id default= 0</br>
line_id</br>
profile_img</br>

</br></br></br></br>
address</br>
one to many address</br>
cus_id</br>
-address,</br>
-district</br>
-city</br>
-country  default thai</br>
-provice</br>
-zipcode</br>
-phone,</br>
-email,</br>
-store_id default= 0</br>

</br></br></br></br>
class Shipping_method</br>
- condition_name // weight , price, item</br>
- country</br>
- condition_from_value  //decimal</br>
- condition_to_value   </br>
</br></br>
แยก class</br>
- - delivery_type</br>
        -id</br>
        -name</br>

 //ems flash</br>
- provinces_code</br>


</br></br></br></br>
-payment_method</br>
        id </br>
        payment_type</br>
        order_id // one to one field</br>

</br></br></br></br>
Order:</br>
-id PK,</br>
-status</br>
-created_at</br>
-updated_at</br>
-customerID -> Customer.ID</br>
-address,</br>
-tambon</br>
-city</br>
-provice</br>
-zipcode</br>
-productID -> product.ID</br>
-productdesc => Seliriel: productId, qty, productName, finalPrice</br>
-weight</br>
-increment_id</br>
-subtotal</br>


</br></br></br></br>
-shipping_method</br>
-shipping_amount</br>
-grand_total</br>
-store_id //ให้ FIX เป็น 0 ไปก่อน</br>
</br></br></br></br>

Product:</br>
-id PK,</br>
-name,</br>
-price,</br>
-code,</br>
-description,</br>
-qty</br>
-weight</br>
-store_id //ให้ FIX เป็น 0 ไปก่อน