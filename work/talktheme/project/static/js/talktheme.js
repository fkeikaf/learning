function callDraw() {
    // Ajax通信を開始
    // $.ajax({
    //     url: 'http://localhost:8000/api/v1/talktheme/draw/',
    //     type: 'GET',
    //     contentType: 'application/json', 
    //     timeout: 5000,
    // })
    // .done(function(data) {
    //     // 通信成功時の処理を記述
    //     console.log(data);
    // })
    // .fail(function() {
    //     // 通信失敗時の処理を記述
    //     console.log("失敗");
    // });
    window.location.href = "http://localhost:8000/product/talktheme/draw/";
}

function callReset() {
    console.log("Reset")
}

