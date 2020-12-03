{% load static %}

{% include 'header.php' %}


<style>
    .header{
        box-shadow: 1px 1px 10px 1px grey;
    }
    .header a.hm{
        background:transparent;
    }
    .header a{
      color:black!important;
    }
    .header .listing .list a,
    .header .listing .refresh,
    .header .listing .heart,
    .header .listing .user{
        border: 1px solid var(--pri-color);
    }
    .header .listing .list a:hover{
        background: var(--pri-color);
        color:white!important;
    }
    .header .menu #bars{
        color:var(--pri-color)!important;
    }
    .header .register a{
        color:var(--pri-color)!important;
    }
    .header .register a:hover{
        color:var(--sec-color)!important;
    }
    section.form{
        font-family:'abel';
    }
</style>

<div class="clearfix"></div>


    <section class="form" >
        <div class="container">
            <div class="row">

                <div class="col-md-6 clearfix">
                    <div class="first-form">
                    <h4>Sign In</h4>


                    <form action="#" method="POST">
                        <p>Login</p>
                        <input spellcheck="false"  type="text" class="form-control" name="login" placeholder="Enter login" required>

                        <p>Password</p>
                        <input spellcheck="false" type="password" class="form-control" name="first_name" placeholder="Enter password" required>

                    
                        <div class="custom-control custom-checkbox">
                                <input spellcheck="false" type="checkbox" class="custom-control-input" id="customCheck1">
                                <label class="custom-control-label" for="customCheck1">Remember me</label>
                        </div>

                        <button class="btn form-control" type="submit"> SIGN IN </button>
                    </form>
                    </div>
                </div>


                <!-- Registration part -->

                <div class="col-md-6 clearfix" style="background: rgba(185, 184, 184, 0.192)">
                    <div class="second-form">
                        <h4>Registration</h4>

                        <form action="/signup" method="post">
                                <p>Username</p>
                                <input spellcheck="false" type="text" id="username" class="form-control" name="username" placeholder="Enter login" required>

                                <p>First Name</p>
                                <input spellcheck="false" type="text" id="fname" class="form-control" name="fname" placeholder="Enter first name" required>

                                <p>Last Name</p>
                                <input spellcheck="false" type="text" id="lname" class="form-control" name="lname" placeholder="Enter last name" required>

                                <p>Email</p>
                                <input spellcheck="false" type="text" id="email" class="form-control" name="email" placeholder="Enter email" required>

                                <p>User role</p>
                                <select style="height:50px;" class="custom-select">
                                        <option selected>Select user role</option>
                                        <option value="1">Realtor</option>
                                        <option value="1">Landlord</option>
                                        <option value="1">Renter</option>
                                        <option value="1">User</option>
                                </select>

                                <p>Password</p>
                                <input spellcheck="false" type="password" id="pass1" class="form-control" name="pass1" placeholder="Enter password" required>

                                <p>Re-enter Password</p>
                                <input spellcheck="false" type="password" id="pass2" class="form-control" name="pass2" placeholder="Re-enter password" required>
                                    {% csrf_token %}
                               <div class="but text-right ">
                                    <button class="btn" type="submit"> REGISTER </button>
                             </div>
                        </form>

                    </div>
                </div>
            </div>
        </div>
    </section>

    {% include 'footer.php' %}
