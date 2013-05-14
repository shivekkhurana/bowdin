l = window.location['pathname'];
s = "female";
level=1;
if (l == "/iam/female") {
	s = "male";
}
c = 0;
images = [];

$(function () {

	//document ready
	function load_images() {
		$('img').css("border-bottom","8px solid #fff");
		if (images.length !== 0) {
			$('.image_container .image1 img').attr('src', images[0][2]);
			$('.image_container .image2 img').attr('src', images[1][2]);

			$('.image_container .image1 a').attr('href', '/game/' + images[0][0] + '/wins/' + images[1][0]);
			$('.image_container .image2 a').attr('href', '/game/' + images[1][0] + '/wins/' + images[0][0]);

			$('.image_container .image1 div').html('wins : ' + (images[0][1] == 0 ? "0 (first match)" : images[0][1]));
			$('.image_container .image2 div').html('wins : ' + (images[1][1] == 0 ? "0 (first match)" : images[1][1]));

			images.splice(0, 2);
			for (i = 0; i < 2; i++) {
				(new Image()).src = images[i][2];
			}
		} else {
			load_next_set();
		}
	}

	function load_next_set() {
		var colors = ["#333", "#6E0280", "#004CB5", '#E0311C', "#15298A", "#2B7B22"];
		$.getJSON("/send/" + s, function (data) {
			images = data;
		}).success(function () {
			if (colors[c] === undefined) {
				c = 0;
			}
			$('.gamehead').css("background", colors[c++]);
			if(c>1){
       	$('.gameinfo').html("Level " + ++level);
			}
			load_images();
		});
	}

	load_next_set();

	$('.image_container a').click(function () {
		var f = '.' + $(this).attr('alt');
		$(f + ' img').css("border-bottom","8px solid #d8193b");

		//put up image loaders
		$('.image_container .image1 img').attr('src', '/assets/images/ajax-loader.gif');
		$('.image_container .image2 img').attr('src', '/assets/images/ajax-loader.gif');
			
		var post_url = $(this).attr('href');
		$.post(post_url, function (data) {
			//$('.image_container a').children('img').css("border-bottom", "8px solid #fff");
			load_images();
		});
		return false;
	});

	$('a.skip_set').click(function () {
		//put up image loaders
		$('.image_container .image1 img').attr('src', '/assets/images/ajax-loader.gif');
		$('.image_container .image2 img').attr('src', '/assets/images/ajax-loader.gif');
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
			$('a.skip_set').click();
		}
	});
});
