$(document).ready(function() {
        var amountScrolled = 400;

        // back to top icon
        $(window).scroll(function() {
          if ( $(window).scrollTop() > amountScrolled ) {
            $('a.back-to-top').fadeIn('slow');
          } else {
            $('a.back-to-top').fadeOut('slow');
          }
        });

        $('.ui.accordion').accordion('toggle');

          // create sidebar and attach to menu open
        $('.toc').click(function() {
          $('.ui.sidebar').sidebar('toggle')
        });


        //modal script at program section

        // image hover effect
        $('.dimmer').dimmer({
            on: 'hover'
        });


        // back to top button
        $('.pusher').append('<a href="#" class="back-to-top">Back to Top</a>');
        $('a.back-to-top, a.simple-back-to-top').click(function() {
        	$('html, body').animate({
        		scrollTop: 0
        	}, 700);
        	return false;
        });

        $('.ui.menu .ui.selection.dropdown').dropdown();
        $('.ui.menu .ui.dropdown.item').dropdown({on: 'hover'});

        $('.ui.segment .faculty').popup({
          on: 'hover',
          variation: 'small inverted',
        });

        // Update of March 25, 2018 6:34


        // for fixed menus like in the FAQs Section
        $('.main.menu').visibility({
          type: 'fixed'
        });

        // Custom script for index.html

                var header = "#CHANGEheader";
                var description = "#CHANGEdescription";
                var image = "#CHANGEimage";
                var date = "#CHANGEdate";


                var headerBuffer = $(header).text();
                var textBuffer = $(description).text();
                var imageBuffer = $(image).html();
                var dateBuffer = $(date).text();


                var interval = 500;
                var text_default = "Lorem iptium";
                var id_1 = "#hoverImage", id_2 = "#hoverImage2", id_3 = "#hoverImage3", id_4 = "#hoverImage4", id_5 = "#hoverImage5", id_6 = "#hoverImage6", id_7 = "#hoverImage7", id_8 = "#hoverImage8";


                $("#hoverImage, #hoverImage2, #hoverImage3, #hoverImage4, #hoverImage5, #hoverImage6, #hoverImage7, #hoverImage8").hover(function (){
                  // buffer = $(this).html();
                    if ($(this).is(id_1))
                  {
                    $(header).fadeOut(interval, function(){
                      $(this).text("Classroom of Grade 11 - Andromeda").fadeIn(interval)
                    });
                    $(description).fadeOut(interval, function(){
                      $(this).text("Fully prepared Senior High Rooms").fadeIn(interval)
                    });
                    $(image).fadeOut(interval, function(){
                      $(this).html("<img src=\"img/qshs/Students + SHS.jpg\">").fadeIn(interval)
                    });
                    $(date).fadeOut(interval, function(){
                      $(this).text("Taken: Feb 69, 1969").fadeIn(interval)
                    });
                  }
                  else if ($(this).is(id_2))
                  {
                    $(header).fadeOut(interval, function(){
                      $(this).text("Classroom of Grade 10 - Antares").fadeIn(interval);
                    });
                    $(description).fadeOut(interval, function(){
                      $(this).text("Equiped with the latest technology \n Also, it has aircon").fadeIn(interval);
                    });
                    $(image).fadeOut(interval, function(){
                      $(this).html("<img src=\"img/qshs/Room + Main 2.jpg\">").fadeIn(interval)
                    });
                    $(date).fadeOut(interval, function(){
                      $(this).text("Taken: Feb 69, 1969").fadeIn(interval)
                    });
                  }
                  else if ($(this).is(id_3))
                  {
                    $(header).fadeOut(interval, function(){
                      $(this).text("Chemical Laboratory").fadeIn(interval);
                    });
                    $(description).fadeOut(interval, function(){
                      $(this).text("Changed content 3").fadeIn(interval);
                    });
                    $(image).fadeOut(interval, function(){
                      $(this).html("<img src=\"img/4.jpg\">").fadeIn(interval)
                    });
                    $(date).fadeOut(interval, function(){
                      $(this).text("Taken: Feb 69, 1969").fadeIn(interval)
                    });
                  }
                  else if ($(this).is(id_4))
                  {
                    $(header).fadeOut(interval, function(){
                      $(this).text("Computer Laboratory").fadeIn(interval);
                    });
                    $(description).fadeOut(interval, function(){
                      $(this).text("Changed content 4").fadeIn(interval);
                    });
                    $(image).fadeOut(interval, function(){
                      $(this).html("<img src=\"img/qshs/Comlab2.jpg\">").fadeIn(interval)
                    });
                    $(date).fadeOut(interval, function(){
                      $(this).text("Taken: Feb 69, 1969").fadeIn(interval)
                    });
                  }
                  else if ($(this).is(id_5))
                  {
                    $(header).fadeOut(interval, function(){
                      $(this).text("Speech Laboratory").fadeIn(interval);
                    });
                    $(description).fadeOut(interval, function(){
                      $(this).text("Changed content 5").fadeIn(interval);
                    });
                    $(image).fadeOut(interval, function(){
                      $(this).html("<img src=\"img/qshs/Speech Lab + Students.JPG\">").fadeIn(interval)
                    });
                    $(date).fadeOut(interval, function(){
                      $(this).text("Taken: Feb 69, 1969").fadeIn(interval)
                    });
                  }
                  else if ($(this).is(id_6))
                  {
                    $(header).fadeOut(interval, function(){
                      $(this).text("Dormitory").fadeIn(interval);
                    });
                    $(description).fadeOut(interval, function(){
                      $(this).text("Changed content 6").fadeIn(interval);
                    });
                    $(image).fadeOut(interval, function(){
                      $(this).html("<img src=\"img/qshs/Dorm 2.jpg\">").fadeIn(interval)
                    });
                    $(date).fadeOut(interval, function(){
                      $(this).text("Taken: Feb 69, 1969").fadeIn(interval)
                    });
                  }
                  else if ($(this).is(id_7))
                  {
                    $(header).fadeOut(interval, function(){
                      $(this).text("Cafeteria").fadeIn(interval);
                    });
                    $(description).fadeOut(interval, function(){
                      $(this).text("Changed content 7").fadeIn(interval);
                    });
                    $(image).fadeOut(interval, function(){
                      $(this).html("<img src=\"img/qshs/Cafeteria.jpg\">").fadeIn(interval)
                    });
                    $(date).fadeOut(interval, function(){
                      $(this).text("Taken: Feb 69, 1969").fadeIn(interval)
                    });
                  }
                  else if ($(this).is(id_8))
                  {
                    $(header).fadeOut(interval, function(){
                      $(this).text("Garden of Knowledge").fadeIn(interval);
                    });
                    $(description).fadeOut(interval, function(){
                      $(this).text("Changed content 8").fadeIn(interval);
                    });
                    $(image).fadeOut(interval, function(){
                      $(this).html("<img src=\"img/qshs/Garden + Students.jpg\">").fadeIn(interval)
                    });
                    $(date).fadeOut(interval, function(){
                      $(this).text("Taken: Feb 69, 1969").fadeIn(interval)
                    });
                  }
                }, function (){
                  $(header).fadeOut(interval - 250, function(){
                    $(this).text(headerBuffer).fadeIn(interval);
                  });
                  $(description).fadeOut(interval - 250, function(){
                    $(this).text(textBuffer).fadeIn(interval);
                  });
                  $(image).fadeOut(interval - 250, function(){
                    $(this).html(imageBuffer).fadeIn(interval);
                  });
                  $(date).fadeOut(interval - 250, function(){
                    $(this).text(dateBuffer).fadeIn(interval);
                  });
                  }
                );

      // Script for admissions.html
      $(".ui.vertical.stripe.segment > .ui.attached.segment > .content_1, .content_2, .content_3, .content_4").hide();
      prev = "#step1";
      $("#step1, #step2, #step3, #step4").click(function()
      {
        $(".content_1, .content_2, .content_3, .content_4").hide();

        if($(this).attr("id") == "step1")
        {
          $(".content_1").fadeIn('slow');
          $(prev).removeClass("active");
          prev = $(this);
          $(this).addClass("active");
        }
        else if($(this).attr("id") == "step2")
        {
          $(".content_2").fadeIn('slow');
          $(prev).removeClass("active");
          prev = $(this);
          $(this).addClass("active");
        }
        else if($(this).attr("id") == "step3")
        {
          $(".content_3").fadeIn('slow');
          $(prev).removeClass("active");
          prev = $(this);
          $(this).addClass("active");
        }

        else if($(this).attr("id") == "step4")
        {
          $(".content_4").fadeIn('slow');
          $(prev).removeClass("active");
          prev = $(this);
          $(this).addClass("active");
        }

      });

      $('.ui.form').form({
        fields: {
          author: 'empty'
        }
      });

});
