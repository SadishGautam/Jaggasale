

{% load static %}

<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <!-- <link rel="stylesheet" href="css/bootstrap.min.css"> -->

    

    <!-- css -->
    <link rel="icon" href="{% static 'pics/home.ico' %}">
    <link rel="stylesheet" type="text/css" href="{% static 'css/style.css' %}">
    <link rel="stylesheet" type="text/css" href="{% static 'css/ofc-detail1.css' %}">
    <link rel="stylesheet" type="text/css" href="http://sadish.com.np/projects/jaggasale/css/style.css">

    <link rel="stylesheet"  type="text/css" href="http://sadish.com.np/projects/jaggasale/css/why-choose.css">
    <link rel="stylesheet"  type="text/css" href="http://sadish.com.np/projects/jaggasale/css/register.css">
    <link rel="stylesheet" type="text/css" href="http://sadish.com.np/projects/jaggasale/css/footer.css">
    <link rel="stylesheet" type="text/css" href="http://sadish.com.np/projects/jaggasale/css/about.css">


    <!-- fonts -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.10.0-11/css/all.css">
    <link href="https://fonts.googleapis.com/css?family=Farro&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Farro|Open+Sans&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Abel&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Ubuntu&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Tangerine&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Roboto&display=swap" rel="stylesheet">


    <!-- carousel -->
    <link rel="stylesheet" type="text/css" href="http://sadish.com.np/projects/jaggasale/css/owl-carousel.min.css">
    <link rel="stylesheet" type="text/css" href="http://sadish.com.np/projects/jaggasale/css/owl.theme.default.min.css">
    <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.1/css/lightbox.min.css">

    <title>JaggaSale</title>
  </head>
  <body>

    <!-- ---------------------------Sadish Codes---------------------------  -->

    <div class="container-fluid header pt-5 pb-5">
        <div class="row">
            <div class="col-lg-3 col-md-3 col-sm-12 ">
                <a href="{% url 'home' %}" style="padding-left:40px;color:white;text-decoration: none;display: inline-block;text-shadow:1px 1px 3px grey;font-family:'Tangerine'"><h1 class="display-4">JaggaSale.com</h1></a>

                
            </div>
            <div class="col-lg-5 col-md-5 col-sm-12 text-center">
               
                    <ul class="list-unstyled d-flex mt-3">
                     <li class="dropdown">
                        <a class="dropbtn hm" href="{% url 'home' %}">HOME</a>
                        <div class="dropdown-content">
                            <a href="{% url 'about page' %}">About</a>
                            <a href="{% url 'contact page' %}">Contact</a>
                            <a href="{% url 'news page' %}">News</a>
                        </div>
                     </li>   
                    <li class="dropdown">
                        <a href="kathmandu.php" style="color:white;text-decoration:none;transition:.5s;" class="dropbtn">KATHMANDU</a>
                        <div class="dropdown-content">
                            <a href="kathmandu.php">Baneshwor</a>
                            <a href="#">Sundhara</a>
                            <a href="#">Kalanki</a>
                            <a href="#">Gaushala</a>
                            <a href="#">Balaju</a>
                        </div>
                    </li>
                    <li class="dropdown">
                        <a href="#" style="color:white;text-decoration:none;transition:.5s;" class="dropbtn">LALITPUR</a>
                        <div class="dropdown-content">
                            <a href="#">Patan</a>
                            <a href="#">Lagankhel</a>
                            <a href="#">Jawalakhel</a>
                        </div>
                    </li>
                    <li class="dropdown">
                        <a href="#" style="color:white;text-decoration:none;transition:.5s;" class="dropbtn">BHAKTAPUR</a>
                        <div class="dropdown-content">
                            <a href="#">Siddhapokhari</a>
                            <a href="#">Jagati</a>
                            <a href="#">Suryabinayak</a>
                        </div>
                    </li>
                    <li class="dropdown">
                        <a href="#" style="color:white;text-decoration:none;transition:.5s;" class="dropbtn">OTHERS</a>
                        <div class="dropdown-content">
                            <a href="#">Land</a>
                            <a href="#">Property</a>
                            <a href="#">Cars</a>
                        </div>
                    </li>
                    </ul>

            </div>
            <div class="col-lg-4 col-md-4 col-sm-12">
                <div class="listing mt-2 d-flex align-items-center">
                    <div class="list ml-5">
                        <a href="registerform.php"><i class="fas fa-home"></i>&nbsp; ADD LISTING</a>      
                    </div>
                    <div class="refresh ml-3">
                        <a style="color:white;" href="compare.php"><i class="fas fa-retweet"></i></a><span class="badge">0</span>
                    </div>
                    <div class="wishlist" style="position:relative;">
                    <div class="heart icon ml-3">
                        <a style="color:white" href="#"><i class="far fa-heart"></i></a><span class="badge">0</span>
                    </div>
                        <div class="container wish">
                            <a href="wishlist.php">Wishlist <span class="badge">0</span></a>
                            <a href="save-search.php">Save Searches <span class="badge">0</span></a>
                        </div>
                    </div>
                    <div class="login-form" style="position:relative;">
                        
                        <div class="login container">
                            
                        </div>

                    </div>
                </div>
            </div>
        </div>
        
        <div class="menu" style="display: none;">
            <span id="bars" style="font-size:30px;cursor:pointer;color:white" onclick="openNav()">&#9776;</span>
        </div>

        <div id="myNav" class="overlay">
            <div class="overlay-content">
                <ul class="list-unstyled">
                    <li class="small-drop">
                        <div class="accordion">
                            <div class="card" style="background: var(--pri-color)">
                                <div class="card-header">
                                    <a href="{% url 'home' %}" style="color:white;text-decoration:none;">HOME</a>
                                </div>
                            </div>
                        </div>
                    </li> 
                    <li class="small-drop">
                    <div class="accordion" id="accordionExample">
                        <div class="card">
                            <div class="card-header" id="headingOne">
                                <a style="color:black;text-decoration:none;" href="#" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                                KATHMANDU<i style="float: right;" class="fas fa-chevron-down"></i>
                                </a>                           
                            </div>
                        
                            <div id="collapseOne" class="collapse" aria-labelledby="headingOne" data-parent="#accordionExample">
                            <div class="card-body">
                                <a href="kathmandu.php">Baneshwor</a>
                                <a href="#">Sundhara</a>
                                <a href="#">Kalanki</a>
                                <a href="#">Gaushala</a>
                                <a href="#">Balaju</a>
                            </div>
                            </div>
                        </div>
                    </div>
                    </li>
                    <li class="small-drop">
                        <div class="accordion" id="accordionExample">
                            <div class="card">
                                <div class="card-header" id="headingTwo">
                                    <a style="color:black;text-decoration:none;" href="#" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                                    LALITPUR<i style="float: right;" class="fas fa-chevron-down"></i>
                                    </a>                           
                                </div>
                            
                                <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordionExample">
                                <div class="card-body">
                                    <a href="#">Patan</a>
                                    <a href="#">Lagankhel</a>
                                    <a href="#">Jawalakhel</a>
                                </div>
                                </div>
                            </div>
                        </div>
                    </li>
                    <li class="small-drop">
                        <div class="accordion" id="accordionExample">
                            <div class="card">
                                <div class="card-header" id="headingThree">
                                    <a style="color:black;text-decoration:none;" href="#" data-toggle="collapse" data-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
                                    BHAKTAPUR<i style="float: right;" class="fas fa-chevron-down"></i>
                                    </a>                           
                                </div>
                            
                                <div id="collapseThree" class="collapse" aria-labelledby="headingThree" data-parent="#accordionExample">
                                <div class="card-body">
                                    <a href="#">Siddhapokhari</a>
                                    <a href="#">Jagati</a>
                                    <a href="#">Suryabinayak</a>
                                </div>
                                </div>
                            </div>
                        </div>
                    </li>
                    <li class="small-drop">
                        <div class="accordion" id="accordionExample">
                            <div class="card">
                                <div class="card-header" id="headingFour">
                                    <a style="color:black;text-decoration:none;" href="#" data-toggle="collapse" data-target="#collapseFour" aria-expanded="false" aria-controls="collapseFour">
                                    OTHERS<i style="float: right;" class="fas fa-chevron-down"></i>
                                    </a>                           
                                </div>
                            
                                <div id="collapseFour" class="collapse" aria-labelledby="headingFour" data-parent="#accordionExample">
                                <div class="card-body">
                                    <a href="#">Land</a>
                                    <a href="#">Property</a>
                                    <a href="#">Cars</a>
                                </div>
                                </div>
                            </div>
                        </div>
                    </li>
                </ul>  
            </div>
        </div>
        
            <a href="javascript:void(0)" class="closenav" onclick="closeNav()"><i style="padding:0 10px" class="fas fa-times"></i></a>
        
     </div>

        
          

























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


    <section class="form">
        <div class="container">
            <div class="row">

                <div class="col-md-6 clearfix">
                    <div class="first-form">
                    <h4>Sign In</h4>


                    <form action="/loginonly" method="post">
                    {% csrf_token %}
                        <p>Username</p>
                        <input spellcheck="false"  type="text" class="form-control" id="loginusername" name="loginusername" placeholder="Enter username" required>

                        <p>Password</p>
                        <input spellcheck="false" type="password" class="form-control" id="loginpassword" name="loginpassword" placeholder="Enter password" required>

                    
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
                        {% csrf_token %}
                                <p>Username</p>
                                <input spellcheck="false" type="text" id="username" class="form-control" name="username" placeholder="Username must be lowercase and alphanumeric" required>

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
