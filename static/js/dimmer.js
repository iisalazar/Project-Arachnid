$(document)
  .ready(function() {

    // selector cache
    var
      $pageDimmer = $('.demo.page.dimmer'),
      $demo       = $('.dimmer'),
      $showButton = $demo.find('.show.button'),
      $pageButton = $demo.find('.page.button'),
      $hideButton = $demo.find('.hide.button'),
      // alias
      handler
    ;

    // event handlers
    handler = {
      show: function() {
        $(this)
          .closest('.demo')
            .find('.segment')
              .dimmer('show')
        ;
      },
      hide: function() {
        $(this)
          .closest('.demo')
            .find('.segment')
              .dimmer('hide')
        ;
      },
      page: function() {
        $('body &gt; .demo.page.dimmer')
          .dimmer('show')
        ;
      }
    };

    $pageDimmer
      .dimmer()
    ;

    $pageButton
      .on('click', handler.page)
    ;
    $showButton
      .on('click', handler.show)
    ;
    $hideButton
      .on('click', handler.hide)
    ;

  })
;
