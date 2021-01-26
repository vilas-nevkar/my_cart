# My Cart
-------------------------------------------------------------------------------------------
# How to run?
-------------------------------------------------------------------------------------------
1. Run `cli.py -h` to get the help
2. Run the `cli.py` with `python cli.py -m migrate` to create the database
3. Run `cli.py` again to create admin and standard user as follows
4. `python cli.py -u admin -p admin -n Admin -e admin@mycart.com`
5. `-u` is the username `-p` is the password `-n` is the name of user and `-e` is the email of the user
6. Run `cli.py` again to create the one user as follows
7. `python cli.py -u vilas -p vilas -n Vilas -e vilas@mycart.com`
8. Now run the `main.py` to start the app and login with admin credentials
9. Perform admin activity and logout, then login with user for next set of activity.


# Points to remember
------------------------------------------------------------------------------------------
1. Login with admin first and add category
2. Add product (you can choose product category from list)
3. Repeat above steps for number of products you want to add.
4. Admin can't place orders
5. User carts won't be visible until user adds something to his/her cart.
6. Order bills won't be visible until there is an order placed by user.
7. Users can browse categories and products interactively.
8. Products can be added to the cart from product detail page only
9. When user confirmed his/her order product cart will be flushed and no longer be available for admin to view.
10. When user complete his/her order checkout only then admin can view the bills generated.
 
