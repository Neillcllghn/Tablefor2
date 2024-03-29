# TABLEFOR2
## CONTENTS

* [AUTOMATED TESTING](#automated-testing)
  * [W3C Validator](#w3c-validator)
  * [W3C CSS Validator](#w3c-css-validator)
  * [JavaScript Validator](#javascript-validator)
  * [Python Validator](#python-validator)
  * [Lighthouse](#lighthouse)
* [MANUAL TESTING](#manual-testing)
  * [Testing User Stories](#testing-user-stories)
  * [Full Testing](#full-testing)
* [BUGS](#bugs)
  * [Solved Bugs](#solved-bugs)
  * [Known Bugs](#known-bugs)

Testing was ongoing throughout the entire build. During development I made use of Google Chrome Developer Tools to ensure everything was working correctly and to assist with troubleshooting when things were not working as expected.

I have gone through each page using Google Chrome Developer Tools to ensure that each page is responsive on a variety of different screen sizes and devices.

- - -

## AUTOMATED TESTING

### W3C Validator

[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the website. I have checked the HTML via direct input and also by inspecting the page source and running this through the validator.

* [Index Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftablefor2-pp4.herokuapp.com%2F) - No errors or warnings.
* [Make a Booking Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftablefor2-pp4.herokuapp.com%2Fcreate%2F) - No errors or warnings.
* [Update Booking Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftablefor2-pp4.herokuapp.com%2Fupdate%2F37) - No errors or warnings.
* [Register Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftablefor2-pp4.herokuapp.com%2Faccounts%2Fsignup%2F) - No errors or warnings.
* [Sign in Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftablefor2-pp4.herokuapp.com%2Faccounts%2Flogin%2F) - No errors or warnings.
* [Sign Out Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftablefor2-pp4.herokuapp.com%2Faccounts%2Flogout%2F) - No errors or warnings.


- - -

### W3C CSS Validator

No errors were found when passing through the official (jigsaw) validator. Link to vaildator can be found [here](https://jigsaw.w3.org/css-validator/#validate_by_input).

Image of Result:
![image](https://user-images.githubusercontent.com/109948740/235303294-3061dc2d-8409-4df0-97cb-11bc5ee34b97.png)


- - -

### JavaScript Validator

[jshint](https://jshint.com/) was used to validate the JavaScript.

![image](https://user-images.githubusercontent.com/109948740/234950008-3ffaa5b3-192b-4dfd-98b1-8d4300edd346.png)

- - -

### Python Validator

[Code Institute Python Linter](https://pep8ci.herokuapp.com/) was used to validate the python files. Please see below the results from the python files in which I had to input 

* bookings app.py - No errors or warnings.
![image](https://user-images.githubusercontent.com/109948740/234952613-5513be5c-fbba-4728-90d7-a8c7f538d6bc.png)

* tablefor2 app.py - No errors or warnings.
![image](https://user-images.githubusercontent.com/109948740/234954589-4e932e47-f12d-4f5c-931a-8f28da38d6da.png)

* forms.py - No errors or warnings.
![image](https://user-images.githubusercontent.com/109948740/234952920-aca96315-3052-41a0-b5f9-6ef3a1ecb239.png)

* models.py - No errors or warnings.
![image](https://user-images.githubusercontent.com/109948740/234953170-4e1cd007-724f-4194-b037-5ebda304cf3a.png)

* urls.py - No errors or warnings.
![image](https://user-images.githubusercontent.com/109948740/234953459-aecf26e8-ef1c-45cf-8272-b75ebe56ad2a.png)

* views.py - No errors or warnings.
![image](https://user-images.githubusercontent.com/109948740/234953636-e56121cf-ec03-4dee-ab08-7c858638745a.png)

- - -

### Lighthouse

We used Lighthouse within the Chrome Developer Tools to test the performance, accessibility, best practices and SEO of the website.

Overall, the lighthouse scores are very good, with one thing that could be improved.
### Desktop Results

Home Page:

![image](https://user-images.githubusercontent.com/109948740/234960792-30d716a7-75a1-40cb-a622-8920887e3107.png)

Make a Booking Page:

![image](https://user-images.githubusercontent.com/109948740/234961740-0106a242-3676-4bd9-ac0e-206b8a4cfc35.png)

Your Bookings Page:

![image](https://user-images.githubusercontent.com/109948740/234961984-13a55ca2-9409-4426-87e0-6a7936c79050.png)

Register Page:

![image](https://user-images.githubusercontent.com/109948740/234961081-41f21993-c6d0-4493-b0d1-ec288d1c94d2.png)

Sign In Page:

![image](https://user-images.githubusercontent.com/109948740/234961308-51a68725-0558-46c3-a979-08e12b0e2612.png)

Sign Out page:

![image](https://user-images.githubusercontent.com/109948740/234962162-c9638a7f-83ad-45c1-8375-c812a9ab0bb2.png)


### Mobile Results

Home Page:

![image](https://user-images.githubusercontent.com/109948740/234962665-e2d1b808-66a8-475d-aa1e-789aad7be14d.png)

Make a Booking Page:

![image](https://user-images.githubusercontent.com/109948740/234963051-eecd4522-5c5e-426a-bee4-e84523c5baf5.png)

Your Bookings Page:

![image](https://user-images.githubusercontent.com/109948740/234963156-f5547468-7b91-4c29-8e12-587bc3a463a1.png)

Register Page:

![image](https://user-images.githubusercontent.com/109948740/234963313-faf9d9cc-b75e-42ec-83e2-c6fefa7f4fd6.png)

Sign In Page:

![image](https://user-images.githubusercontent.com/109948740/234963435-9900b7d5-72d6-4624-ace4-375c995229f8.png)

Sign Out page:

![image](https://user-images.githubusercontent.com/109948740/234962503-92b60410-b836-4f1d-8c92-aeae13a7c9d2.png)

- - -

## MANUAL TESTING

### Testing User Stories

| Goals | How are they achieved? |
| :--- | :--- | 
| `User/Customers, both First time and returning customers` |
|  |  |  |
| Provide a menu that the user can view. | Created a standard menu list that is collapsible thanks to JS and gives three of each of starter, main course and dessert so that the user can see what is on offer. |
| Provide select times for reservations that the user can view. | Times that the user can select will be displayed on the home page. |
| Register for an account. | The description on the home page encourages new users to register for an account in order to make a booking. A register link is displayed on the navbar if a user is not logged in. |
| Log in to my account. | If a user is not logged into an account, a login link is provided on the navbar. |
| Make a booking (selecting a time and day). | A `Make a Booking` page will allow user selecting a specfic time by and day of their choosing. |
| View a list of the users' bookings. | A `Your Bookings` page will allow the user to view all bookings made, and will state whether they are pending approval or are approved. |
| Edit a booking. | When a user views their booking on the Your Bookings page, they are given the option to edit their booking (this option wiil only be available for pendng approval bookings). |
| Delete a booking. | When a user views their booking on the Your Bookings page, they are given the option to delete their booking. When the user selects delete, a modal will pop up to confirm deletion and to let the user know that the booking be deleted and cannot be undone (this option wiil be available for both pendng approval and approved bookings). |
| `Admin user` |
|  |  |  |
| Approve Bookings. | In the admin window, the bookings will be listed out in order of reservation dates and can be approved by selecting the checkbox beside each booking and clicking on accept from drop down menu. |


### Full Testing

Full testing was performed on the following devices, and additional testing for other devices was carried out using developer tools:

iMac 2021, MacBook Pro 14 inch 2021, iPhone 13 Pro, Samsung S20, 25 inch monitor, windows laptop

Each device tested the site using the following browsers:

Google Chrome on Mac and Windows, Safari

`Index/Base Page`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| **NAVBAR** |  |  |  |  |
|  |  |  |  |  |
| Logo image link | When clicked you are redirected to the home page | Clicked Logo | Redirected to home page | Pass|
| Navbar home link | When clicked you are redirected to the home page | Clicked link | Redirected to home page | Pass|
| Navbar Register link | When clicked you are redirected to the Register page | Clicked link | Redirected to Register page | Pass|
| Navbar Login link | When clicked you are redirected to the Sign in page | Clicked link | Redirected to Sign in page | Pass|
| Navbar Make a Booking link | When clicked you are redirected to the Make a booking page | Clicked link | Redirected to Make a booking page | Pass|
| Navbar Your Booking link | When clicked you are redirected to the Your Booking page | Clicked link | Redirected to Your Booking page | Pass|
| Navbar Logout link | When clicked you are redirected to the Sign out page | Clicked link | Redirected to Sign out page | Pass|
| Navbar link - Hover | When hovered over a shading of the area will occur to indicate that the cursor is over link | Hovered over link | Shading appears | Pass|
| **Menu** |  |  |  |  |
|  |  |  |  |  |
| Menu list | When clicked on, the menu will open to reveal the menu list and when clicked again it will collapse | Click collapsible list | List of menu appears and collapses when clicked on again. | Pass|
| **Footer** |  |  |  |  |
|  |  |  |  |  |
| Social media links | When clicking on social media links (displayed to users as icons courtesy of font awesome) an new window will appear therefore not closing the webpage the user is on | Clicked link | A new window will appear. | Pass|
| Footer will stick to bottom of page | Regardless of what content is displayed on the webpage, the footer will remain at the base of that page | Stick footer | Footer remains at bottom of page. | Pass|

`Login Page`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Username input - empty | This is a required field so the form should not submit if empty | Tried to submit the form with this field empty| Error message will appear to user requiring a username to proceed. | Pass|
| Password input - empty | This is a required field so the form should not submit if empty | Tried to submit the form with this field empty| Error message will appear to user requiring a password to proceed. | Pass|
| Incorrect username or password used | A flash message should display saying username/password incorrect - this is defensive programming - not letting user know which input is incorrect | Incorrect username/password entered| Message flashes to let the user know they have entered an incorrect username/password. | Pass|
| Link to register page | This should redirect the user to the register page | Clicked link| Redirected to the register page. | Pass|

`Register Page`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Username input - empty | The username is a required field, so should not submit with no value | Tried to submit form with no value entered | Tooltip lets user know this value is required. | Pass|
| Username input | If username is in use, message should flash to user | entered an in use username | Message flashed to say username already in use. | Pass|
| Password input | This field should be at least 8 characters long | Entered password less than 8 characters long | Tooltip tells user the password should be at least 8 characters long. | Pass|
| Password input - empty | The password is a required field, so should not submit with no value | Tried to submit form with no value entered | Tooltip lets user know this value is required. | Pass|
| Register button | Should redirect user to the log in page and a successful message flashed | Created new user and submitted form | Redirected to the log in page and message flashed. | Pass|


`Make a booking Page`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| **Email** |  |  |  |  |
|  |  |  |  |  |
| Email required | Before a booking can be made an email is needed | Click booking submit button without an email| Error message will appear to user requiring an email to proceed. | Pass|
| Email required | Only an email (format of an email) can be inputted into the email field | Click booking submit button without an email | Error message will appear to user requiring an email to proceed. | Pass|
| Different emails can allow for bookings on the same day | To allow the user to book for friends or colleagues on the same day that the user has booked, the user can use their emails to make booking| Click booking submit button with email| Booking made successfully. | Pass|
| **Number of People** |  |  |  |  |
|  |  |  |  |  |
| Selecting a number of guests between 1-6 | As noted on the bookings page, only between 1-6 people can be select per booking | Select number of people outside of the number 1-6| Error message will appear to user requiring number of guest between 1-6 to proceed. | Pass|
| **Reservation Date** |  |  |  |  |
|  |  |  |  |  |
| Selecting a day of booking | A user cannot select a day in the past | Selecting a day in the past | Error message will appear to user requiring today's date or a day in the future to proceed. | Pass|
| Selecting a day of booking (Double Booking) | Preventing the user from select a day that is already booked when creating a new booking (if same email is used). | Selecting a date that is already booked | Error message will appear to user stating that the booking exists for the email used. | Pass|
| **Reservation Time** |  |  |  |  |
|  |  |  |  |  |
| Selecting a time of booking | A user cannot select a time in the past (Based on the GMT Irish timezone) | Selecting a time in the past | Error message will appear to user requiring time in the future to proceed. | Pass|
| Selecting a time based on the specfic times outlined on website | A user cannot select a time that is outside the times outlined on the Home page | Selecting a time in outside of these times | Error message will appear to user requiring correct time to proceed. | Pass|

`Your Bookings Page`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| **List of Bookings** |  |  |  |  |
|  |  |  |  |  |
| List of Bookings in order of day | As list of Bookings will appear on this page when bookings are made and are in order by Reservation date | List of Bookings in order of Reservation date | List will appear in order of reservation date. | Pass|
| Status of Booking | The user can see approval status whether pending approval or approved | When booking is created, status pending approval will appear and user can edit or delete booking. When approved, status will appear as approve and the user can only delete booking | List of Bookings will appear with Pending Approval or Status approved. | Pass|
| **Edit Bookings** |  |  |  |  |
|  |  |  |  |  |
| Edit Booking | User can edit a pendng approval status booking by clicking on Green Edit Booking | Click on Edit Booking button | Redirected to a new page called Update Booking. | Pass|
| Make changes | User can edit a booking by adding addtional guests (Between 1-6), Todays' date or in the future, a time in the future, or change the email | Edit the number of guests, the day and time and change the email | Once clicked on the Update booking button, you are redirected to a Your Bookings page with the booking updated. | Pass|
| Edit Booking - Editing another user's booking | When logged in and trying to edit another user's booking by directly copying the url of that booking, the user doing so will be directed to a 404 page with warning | copy a url for editing another user's booking | Redirected back to 404 not found page. | Pass|
| Edit Booking - Editing another user's booking while logged out | When logged out and trying to edit another user's booking by directly copying the url of that booking, the user doing so will be redirected the sign in page | copy a url for editing another user's booking | Redirected back to sign in page. | Pass|
| **Delete Bookings** |  |  |  |  |
|  |  |  |  |  |
| Delete Booking - Modal | A modal should appear stating to user that this action cannot be undone | Click on Delete Booking button | Modal appears with Warning message that this acction cannot be undone. | Pass|
| Delete Booking - Close | A modal should appear stating to user that this action cannot be undone, when the user clicks on Close, they are redirected to the Your Bookings page | Click on close button in modal | Redirected back to Your Bookings page and booking is not deleted. | Pass|
| Delete Booking - Delete | A modal should appear stating to user that this action cannot be undone, when the user clicks on Delete, they are redirected to the Your Bookings page with the selected booking deleted | Click on Delete button in modal | Redirected back to Your Bookings page and selected booking is deleted. | Pass|
| Delete Booking - Deleting another user's booking | When logged in and trying to delete another user's booking by directly copying the url of that booking, the user doing so will be redirected the the home page | copy a url for deleting another user's booking | Redirected back to home page. | Pass|
| Delete Booking - Deleting another user's booking while logged out | When logged out and trying to delete another user's booking by directly copying the url of that booking, the user doing so will be redirected the sign in page | copy a url for deleting another user's booking | Redirected back to sign in page. | Pass|

 - - -

## BUGS

### Solved Bugs

| No | Bug | How I solved the issue |
| :--- | :--- | :--- |
| 1 | Modal was not working. | Added Modal Trigger class to the `a` element instead of the `button` element which triggered the modal.  |
| 2 | Index.html (Home Page) was not loading correctly when I tried to logout. When logging out, an error page appeared intead of the home page. | In addtion to the adding of the path to index.html as `path('', views.index, name='home')` to bookings app urls.py, I had to change the `LOGOUT_REDIRECT_URL = 'home'` in settings.py.  |
| 3 | When intially testing the field for Number of people that a user can book, there was no limit to what the user can book, even book 0 people. | Created a function in the forms.py that will prevent user from going below 1 and exceeding 6 people `def clean_group_size(self)`.  |
| 4 | When intially testing the field for Reservation Date, the user could book a day in the past and it will be accepted. | Created a function in the forms.py that will prevent user selecting a day in the past `def clean_day(self)`.  |
| 5 | Another issue arrised when the user could select a time in the past and although I had created a function similar to the `def clean_day(self)` this did not have the desired affect as it prevented the user from booking in the future (or the present) in terms of the day if the time was not in the future at the local time of booking. | Created a function `def clean_future_time_day(self)` (with the assistance of the CI Tutors which were a great help) that took the current day and local time in an if statement and if the day is equal to the present day and the time was greater than the current time, then the user can proceed, else raise a `ValidationError`.  |
| 6 | Even though the user can see the bookings they make and therefore double booking is unlikely, however in the event that the user does double book, a function was created to prevent this which was `def clean(self)`. However, this also prevented the user from editing bookings if it was on the same day or the same email was used. | I rewrote the code in both the `def clean(self)` to exclude bookings that contain the `instance` attribute using the `hasattr()` method and to filter for email. This had the desired effect.  |
| 7 | Following up on the time issue, another issue arised when the local time (GMT irish) and the server time was not synced correctly and so this was causing the user to book a time that was in the past (in terms of the local time). | I did not realise at the time that the `TIME_ZONE` variable in `Settings.py` was set to `UTC` and so I changed this to `Europe\London` and this corrected this issue.  |
| 8 | Error messages will not appear for the user when `updating a booking` as is the case with the `create a new booking` but due to time consraints I have added this to the future implementation section in the README. | I resolved the issue by rewriting the code chnaging from a function to a class based view similar to the BookingCreate Class..  |

- - -

### Known Bugs

| No | Bug | |
| :--- | :--- | :--- |
| 1 | When a user trys to update another user's booking - they are directed to a 404 page with a warning message. | due to time constraints I was unable to create a more user friendly view (in which I will state in future implementaion section of the README file), however the function prevent any user from updating another user's booking which for now serves its purpose|
