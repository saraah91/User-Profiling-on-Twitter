function showDiv() {
   document.getElementById('stats').style.display = "block";
   //add something to update html based on json file
}
function sendFile(){
    var reader = new FileReader();
    reader.onload = onReaderLoad;
    reader.readAsText(document.querySelector('input').files[0]);


    function onReaderLoad(event){
      var data = JSON.stringify(event.target.result);
      console.log(data);
    }


$.post('/analyze', {
        data: "data",
    }).done(function(response) {
       numTweets = response["numTweets"]
    // display numTweets on the DOM
    })

}
