alert("welcome to website")

let name = prompt("what is your name?")

if (!confirm("your name is " + name + " ?")) {
    name = prompt("what is your name?")
}
document.getElementById("name").innerHTML = name;