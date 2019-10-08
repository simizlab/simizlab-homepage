// https://www.webantena.net/javascriptjquery/jquery-currentmenu-design/
$('#navigation ul li a').each(function(){
        var $href = $(this).attr('href');
        var $current_href = location.href

        if($href.slice(-1) == "/"){
          var $href = $href.slice(0, -1);
        }
        if($current_href.slice(-1) == "/"){
          var $current_href = $current_href.slice(0, -1);
        }

        var $base = $(this).parent('.dropdown')
        if($current_href == $href) {
          $base.addClass('active');
        }
        else {
          $base.removeClass('active');
        }
});
