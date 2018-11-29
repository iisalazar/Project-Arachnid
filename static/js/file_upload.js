$(function () {
  /* 1. OPEN THE FILE EXPLORER WINDOW */
  $(".js-upload-photos").click(function () {
    $("#fileupload").click();
  });

  /* 2. INITIALIZE THE FILE UPLOAD COMPONENT */
  $("#fileupload").fileupload({
    dataType: 'json',
    sequentialUploads: true,  /* 1. SEND THE FILES ONE BY ONE */
    start: function (e) {  /* 2. WHEN THE UPLOADING PROCESS STARTS, SHOW THE MODAL */
      $(".ui.basic.modal").modal("show");
      $('.ui.basic.modal .actions #confirm_button').hide();
    },
    stop: function (e) {  /* 3. WHEN THE UPLOADING PROCESS FINALIZE, HIDE THE MODAL */
      $('.ui.basic.modal .actions #cancel_button').hide();
      $('.ui.basic.modal .actions #confirm_button').show();
      //$(".ui.basic.modal").modal("hide");
    },

    progressall: function (e, data) {  /* 4. UPDATE THE PROGRESS BAR */
      var progress = parseInt(data.loaded / data.total * 100, 10);
      var total = data.total
      var strProgress = progress + "%";
      //$(".progress-bar").css({"width": strProgress});
      //$(".progress-bar").text(strProgress);
      //$('.ui.basic.modal #progress').progress({percent : this.progress });
      $('.ui.basic.modal #progress').progress({
        percent: progress,
        total : total,
        text: {
          success: 'Successfully added photos',
          active: 'Uploading {percent}%',
        }
      });
    },

    done: function (e, data) {  /* 3. PROCESS THE RESPONSE FROM THE SERVER */
      if (data.result.is_valid) {
				console.log(data.result.url);
        $('.gallery.recently.uploaded').append("<img src='" + data.result.url + "' width='200'>");
      }
			else {
				console.log("fuck");
			}
    }
  });
});
