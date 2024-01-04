const stick1 = document.getElementById("stick1")
stick1.innerHTML = "<h1>nice</h1>"



stickElement = document.querySelectorAll("#stick1, #stick2, #stick3")
stickElement.forEach(element => {
    element.style.backgroundColor = "#fff"
    element.style.color = "#000"
    element.style.fontSize = "0.7em"
});

const galleryImages = document.createElement("img")


// let jobs = document.getElementsByname("select");
// var options = document.createElement("option");
// options.value = "other";
// options.innerText = "อื่นๆ";
// jobs.appendChild(options);