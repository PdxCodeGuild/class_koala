let target = document.getElementById("target");
let quoteButton = document.getElementById("quote-button");

quoteButton.addEventListener("click", function(e) {
    let req = new XMLHttpRequest();
    req.addEventListener("progress", function(e) {
        console.log(e.loaded);
        target.innerText = "Loading...";
    });
    req.addEventListener("error", function(e) {
        console.log(e.status);
        target.innerText = "Cannot load quote. Try again later!";
    });
    req.addEventListener("load", function(e) {
        console.log(req.responseText);
        let response = JSON.parse(req.responseText);
        console.log(response);
        let resultHTML = `
            <p>${response.quote.body}</p>
            <p><i><a href="${response.quote.url}">${response.quote.author}</a></i></p>
            `
        textTarget.innerHTML = resultHTML;
    });
    req.open("GET", "https://favqs.com/api/qotd");
    req.setRequestHeader("Authorization", 'Token token="62ed060e527356492260d09e11562aa2"');
    req.send()
});
