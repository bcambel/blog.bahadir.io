(function($){
	$(init);
	function init(){
		$(".articles").masonry({
								   itemSelector : 'h3',
								   columnWidth : 240
							   });
	}
})(jQuery);