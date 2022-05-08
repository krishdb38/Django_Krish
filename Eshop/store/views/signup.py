from django.shortcuts import render, redirect 
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signup(View):

    def get(self, request, *args, **kwargs):
        return render(request,'signup.html')

    def post(self, request, *args, **kwargs):
        postData = request.POST 
        first_name = postData.get('first_name')
        last_name = postData.get('last_name')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        # Validation 
        value = {"first_name":first_name, "last_name":last_name, "phone":phone, "email":email}
        errror_message = None
        customer = Customer(first_name = first_name, last_name = last_name, phone=phone, email = email, password=password)
        error_message = self.validateCutomer(customer)

        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')

        else:
            data = {
                'error' : error_message, 
                'values' : value
            }

            return render (request, 'signup.html' , data)

    def validateCustomer(self, customer) :
        error_message = None
        if not customer.first_name :
            error_message = "First Name Required "
        elif len(customer.first_name ) < 4:
            error_message = "First name must be 4 char long or more"
        elif not customer.last_name :
            error_message = "Last name must be pass "
        elif len(customer.last_name) < 4 :
            error_message = "LastName length must be higher than 4"
        elif customer.phone :
            error_message = "Phone number not Entered "
        elif len(customer.phone) <10 :
            error_message = "Phone number must be higher than 10 characters "
        elif len(customer.password) < 10 :
            error_message = "password lenght must be longer than 10 characters"
        elif len(customer.email) < 5 :
            error_message = " Customer email length must be longer than 5"
        elif customer.isExist():
            error_message = "Email Address already Registered"
        return error_message
        