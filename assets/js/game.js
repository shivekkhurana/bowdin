l = window.location['pathname'];
s = "female";
if (l == "/iam/female") {
	s = "male";
}
images = [];

$(function () {

	//document ready
	function load_images() {
			if(images.length != 0){
				//put up image loaders
				$('.image_container .image1 img').attr('src', '/assets/images/ajax-loader.gif');
				$('.image_container .image2 img').attr('src', '/assets/images/ajax-loader.gif');
		
				for (i = 0; i < 2; i++) {
					(new Image()).src = images[i][2];
				}


				$('.image_container .image1 img').attr('src', images[0][2]);
				$('.image_container .image2 img').attr('src', images[1][2]);

				$('.image_container .image1 a').attr('href', '/game/' + images[0][0] + '/wins/' + images[1][0]);
				$('.image_container .image2 a').attr('href', '/game/' + images[1][0] + '/wins/' + images[0][0]);

				$('.image_container .image1 div').html('win percent : ' + images[0][1] + "%");
				$('.image_container .image2 div').html('win percent : ' + images[1][1] + "%");

				images.splice(0, 2);
			}
			else{
				load_next_set();
			}
	}
	
	function load_next_set(){
		$.getJSON("/send/"+s, function (data) {
		images = data;
		}).success(function(){
			load_images();
		});
	}
	
	load_next_set();
	
	$('.image_container a').click(function () {
		$('.image_container a').children('img').css("border-bottom", "8px solid #fff");
		$(this).children('img').css("border-bottom", "8px solid #e74d19");

		var post_url = $(this).attr('href');
		$.post(post_url, function (data) {
			$('.image_container a').children('img').css("border-bottom", "8px solid #fff");
			load_images();
		});
		return false;
	});

	$('a.skip_set').click(function () {
		load_images();
	});

	$(document).keydown(function (event) {
		if (event.keyCode == 39) {
			//right key pressed
			$('.image_container .image2 a').click();
		}

		if (event.keyCode == 37) {
			//left key pressed
			$('.image_container .image1 a').click();
		}

		if (event.keyCode == 40) {
			//down key pressed
			load_images();
		}
	});
});
