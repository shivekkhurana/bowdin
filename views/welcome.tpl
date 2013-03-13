<!doctype html>
<html lang="en">

<head>
	<meta charset="utf-8" />
	<title>bowd.in</title>

	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	
	<!-- 1140px Grid styles for IE -->
	<!--[if lte IE 9]><link rel="stylesheet" href="/assets/css/ie.css" type="text/css" media="screen" /><![endif]-->

	<!-- The 1140px Grid - http://cssgrid.net/ -->
	<link rel="stylesheet" href="/assets/css/1140.css" type="text/css" media="screen" />
	
	<!-- Custom styles -->
	<link rel="stylesheet" href="/assets/css/style.css" type="text/css" media="screen" />
	
	<!--css3-mediaqueries-js - http://code.google.com/p/css3-mediaqueries-js/-->
	<script type="text/javascript" src="/assets/js/css3-mediaqueries.js"></script>
	
	<!--favicon-->
	<link rel="shortcut icon" type="image/x-icon" href="/assets/favicon.ico">
	
</head>



<body>
<div class="container masthead">
	
	<div class="row">
		<div class="twelvecol">
			<!--img src="assets/images/specs.jpg"-->
			<h1>bowd.in</h1>
			<hr class="bottom"/>
			Everyone is 	&#9733; FAMOUS 	&#9733;
		</div>
	</div>
</div>


<div class="container call_to_action">
	<div class="row">
		<div class="sixcol guy">
			<a href="iam/male"><p>I'm a boy</p></a>
		</div>
		<div class="sixcol girl last">
			<a href="iam/female"><p>I'm a girl</p></a>
		</div>
	</div>
</div>


<div class="container about">
	<div class="row">
		<div class="twelvecol">
			<h4>About</h4>
			bowd.in utilizes facebook open graph api to bring good looking pictures of amazing people on front page of the internet. Then you :) choose the ones you like and we put them on the leader board. 
		</div>
	</div>
</div>

<div class="container leader_board">
	<div class="row">
		<div class="twelvecol">
			<h4>Most bowd</h4>
		</div>
	</div>
		
	<div class="row">
		%i = -1
		%for k in top:
			%i +=1
			%if((i+1)%6 == 0):
				<div class="twocol last"><img src="{{k[0]}}"/>{{k[1]}}</div>
				</div>
				<div class="row">
				
			%else:
				<div class="twocol"><img src="{{k[0]}}"/>{{k[1]}}</div>
			%end
		%end
	</div>
	
</div>


<div class="container footer">
	<div class="row">
		<div class="twelvecol">
			<a href="/">Home</a>
			<a href="/faq">FAQ</a>
			<a href="/report">Report Abuse</a>
			<a href="/contact">Contact</a>
		</div>
	</div>
</div>

</body>

</html>
