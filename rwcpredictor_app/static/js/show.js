// $.ajax({
//     url: "pathto/filename.csv",
//     async: false,
//     success: function (csvd) {
//         data = $.csv2Array(csvd);
//     },
//     dataType: "text",
//     complete: function () {
//         // call a function on complete
//     }
// });

function showPrediction(elementID){
  document.getElementById(elementID).className = "text-center"
}
