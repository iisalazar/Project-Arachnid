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
