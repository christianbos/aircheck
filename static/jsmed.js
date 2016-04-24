// start at bottom of page
$(document).ready(function() {
	scrollBottom();
});

function scrollBottom() {
	// var $target = $('html, body').outerHeight();
	// console.log($target);
	// $('html, body').scrollTop( $target );

	$('html, body').scrollTop($(".pad").offset().top);

	// if($(window).scrollTop() + $(window).height() >= $(document).height()){
	// window.scrollTo(0,document.body.scrollHeight);
	// }
}

window.onbeforeunload = function(e) {
	$('html, body').scrollTop(0);
};

var height = $(document).height();
$depthNumber = $('.js-depth');
$depth = $('.depth');
$loader = $('.js-loader');
var startDepth = {depth:0.00};
var snippet;

$.jGFeed('http://water.weather.gov/ahps2/rss/obs/rmdv2.rss',
	function(feeds) {
		// Check for errors
		if (feeds) {
			snippet = feeds.entries[0].content;
			parseFeed(snippet);

		} else {
			// there was an error
			return false;
		}
	}, 10);

function parseFeed(snippet) {

	var start_pos = snippet.indexOf('Latest Observation:') + 20;
	var end_pos = snippet.indexOf(' ',start_pos);
	var depth = parseFloat(snippet.substring(start_pos,end_pos));

	var decimal = snippet.substring(start_pos,end_pos);
	var scrollTop = $(window).scrollTop();
	var scrollPosition = scrollTop - decimal.replace(/\./g, "");
	var depthPosition = decimal.replace(/\./g, "");
	console.log(scrollTop);
	setTimeout(function(){
		animate(depth, scrollPosition, depthPosition);
	}, 3000);
}
function animate(depth, scrollPosition, depthPosition) {

	TweenMax.to($loader, 0.5, {
		opacity: 0,
		ease: Power4.easeOut
	});

	TweenMax.to(startDepth, 2.5, {
		depth:"+="+ depth,
		onUpdate:updateDepth,
		ease:Power2.easeOut
	});

	TweenMax.to($depth, 2.5, {
		bottom: depthPosition,
		ease:Power2.easeOut
	});

	TweenMax.to(window, 2.5, {scrollTo:{y:scrollPosition, x:0, ease:Power2.easeOut}});
}

function updateDepth() {
	var d = startDepth.depth;
	var de = d.toFixed(2);
	$depthNumber.html(de);
}
