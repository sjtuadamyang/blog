/* Loading Script */
$(window).load(function() {
  "use strict";
    	$(".loader").delay(500).fadeOut();
    	$("#mask").delay(1000).fadeOut("slow");
    });

/* Load content */
$('.navigation > li').click(function(){
  $('.flex-active').removeClass('flex-active');
  var clickedPage = $(this);
  clickedPage.addClass('flex-active');
  $('.content').fadeOut('fast', function() {
    $('.content').load("/blog/" + clickedPage.index().toString(), function(){
      // Load js for google map
      "use strict";
      if ($('.content > div').attr('id') == '4') {
        $('.nivo-lbox').nivoLightbox({ effect: 'fade' });
        $('.post').click(function(){
          var clickPost = $(this);
          $('.content').fadeOut('fast', function() {
            $('.content').load("/blog/article/" + clickPost.attr('id'), function(){
              $('.content').fadeIn('fast');
            }) 
          });
        });
      }
      $('.content').fadeIn('fast', function() {
        if ($('.content > div').attr('id') == '5') {
          var map = new GMaps({
            el: "#map",
            lat: 37.4047456,
            lng: -122.0071204,
            zoom: 15, 
            zoomControl : true,
            zoomControlOpt: {
              style : "BIG",
              position: "TOP_LEFT"
            },
            panControl : true,
            streetViewControl : false,
            mapTypeControl: false,
            overviewMapControl: false
          });
                
          var styles = [
                {
                  stylers: [
                    { hue: "#00ffe6" },
                    { saturation: -100 }
                  ]
                }
          ];
                
          map.addStyle({
                styledMapName:"Styled Map",
                styles: styles,
                mapTypeId: "map_style"  
          });
                
          map.setStyle("map_style");

          map.addMarker({
            lat: 37.4047456,
            lng: -122.0071204,
            icon: $('#marker').attr('href')
          });
        }
      });
    })
  })
  
})




