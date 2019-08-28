'use strict';
// document.addEventListener('DOMContentLoaded', function () {
//     console.log(document.getElementById('contact-message'));
// });

$('.mail-submit').click(function(){
    // check required method
    var submit_flag = true;
    $("input[required]:invalid").each(function(){
        submit_flag = false;
    });
    $("textarea[required]:invalid").each(function(){
      submit_flag = false;
    });
    if(!submit_flag) return false;

    const baseurl = 'https://formspree.io/';
    const encoded_data = $(this).parents('form').attr('action');
    // http://jsfiddle.net/HX642/6/
    const decoded_data = encoded_data.replace(/[a-zA-Z]/g, function(char){ //foreach character
              // console.log(char);
              return String.fromCharCode( //decode string
                  /**
                   * char is equal/less than 'Z' (i.e. a  capital letter), then compare upper case Z unicode
                   * else compare lower case Z unicode.
                   *
                   * if 'Z' unicode greater/equal than current char (i.e. char is 'Z','z' or a symbol) then
                   * return it, else transpose unicode by 26 to return decoded letter
                   *
                   * can't remember where I found this, and yes it makes my head hurt a little!
                   */
                  (char<="Z"?90:122)>=(char=char.charCodeAt(0)+13)?char:char -26);
          });
    // console.log(baseurl + decoded_data);
    $(this).parents('form').attr('action', baseurl + decoded_data);
    $(this).parents('form').submit();
});
