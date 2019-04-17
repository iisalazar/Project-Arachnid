$(function () {
  /* 1. OPEN THE FILE EXPLORER WINDOW */
  $(".ui.blue.button").click(function () {
    $("#fileupload").click();
  });

  /* 2. INITIALIZE THE FILE UPLOAD COMPONENT */
  $("#fileupload").fileupload({
    dataType: 'json',

    sequentialUploads: true,  /* 1. SEND THE FILES ONE BY ONE */
    start: function (e) {  /* 2. WHEN THE UPLOADING PROCESS STARTS, SHOW THE MODAL */
      $(".ui.basic.modal").modal("show");
      var segment = document.getElementById('uploaded-segments');
      segment.style.display = 'block'; // to show the segments section
      $(".ui.placeholder.segment .ui.icon.header#image-null-holder").remove();
    },
    stop: function (e) {  /* 3. WHEN THE UPLOADING PROCESS FINALIZE, HIDE THE MODAL */
      $(".ui.basic.modal").modal("hide");
    },

    progressall: function (e, data) {  /* 4. UPDATE THE PROGRESS BAR */
      var progress = parseInt(data.loaded / data.total * 100, 10);

      var total = data.total
      var strProgress = progress + "%";
      /* WHEN THE PROGRESS PERCENTAGE IS ABOVE THAN ZERO, THE DISPLAY PROGRESS*/
      if (progress > 0 ){
        $('.ui.basic.modal #progress').progress({
          percent: progress,
          text: {
            active: 'Uploading {percent}%',
            success: 'Successfully added photos'
          }
      });
      }
    },
    done: function (e, data) {  /* 3. PROCESS THE RESPONSE FROM THE SERVER */

      if (data.result.is_valid) {
				console.log(data.result.url);
        //$('#recently-uploaded .ui.icon.header').append("<img src='" + data.result.url + "' width='200'>");

        $('#recently-uploaded .ui.segments').append('<div class="ui segment">Uploaded <a href="#">'+ data.result.name +'</a></div>');
      }
			else {
				console.log("fuck");
			}
    }
  });
});
