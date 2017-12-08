index_html = """
{% load static %}
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://fonts.googleapis.com/css?family=Quicksand:500|Khula:300,400,700" rel="stylesheet">

  <!-- Latest compiled and minified CSS -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

  <!-- Optional theme -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
  <script src="https://code.jquery.com/jquery-3.2.1.min.js" integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4=" crossorigin="anonymous"></script>

  <!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
    <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
  <![endif]-->
  <link rel="stylesheet" href="{% static 'css/csdt.css' %}" type="text/css" />
  <link rel="stylesheet" href="{% static 'css/template.css' %}" type="text/css" />
  <!-- <link rel="stylesheet" href="https://csdt.rpi.edu/culture/quilting/template.css" type="text/css" /> -->
  <link rel="stylesheet" href="{% static 'css/tutorial.css' %}" type="text/css" />
</head>

<body>

<!-- Static navbar -->
  <nav class="navbar navbar-inverse navbar-fixed-top">
    <div class="container">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
          <span class="sr-only">Toggle navigation</span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <a class="navbar-brand" href="http://www.nsf.gov"><img style="height: 40px;margin-top: -10px;margin-right:10px;" alt="NSF" src="https://csdt.rpi.edu/static/img/nsf.gif"></a>

        <a class="navbar-brand" href="/"><img style="height: 40px;margin: -10px;" alt="CSDT" src="https://csdt.rpi.edu/culture/img/CSDT.LOGO2-SMALL.jpg"></a>

      </div>
      <div id="navbar" class="collapse navbar-collapse">
        <ul class="nav navbar-nav">
          <li><a href="/">Applications</a></li>
          <li><a href="/projects">Projects</a></li>
          <li><a href="/teams/teams">Classrooms</a></li>
          <li><a href="/news">News</a></li>
          <li><a href="/about">About</a></li>
        </ul>
        <ul class="nav navbar-nav navbar-right">

        </ul>
      </div><!--/.nav-collapse -->
    </div>
  </nav>

  <div class="page-scroll">
    <div class="row row-offcanvas row-offcanvas-left">

      <nav class="navbar navbar-inverse navbar-local visible-xs">
        <div class="container-fluid">
          <div class="navbar-header">
              <a class="navbar-brand" href="../index.html">Quilting</a> <button aria-expanded="false" class="navbar-toggle collapsed" data-target="#nav-menu" data-toggle="collapse" type="button"><span class="sr-only">Toggle navigation</span> <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span></button>
          </div>
          <div class="collapse navbar-collapse navbar-right" id="nav-menu">
              <ul id="xs-nav" class="nav navbar-nav">
                  
              </ul>
          </div>
        </div>
      </nav>

      <!-- sidebar -->
      <div class="stuck">
        <div class="col-xs-6 col-sm-3 sidebar-offcanvas" id="sidebar" role="navigation">
          <ul id="sidenav" class="nav">
                
          </ul>
        </div>
      </div>


      <div class="right">
        <!------------>
        <div class="cultural-bg-0">
          <a class="anchor" id="background" class=""></a>
              <!-- <div class="section-header">
                  Quilting
              </div> -->
       
          <div class="row">
            <div class="col-md-12">
              <div class="below-text">
                  {% include section %}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <script>
  $(document).ready(function() {
    $('[data-toggle=offcanvas]').click(function() {
      $('.row-offcanvas').toggleClass('active');
    });
  });

  $.getJSON("{{ repo.get_absolute_url }}render/sidenavbar.json", function(json) {
      for (var key in json){
          console.log(json[key].name + ":" + json[key].link);
          if (json[key].children){
              for (var i = 0; i < json[key].children.length; i++){
                  console.log("    "+json[key].children[i].name+":"+json[key].children[i].link);
              }
          }
      }

      var sidenav = $('#sidenav').empty();
      var xsnav = $('#xs-nav').empty()
      for (var key in json){
          sidenav.append('<li><a href="' + json[key].link + '">' + json[key].name + '</a></li>');
          xsnav.append('<li><a href="' + json[key].link + '">' + json[key].name + '</a></li>');
          if (json[key].children){
              for (var i = 0; i < json[key].children.length; i++){
                  sidenav.append('<li class="indented"><a href="' + json[key].children[i].link + '">' + json[key].children[i].name + '</a></li>')
                  xsnav.append('<li><a href="' + json[key].children[i].link + '">' + json[key].children[i].name + '</a></li>');
              }
          }
      }
  });

  </script>
  <!-- Latest compiled and minified JavaScript -->
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>

</body>
</html>
"""

background = '''
<h1>Quilting</h1>

<p>Quilting uses small scraps of fabric to make larger blankets, bed covers and other works. Because it is often based on discarded textiles, it is available to low income communities, and benefits the environment by reducing waste. In this site you can learn about the cultural background and program simulations for the designs of 3 quilt traditions: Gees Bend African American quilts; Native American star quilts, and Appalachian quilting practices. Quilting is just one of many textiles that sustain both cultural traditions, economic income, and environmental sustainability. Read more <a href="teaching.html">here</a>.</p>
'''

