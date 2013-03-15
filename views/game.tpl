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
	
	<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
</head>

<script type="text/javascript">
	$(function(){
		//document ready
		
		function load_images()
		{
			$.getJSON("/send/{{gender}}", function(data){
				var images = ['http://graph.facebook.com/'+data[0]+'/picture?type=large', 'http://graph.facebook.com/'+data[2]+'/picture?type=large'];
				
				
				//put up image loaders
				$('.image_container .image1 img').attr('src', '/assets/images/ajax-loader.gif');
				$('.image_container .image2 img').attr('src', '/assets/images/ajax-loader.gif');
				
				$(images).each(function(){
					(new Image()).src = this;
				});
				    		
				$('.image_container .image1 img').attr('src', images[0]);
				$('.image_container .image2 img').attr('src', images[1]);
				
				$('.image_container .image1 a').attr('href','/game/'+data[0]+'/wins/'+data[2]);
				$('.image_container .image2 a').attr('href','/game/'+data[2]+'/wins/'+data[0]);
				
				$('.image_container .image1 div').html('wins : '+data[1]);
				$('.image_container .image2 div').html('wins : '+data[3]);
			});
		}
		load_images();
		
		$('.image_container a').click(function(){
			$('.image_container a').children('img').css("border-bottom","8px solid #fff");
			$(this).children('img').css("border-bottom","8px solid #e74d19");
			
			var post_url = $(this).attr('href');
			$.post(post_url, function(data){
				$('.image_container a').children('img').css("border-bottom","8px solid #fff");
				load_images();	
			});
			return false;
		});
		
		$(document).keydown(function(event){
			if(event.keyCode == 39){
				//right key pressed
				$('.image_container .image2 a').click();
			}
			
			if(event.keyCode == 37){
				//left key pressed
				$('.image_container .image1 a').click();
			}
			
			if(event.keyCode == 40){
				//down key pressed
				load_images();
			}
		});
	});
</script>

<body>
<div class="container gamehead">
	<div class="row">
		<div class="twelvecol">
			Everyone is 	&#9733; FAMOUS 	&#9733;
		</div>
	</div>
</div>

<div class="container">
	<div class="row">
		<div class="sixcol">
			<h4>Rules</h4>Click on the image to bowd it.
		</div>
		<div class="sixcol last controls">
				<strong>Shortcuts</strong>
				&#8594; Right Image / 
				&#8592; Left Image /
				&#8595; Skip 
		</div>
	</div>
</div>


<div class="container image_container">
	<div class="row">
			<div class="image1 sixcol">
				<a href=""><img src=""/></a>
				<div></div>
			</div><!--<div class="image1">-->
			
			<div class="image2 sixcol last">
				<a href=""><img src=""/></a>
				<div></div>
			</div><!--<div class="image2">-->
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

