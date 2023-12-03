# _Taverna Restaurant_

The goal of Taverna Restaurant's website is to captivate patrons with its pub atmosphere, emphasizing a diverse selection of beers and whiskey along with entertaining games like pool and arcades. The website aims to draw customers in by providing details on the drink offerings, gaming options, and creating an inviting space for socializing.

Visitors to the Taverna Restaurant website will encounter a user-friendly interface designed to encourage reservations, offer insights into the menu, and provide essential information such as the location and contact details. The site ensures seamless navigation, enabling users to effortlessly manage their bookings, whether it's scheduling, canceling, or updating reservation dates. While an account is required for these actions, the registration and login process is straightforward, placing emphasis on the main attraction—the delightful culinary experience at Taverna.


## Features

### Existing Features

- __Restaurant Land Page__
 
  - The homepage is crafted to captivate visitors instantly, aiming to swiftly grab attention and spark curiosity, potentially leading to reservations or a brief perusal of the menu. It boasts a well-thought-out design featuring visually enticing food images and a delightful ambiance. Navigation is seamless, facilitating easy access to crucial areas such as the menu, reservation system, and user section. The objective is to deliver a favorable and immersive initial encounter that encourages visitors to delve deeper into the restaurant. The page also includes a direct link to the reservation section, enhancing user convenience.

  ![Land Page](https://i.imgur.com/zUZzxbd.png)

- __Welcome to Taverna Section__
 
  - The "Welcome to Taverna" section enhances the user experience by presenting information in a user-friendly format. It introduces customers to their potential experiences at the restaurant, offering insights into our cuisine and the exceptional care we take of our patrons. The page also includes a direct link to the menu section, ensuring easy access to the culinary offerings.

  ![Welcome Taverna Section](https://i.imgur.com/3bvNiWz.png)

- __Menu Section__

  - The primary goal of the menu section is to captivate customers through visually striking and informative displays of our diverse food and beverage options. By providing an engaging presentation, it aims to streamline decision-making and foster enthusiasm for our culinary offerings. This section categorizes our menu into six distinct sections: starters, main courses, pizzas, desserts, drinks, and beverages. Hover over these categories to reveal detailed textual information about each menu item.

  ![Menu Section](https://i.imgur.com/zMXj9pK.png)

- __Menu Items Section__
 
  - Each menu item is succinctly described, offering key details such as price, ingredients, and flavors. This straightforward approach aims to inform and attract customers effectively.

  ![Menu Items Section](https://i.imgur.com/lIrUXpu.png)
  ![Menu Items Section Items](https://i.imgur.com/AVGtAld.png)

  - __Reservation Section__
 
    - The reservation area is designed for booking tables accommodating two, four, or six persons, providing users with a convenient experience. Although it's not explicitly mentioned initially, it's worth noting that users can book only one table at a time.

  ![Reservation Section](https://i.imgur.com/8U2mBrS.png)

- __User Page Section__
 
  - The User Page section is crafted for handling bookings and user account management. Users can perform actions such as logging out or unregistering from the site within this section.
    
  ![User Page Section](https://i.imgur.com/5HFbuqW.png)
    
  - __Log In/ Register__
 
    - The login and registration section is designed to be user-friendly and straightforward, enabling users to easily register and log in. Once registered, users are automatically logged in.

  ![Log In/ Register](https://i.imgur.com/bogCtQ5.png)

  ![Log In/ Register](https://i.imgur.com/P96uP5f.png)

  - __Models__
 
    - For this project, a single model has been created—the Reservation model. This model is tasked with linking each booking to a particular customer, ensuring there are no duplicate bookings. It also incorporates functionality to verify the availability of a table of a specified size at a given time on a particular date. Notably, the restaurant has only two tables of each size.
      - user: This establishes a one-to-one relationship with the built-in User model, creating a link between a reservation and a specific user.
      - date: Captures the date of the reservation using a DateField.
      - booking_time: Represents the chosen reservation time from a selection ranging between 2pm and 8pm
      - table_size: Signifies the selected table size for the reservation, with options for 2, 4, or 6 persons.
      - check_table_availability method: This method conducts a database query to confirm the availability of a table at a specific time and date. It returns false if two reservations already exist for the same table, indicating that the table is unavailable. Otherwise, it returns true.
      -  str method: This method creates a textual representation of a reservation, showcasing details such as booking time, date, and table size.


### Features Left to Implement

  - Enable the website administrator to receive email notifications whenever a customer makes a table reservation.
  - Online Food Purchase for Customers:
    - Empower customers to purchase their food online, incorporating:
    - Secure payment methods.
    - Options to track delivery time and location.
  - Implement a system to automatically remove outdated data every two weeks.
  - Establish a direct communication channel for customers to contact the restaurant owner.
    

## Testing

### Django Test Function
- Executed Django's built-in test function, and the code passed without any issues.

### PEP 8 Code Validation
- Validated the code using the PEP 8 code validator, ensuring adherence to coding standards.

### Manual Testing
- Conducted manual tests to simulate scenarios, such as:
  - Submitting invalid inputs.
  - Attempting to reserve tables without prior registration.
  - Checking for potential double bookings.

### Environment Testing
- Verified the code's functionality both on Heroku and the local development environment.

This thorough testing approach ensures the reliability and robustness of your code. Well done!


## Validator Testing

  ## Code Validation and Testing

### PEP8 Code Validation
No errors were encountered when the code underwent validation using the official [PEP8 validator](https://pep8ci.herokuapp.com/). The validation was performed on all files, although only the models and views were uploaded for simplicity.

#### PEP8 Views.py
![PEP8 Views](https://i.imgur.com/ICJERNp.png)

#### PEP8 Model.py
![PEP8 Model](https://i.imgur.com/PDCWRvF.png)

### Django Built-in Tests
The code passed all tests executed through Django's built-in testing framework.

![Django Test](https://i.imgur.com/K9FQS49.png)

This comprehensive validation and testing process ensures the code's adherence to coding standards and its functionality.


## Bugs

### Solved Bugs

At the project's outset, my familiarity with Django was limited, and I had to learn various concepts during its development. I sought assistance on web forums, and once I grasped the language, coding became smoother. The most challenging aspect of this project was its deployment on Heroku, requiring over 4 days to resolve issues like bad requests and broken links. Ultimately, I opted for Cloudinary for page images and White Sound for static files. Since making that decision, everything has functioned as expected.

### Remaining Bugs
  
No remaining bugs.

# Project Deployment

The project has been successfully deployed using Heroku. To deploy it yourself, follow these steps:

1. Duplicate or clone the repository to your local machine.
2. Establish a new Heroku application.
3. Adjust the deployment settings as needed.
4. Create a connection with PostgreSQL.
5. Associate your Heroku app with the repository and proceed with the deployment.

For a live demonstration, visit: [mytavernrestaurant](https://mytavernrestaurant-fcc6f699d784.herokuapp.com/)


## Credits

### Images

All images used in this project are copyright-free and sourced from [freepik.com](https://www.freepik.com/).

### Template Source Code

The source code for the template is from an open-source Bootstrap theme:
- [Bootstrap Theme](https://startbootstrap.com/theme/creative)

### Problem Solving Resources

I sought solutions to challenges during project development on various platforms:
- [Stack Overflow](https://stackoverflow.com/)
- [GeeksforGeeks](https://www.geeksforgeeks.org/)
- [freeCodeCamp](https://www.freecodecamp.org/news)
- [Medium](https://medium.com/)

### Deployment Assistance

I received support and guidance from [Code Institute](https://www.codeinstitute.net/) for the deployment process.


#### Requirements

Go to api direcotory

To make virtual environment using
```
python -m venv myenv

Activate environment
For Windows:
./myenv/Script/activate
For MACos:
source ./myenv/bin/activate
```

To install requirements type

```
pip install -r requirements.txt
```

`To use Github api put your credentials in settings.py`


To migrate the database open terminal in project directory and type

```
python manage.py makemigrations
python manage.py migrate
```

To run the program in local server use the following command

```
python manage.py runserver
```

Server will be available at `http://127.0.0.1:8000` in your browser

#### Author

<blockquote>
luizsmania1<br>
</blockquote>

========Thank You !!!=========