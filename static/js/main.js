/* init WOW */
new WOW().init();

/* --------------  Slide-To-Top --------------  */
var btn = $('#toTop');

$(window).scroll(function () {
  if ($(window).scrollTop() > 300) {
    btn.addClass('show');
  } else {
    btn.removeClass('show');
  }
});

btn.on('click', function (e) {
  e.preventDefault();
  $('html, body').animate({ scrollTop: 0 }, '300');
});

/* --------------  JS for EasyResponsive tab --------------  */
$(document).ready(function () {
  $('#horizontalTab').easyResponsiveTabs({
    type: 'default', //Types: default, vertical, accordion           
    width: 'auto', //auto or any width like 600px
    fit: true   // 100% fit in a container
  });
});

/* --------------  Year --------------  */